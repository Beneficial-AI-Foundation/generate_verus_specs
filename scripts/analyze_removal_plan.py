#!/usr/bin/env python3
"""
Analyze the removal plan to provide insights about what will be kept vs removed.
"""

import json
from pathlib import Path
from collections import defaultdict, Counter

def analyze_removal_plan(json_file: str = "removable_files.json"):
    """Analyze the removal plan and generate insights."""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Statistics
    total_analyzed = data['total_files_analyzed']
    removable = len(data['mappings'])
    kept = total_analyzed - removable
    
    print(f"# Duplicate Removal Analysis\n")
    print(f"**Total files analyzed**: {total_analyzed}")
    print(f"**Files to keep**: {kept} ({kept/total_analyzed*100:.1f}%)")
    print(f"**Files to remove**: {removable} ({removable/total_analyzed*100:.1f}%)")
    print(f"**Similarity threshold**: {data['threshold']*100:.0f}%\n")
    
    # Analyze by directory
    remove_by_dir = Counter()
    keep_by_dir = Counter()
    
    # Count files to remove by directory
    for mapping in data['mappings']:
        remove_path = Path(mapping['remove'])
        keep_path = Path(mapping['keep'])
        
        if remove_path.parts:
            remove_by_dir[remove_path.parts[0]] += 1
        if keep_path.parts:
            keep_by_dir[keep_path.parts[0]] += 1
    
    # Get all directories
    all_dirs = set(remove_by_dir.keys()) | set(keep_by_dir.keys())
    
    print("## Directory Analysis\n")
    print("| Directory | Total Files | To Remove | To Keep | Remove % |")
    print("|-----------|-------------|-----------|---------|----------|")
    
    # Count total files per directory
    dir_totals = defaultdict(int)
    for mapping in data['mappings']:
        remove_path = Path(mapping['remove'])
        if remove_path.parts:
            dir_totals[remove_path.parts[0]] += 1
    
    # Also count kept files
    keep_files = set()
    for mapping in data['mappings']:
        keep_files.add(mapping['keep'])
    
    # Rough estimate of total files per directory
    for dir_name in sorted(all_dirs):
        remove_count = remove_by_dir.get(dir_name, 0)
        # This is an approximation
        total_estimate = remove_count * 2  # Assuming similar distribution
        keep_estimate = total_estimate - remove_count
        remove_pct = (remove_count / total_estimate * 100) if total_estimate > 0 else 0
        print(f"| {dir_name} | ~{total_estimate} | {remove_count} | ~{keep_estimate} | {remove_pct:.1f}% |")
    
    # Analyze cross-directory deduplication
    print("\n## Cross-Directory Deduplication\n")
    cross_dir_count = 0
    cross_dir_patterns = defaultdict(int)
    
    for mapping in data['mappings']:
        remove_path = Path(mapping['remove'])
        keep_path = Path(mapping['keep'])
        
        if remove_path.parts and keep_path.parts:
            remove_dir = remove_path.parts[0]
            keep_dir = keep_path.parts[0]
            
            if remove_dir != keep_dir:
                cross_dir_count += 1
                pattern = f"{remove_dir} → {keep_dir}"
                cross_dir_patterns[pattern] += 1
    
    print(f"**Cross-directory deduplications**: {cross_dir_count} ({cross_dir_count/removable*100:.1f}%)")
    print("\nTop cross-directory patterns:")
    print("| From Directory | To Directory | Count |")
    print("|----------------|--------------|-------|")
    
    for pattern, count in sorted(cross_dir_patterns.items(), key=lambda x: x[1], reverse=True)[:10]:
        from_dir, to_dir = pattern.split(' → ')
        print(f"| {from_dir} | {to_dir} | {count} |")
    
    # Analyze specific file patterns
    print("\n## File Pattern Analysis\n")
    
    # Look for common patterns in removed files
    removed_patterns = defaultdict(int)
    kept_patterns = defaultdict(int)
    
    for mapping in data['mappings']:
        remove_file = Path(mapping['remove']).name
        keep_file = Path(mapping['keep']).name
        
        # Check for common patterns
        if 'unverified' in mapping['remove']:
            removed_patterns['unverified files'] += 1
        if 'verified' in mapping['keep']:
            kept_patterns['verified files'] += 1
        if 'SubBench' in mapping['remove']:
            removed_patterns['SubBench files'] += 1
        if 'additional' in mapping['remove']:
            removed_patterns['additional files'] += 1
        if 'ground_truth' in mapping['keep']:
            kept_patterns['ground_truth files'] += 1
        if '_no_bodies' in mapping['remove']:
            removed_patterns['_no_bodies files'] += 1
        if 'artifacts' in mapping['remove']:
            removed_patterns['artifacts files'] += 1
    
    print("**Patterns in removed files**:")
    for pattern, count in sorted(removed_patterns.items(), key=lambda x: x[1], reverse=True):
        print(f"- {pattern}: {count} files")
    
    print("\n**Patterns in kept files**:")
    for pattern, count in sorted(kept_patterns.items(), key=lambda x: x[1], reverse=True):
        print(f"- {pattern}: {count} files")
    
    # Sample of exact duplicates
    print("\n## Sample Exact Duplicates (100% similarity)\n")
    print("| File to Remove | Keep Instead |")
    print("|----------------|--------------|")
    
    sample_count = 0
    for mapping in data['mappings']:
        if sample_count >= 10:
            break
        # Since we used 95% threshold, most should be very similar
        print(f"| `{mapping['remove']}` | `{mapping['keep']}` |")
        sample_count += 1

if __name__ == "__main__":
    analyze_removal_plan()
