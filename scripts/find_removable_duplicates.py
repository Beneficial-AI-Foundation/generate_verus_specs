#!/usr/bin/env python3
"""
Script to identify files that can be safely removed based on high similarity.
For each removable file, provides a similar file that should be kept.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter
from typing import Set, Dict, List, Tuple
import argparse

def tokenize_file(file_path: Path) -> Set[str]:
    """
    Tokenize a file into a set of tokens.
    Removes comments and normalizes tokens for better comparison.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()
    
    # Remove single-line comments
    content = re.sub(r'//[^\n]*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Tokenize: split on non-alphanumeric characters
    tokens = re.findall(r'\b\w+\b', content.lower())
    
    # Filter out very short tokens (likely not meaningful)
    tokens = [t for t in tokens if len(t) > 1]
    
    return set(tokens)

def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    """
    Calculate Jaccard similarity between two sets.
    Returns a value between 0 and 1, where 1 means identical sets.
    """
    if not set1 and not set2:
        return 1.0
    if not set1 or not set2:
        return 0.0
    
    intersection = set1 & set2
    union = set1 | set2
    
    return len(intersection) / len(union)

def get_file_info(file_path: Path) -> Dict:
    """Get file information including size and modification time."""
    stat = file_path.stat()
    return {
        'size': stat.st_size,
        'mtime': stat.st_mtime,
        'lines': sum(1 for _ in open(file_path, 'rb'))
    }

def prioritize_files(files: List[Path], base_dir: Path) -> List[Tuple[Path, int]]:
    """
    Assign priority scores to files to determine which to keep.
    Higher score = higher priority to keep.
    """
    scored_files = []
    
    for file in files:
        score = 0
        rel_path = file.relative_to(base_dir)
        path_parts = rel_path.parts
        
        # Prefer files in 'verified' directories
        if 'verified' in str(rel_path).lower():
            score += 100
        elif 'unverified' in str(rel_path).lower():
            score -= 50
        
        # Prefer files in ground_truth directories
        if 'ground_truth' in str(rel_path).lower():
            score += 80
        
        # Prefer files with cleaner paths (fewer subdirectories)
        score -= len(path_parts) * 5
        
        # Prefer files not in 'artifacts' or 'tmp' directories
        if 'artifacts' in path_parts or 'tmp' in path_parts:
            score -= 30
        
        # Prefer files with simpler names (no 'copy', 'duplicate', etc.)
        filename = file.stem.lower()
        if any(word in filename for word in ['copy', 'duplicate', 'tmp', 'temp', 'old', 'backup']):
            score -= 20
        
        # Prefer files with task_id in standard locations
        if 'task_id' in filename and ('MBPP' in str(rel_path) or 'HumanEval' in str(rel_path)):
            score += 10
        
        # Get file info for additional scoring
        try:
            info = get_file_info(file)
            # Slightly prefer larger files (might be more complete)
            score += min(info['lines'] / 100, 10)
        except:
            pass
        
        scored_files.append((file, score))
    
    return scored_files

def find_duplicate_groups(directory: Path, threshold: float = 0.95) -> List[List[Path]]:
    """
    Find groups of highly similar files.
    Returns groups where files have similarity >= threshold.
    """
    rust_files = list(directory.rglob("*.rs"))
    print(f"Found {len(rust_files)} Rust files in {directory}")
    
    # Tokenize all files
    file_tokens = {}
    print("Tokenizing files...")
    for i, file_path in enumerate(rust_files):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(rust_files)} files...")
        file_tokens[file_path] = tokenize_file(file_path)
    
    # Build similarity graph
    print("Building similarity graph...")
    adjacency = defaultdict(set)
    similar_pairs = []
    
    for i, file1 in enumerate(rust_files):
        if i % 50 == 0:
            print(f"  Processing file {i}/{len(rust_files)}...")
        
        for j in range(i + 1, len(rust_files)):
            file2 = rust_files[j]
            similarity = jaccard_similarity(file_tokens[file1], file_tokens[file2])
            
            if similarity >= threshold:
                adjacency[file1].add(file2)
                adjacency[file2].add(file1)
                similar_pairs.append((file1, file2, similarity))
    
    # Find connected components (duplicate groups)
    visited = set()
    groups = []
    
    for file in rust_files:
        if file not in visited and file in adjacency:
            # BFS to find all connected files
            group = set()
            queue = [file]
            
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.add(current)
                    group.add(current)
                    queue.extend(adjacency[current] - visited)
            
            if len(group) > 1:
                groups.append(list(group))
    
    return groups, similar_pairs

def determine_removable_files(groups: List[List[Path]], base_dir: Path) -> Dict[Path, Path]:
    """
    For each group of similar files, determine which can be removed and which to keep.
    Returns a mapping of removable_file -> file_to_keep.
    """
    removable_mapping = {}
    
    for group_id, group in enumerate(groups):
        # Score and sort files in the group
        scored_files = prioritize_files(group, base_dir)
        scored_files.sort(key=lambda x: x[1], reverse=True)
        
        # The file with the highest score is kept
        file_to_keep = scored_files[0][0]
        
        # All others can be removed
        for file, score in scored_files[1:]:
            removable_mapping[file] = file_to_keep
    
    return removable_mapping

def generate_removal_report(removable_mapping: Dict[Path, Path], similar_pairs: List, 
                          base_dir: Path, output_file: str = "removable_files_report.md"):
    """Generate a detailed report of files that can be removed."""
    
    # Group removable files by their keep file
    keep_to_remove = defaultdict(list)
    for remove_file, keep_file in removable_mapping.items():
        keep_to_remove[keep_file].append(remove_file)
    
    # Create similarity lookup
    similarity_lookup = {}
    for file1, file2, sim in similar_pairs:
        similarity_lookup[(file1, file2)] = sim
        similarity_lookup[(file2, file1)] = sim
    
    with open(output_file, 'w') as f:
        f.write("# Removable Files Report\n\n")
        f.write(f"**Total files that can be removed**: {len(removable_mapping)}\n")
        f.write(f"**Number of unique file groups**: {len(keep_to_remove)}\n\n")
        
        # Calculate space savings
        total_size = 0
        for file in removable_mapping:
            try:
                total_size += file.stat().st_size
            except:
                pass
        
        f.write(f"**Estimated space savings**: {total_size / 1024 / 1024:.2f} MB\n\n")
        
        f.write("## File Groups\n\n")
        f.write("Each group shows the file to keep and the similar files that can be removed.\n\n")
        
        # Sort by number of removable files
        sorted_groups = sorted(keep_to_remove.items(), 
                             key=lambda x: len(x[1]), reverse=True)
        
        for i, (keep_file, remove_files) in enumerate(sorted_groups[:50]):  # Top 50 groups
            keep_rel = keep_file.relative_to(base_dir)
            f.write(f"### Group {i+1}: Keep `{keep_rel}`\n\n")
            f.write(f"**Files that can be removed** ({len(remove_files)} files):\n\n")
            
            for remove_file in remove_files[:10]:  # Show up to 10 files
                remove_rel = remove_file.relative_to(base_dir)
                similarity = similarity_lookup.get((keep_file, remove_file), 0)
                f.write(f"- `{remove_rel}` (similarity: {similarity:.1%})\n")
            
            if len(remove_files) > 10:
                f.write(f"- ... and {len(remove_files) - 10} more files\n")
            
            f.write("\n")
        
        if len(sorted_groups) > 50:
            f.write(f"\n... and {len(sorted_groups) - 50} more groups\n\n")
        
        # Summary by directory
        f.write("\n## Summary by Directory\n\n")
        dir_counts = Counter()
        for file in removable_mapping:
            # Get top-level directory under base_dir
            rel_path = file.relative_to(base_dir)
            if len(rel_path.parts) > 0:
                dir_counts[rel_path.parts[0]] += 1
        
        f.write("| Directory | Files to Remove |\n")
        f.write("|-----------|----------------|\n")
        for dir_name, count in dir_counts.most_common():
            f.write(f"| {dir_name} | {count} |\n")

def generate_removal_script(removable_mapping: Dict[Path, Path], base_dir: Path, 
                          output_file: str = "remove_duplicates.sh"):
    """Generate a shell script to remove the duplicate files."""
    
    with open(output_file, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Script to remove duplicate files\n")
        f.write("# Generated by find_removable_duplicates.py\n\n")
        
        f.write("# Create a backup directory\n")
        f.write("BACKUP_DIR=\"removed_duplicates_backup_$(date +%Y%m%d_%H%M%S)\"\n")
        f.write("mkdir -p \"$BACKUP_DIR\"\n\n")
        
        f.write("echo \"Backing up and removing duplicate files...\"\n")
        f.write("echo \"Backup directory: $BACKUP_DIR\"\n\n")
        
        # Group by directory for better organization
        by_dir = defaultdict(list)
        for remove_file, keep_file in removable_mapping.items():
            rel_path = remove_file.relative_to(base_dir)
            by_dir[rel_path.parts[0]].append((remove_file, keep_file))
        
        total_files = len(removable_mapping)
        f.write(f"# Total files to remove: {total_files}\n\n")
        
        count = 0
        for directory, files in sorted(by_dir.items()):
            f.write(f"# Directory: {directory} ({len(files)} files)\n")
            
            for remove_file, keep_file in files:
                count += 1
                remove_rel = remove_file.relative_to(base_dir)
                keep_rel = keep_file.relative_to(base_dir)
                
                # Create backup directory structure
                f.write(f"# File {count}/{total_files}: {remove_rel}\n")
                f.write(f"# Duplicate of: {keep_rel}\n")
                f.write(f'mkdir -p "$BACKUP_DIR/{remove_rel.parent}"\n')
                f.write(f'cp "{remove_rel}" "$BACKUP_DIR/{remove_rel}"\n')
                f.write(f'rm "{remove_rel}"\n\n')
        
        f.write('echo "Done! Files backed up to $BACKUP_DIR"\n')
        f.write('echo "To restore: cp -r $BACKUP_DIR/* ."\n')
    
    # Make script executable
    os.chmod(output_file, 0o755)

def main():
    parser = argparse.ArgumentParser(description='Find removable duplicate files')
    parser.add_argument('--directory', '-d', type=str, default='benches',
                        help='Directory to analyze (default: benches)')
    parser.add_argument('--threshold', '-t', type=float, default=0.95,
                        help='Similarity threshold (0.0-1.0, default: 0.95)')
    parser.add_argument('--output', '-o', type=str, default='removable_files_report.md',
                        help='Output report file')
    parser.add_argument('--script', '-s', type=str, default='remove_duplicates.sh',
                        help='Output removal script')
    parser.add_argument('--json', '-j', type=str, help='Also save results as JSON')
    
    args = parser.parse_args()
    
    # Convert to Path object
    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return
    
    print(f"Finding duplicate files in '{directory}' with threshold {args.threshold:.1%}")
    
    # Find duplicate groups
    groups, similar_pairs = find_duplicate_groups(directory, args.threshold)
    
    print(f"\nFound {len(groups)} groups of similar files")
    
    # Determine which files can be removed
    removable_mapping = determine_removable_files(groups, directory)
    
    print(f"Identified {len(removable_mapping)} files that can be removed")
    
    # Generate reports
    print(f"\nGenerating report to '{args.output}'...")
    generate_removal_report(removable_mapping, similar_pairs, directory, args.output)
    
    print(f"Generating removal script to '{args.script}'...")
    generate_removal_script(removable_mapping, directory, args.script)
    
    # Save JSON if requested
    if args.json:
        print(f"Saving JSON results to '{args.json}'...")
        json_data = {
            'total_files_analyzed': len(list(directory.rglob("*.rs"))),
            'threshold': args.threshold,
            'duplicate_groups': len(groups),
            'removable_files': len(removable_mapping),
            'mappings': [
                {
                    'remove': str(remove.relative_to(directory)),
                    'keep': str(keep.relative_to(directory))
                }
                for remove, keep in removable_mapping.items()
            ]
        }
        with open(args.json, 'w') as f:
            json.dump(json_data, f, indent=2)
    
    print(f"\nAnalysis complete!")
    print(f"Report saved to: {args.output}")
    print(f"Removal script saved to: {args.script}")
    print(f"\nTo remove duplicates, run: bash {args.script}")

if __name__ == "__main__":
    main()
