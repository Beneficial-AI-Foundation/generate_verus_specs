#!/usr/bin/env python3
"""
Script to analyze patterns in duplicate Verus files and provide recommendations.
"""

import os
from pathlib import Path
from collections import defaultdict
import re
import hashlib

def find_duplicate_files_by_content(directory):
    """Find duplicate files by comparing their content."""
    file_hashes = defaultdict(list)
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Only check certain file types (Rust files, Python files, etc.)
            if file.endswith(('.rs', '.py', '.csv', '.txt', '.md')):
                file_path = os.path.join(root, file)
                try:
                    # Get file size
                    file_size = os.path.getsize(file_path)
                    
                    with open(file_path, 'rb') as f:
                        content = f.read()
                        # Calculate hash of file content
                        file_hash = hashlib.md5(content).hexdigest()
                        file_hashes[file_hash].append((file_path, file_size))
                except (IOError, OSError, UnicodeDecodeError):
                    # Skip files that can't be read
                    continue
    
    # Filter to only keep hashes with multiple files (duplicates)
    duplicate_sets = []
    for file_hash, file_info_list in file_hashes.items():
        if len(file_info_list) > 1:
            file_paths = [info[0] for info in file_info_list]
            file_size = file_info_list[0][1]  # All duplicates have same size
            
            # Read a snippet of content for display
            try:
                with open(file_paths[0], 'r', encoding='utf-8') as f:
                    content_preview = f.read(200)  # First 200 characters
            except:
                content_preview = "[Binary or unreadable content]"
            
            duplicate_sets.append({
                'hash': file_hash,
                'files': file_paths,
                'content_preview': content_preview,
                'file_size': file_size
            })
    
    return duplicate_sets

def analyze_duplicate_patterns(duplicates_output):
    """Analyze patterns in the duplicate files output."""
    lines = duplicates_output.strip().split('\n')
    
    # Parse the duplicates
    current_set = None
    duplicate_sets = []
    
    for line in lines:
        if line.startswith('Duplicate Set #'):
            if current_set:
                duplicate_sets.append(current_set)
            current_set = {'files': [], 'hash': ''}
        elif line.strip().startswith('Hash:'):
            current_set['hash'] = line.split('Hash: ')[1]
        elif re.match(r'\s+\d+\.\s+', line):
            # Extract file path
            file_path = line.split('. ')[1].split(' (')[0]
            current_set['files'].append(file_path)
    
    if current_set:
        duplicate_sets.append(current_set)
    
    return duplicate_sets

def categorize_duplicates(duplicate_sets):
    """Categorize duplicates by pattern."""
    categories = {
        'verus_proof_synthesis_duplicates': [],  # Files in both root and subdirectory
        'humaneval_subench_duplicates': [],      # HumanEval SubBench duplicates
        'autoverus_cross_directory': [],         # Cross-directory duplicates in autoverus
        'mbpp_no_bodies_duplicates': [],         # MBPP no_bodies duplicates
        'artifacts_duplicates': [],              # Files involving the artifacts folder
        'misc_duplicates': []                    # Other duplicates
    }
    
    for dup_set in duplicate_sets:
        files = dup_set['files']
        
        # Check for VerusProofSynthesisBench pattern (root vs subdirectory)
        verus_proof_files = [f for f in files if 'VerusProofSynthesisBench/' in f]
        if len(verus_proof_files) == 2 and len(files) == 2:
            # Check if one is in root and one in subdirectory
            root_files = [f for f in verus_proof_files if f.count('/') == 2]  # benches/VerusProofSynthesisBench/file.rs
            subdir_files = [f for f in verus_proof_files if f.count('/') > 2]  # benches/VerusProofSynthesisBench/subdir/file.rs
            
            if len(root_files) == 1 and len(subdir_files) == 1:
                categories['verus_proof_synthesis_duplicates'].append(dup_set)
                continue
        
        # Check for HumanEval SubBench pattern
        humaneval_files = [f for f in files if 'HumanEval-RustBench/' in f]
        if len(humaneval_files) == 2 and len(files) == 2:
            regular_files = [f for f in humaneval_files if '/SubBench/' not in f]
            subench_files = [f for f in humaneval_files if '/SubBench/' in f]
            
            if len(regular_files) == 1 and len(subench_files) == 1:
                categories['humaneval_subench_duplicates'].append(dup_set)
                continue
        
        # Check for autoverus cross-directory duplicates
        autoverus_files = [f for f in files if 'autoverus/' in f]
        if len(autoverus_files) == 2 and len(files) == 2:
            categories['autoverus_cross_directory'].append(dup_set)
            continue
        
        # Check for MBPP no_bodies duplicates
        if any('MBPP_no_bodies' in f for f in files):
            categories['mbpp_no_bodies_duplicates'].append(dup_set)
            continue
        
        # Check for artifacts folder duplicates
        artifacts_files = [f for f in files if 'artifacts/' in f]
        if artifacts_files:
            categories['artifacts_duplicates'].append(dup_set)
            continue
        
        # Everything else
        categories['misc_duplicates'].append(dup_set)
    
    return categories

def main():
    # Find duplicates by content within the benches directory
    
    print("Duplicate Verus Files Analysis (Content-Based)")
    print("=" * 50)
    
    benches_dir = '/home/lacra/git_repos/generate_verus_specs/benches'
    print(f"Scanning directory: {benches_dir}")
    print("Looking for files with identical content...")
    
    # Find duplicates by content
    duplicate_sets = find_duplicate_files_by_content(benches_dir)
    categories = categorize_duplicates(duplicate_sets)
    
    print(f"\nTotal duplicate sets found: {len(duplicate_sets)}")
    print("\nBreakdown by category:")
    print("-" * 30)
    
    # VerusProofSynthesisBench duplicates (root vs subdirectory)
    verus_dups = categories['verus_proof_synthesis_duplicates']
    print(f"\n1. VerusProofSynthesisBench duplicates: {len(verus_dups)} sets")
    print("   Pattern: Files exist both in root directory and subdirectories")
    if verus_dups:
        print("   Examples:")
        for i, dup_set in enumerate(verus_dups[:3]):
            print(f"     - {dup_set['files'][0]}")
            print(f"       {dup_set['files'][1]}")
    print("   Recommendation: Keep files in subdirectories, remove from root")
    
    # HumanEval SubBench duplicates
    humaneval_dups = categories['humaneval_subench_duplicates']
    print(f"\n2. HumanEval SubBench duplicates: {len(humaneval_dups)} sets")
    print("   Pattern: Files duplicated in SubBench subdirectory")
    if humaneval_dups:
        print("   Examples:")
        for dup_set in humaneval_dups[:3]:
            print(f"     - {dup_set['files'][0]}")
            print(f"       {dup_set['files'][1]}")
    print("   Recommendation: Keep either main directory or SubBench, but not both")
    
    # Autoverus cross-directory duplicates
    autoverus_dups = categories['autoverus_cross_directory']
    print(f"\n3. Autoverus cross-directory duplicates: {len(autoverus_dups)} sets")
    print("   Pattern: Same files in different autoverus subdirectories")
    if autoverus_dups:
        print("   Examples:")
        for i, dup_set in enumerate(autoverus_dups[:3]):
            print(f"     Set {i+1}:")
            for f in dup_set['files']:
                print(f"       - {f}")
            if 'content_preview' in dup_set:
                preview = dup_set['content_preview'].replace('\n', '\\n')[:100]
                print(f"       Content preview: {preview}...")
            print()
    print("   Recommendation: Consolidate into single location or use symbolic links")
    
    # MBPP no_bodies duplicates
    mbpp_dups = categories['mbpp_no_bodies_duplicates']
    print(f"\n4. MBPP no_bodies duplicates: {len(mbpp_dups)} sets")
    print("   Pattern: Different task IDs with identical content")
    if mbpp_dups:
        print("   Examples:")
        for i, dup_set in enumerate(mbpp_dups[:3]):
            print(f"     Set {i+1}:")
            for f in dup_set['files']:
                print(f"       - {f}")
            if 'content_preview' in dup_set:
                preview = dup_set['content_preview'].replace('\n', '\\n')[:100]
                print(f"       Content preview: {preview}...")
            print()
    print("   Recommendation: Investigate if these should actually be different")
    
    # Artifacts duplicates
    artifacts_dups = categories['artifacts_duplicates']
    print(f"\n5. Artifacts folder duplicates: {len(artifacts_dups)} sets")
    print("   Pattern: Files involving the artifacts folder")
    if artifacts_dups:
        print("   Examples:")
        for dup_set in artifacts_dups[:3]:
            for f in dup_set['files']:
                print(f"     - {f}")
            print()
    print("   Recommendation: Review if artifacts should be duplicated elsewhere")
    
    # Miscellaneous duplicates
    misc_dups = categories['misc_duplicates']
    print(f"\n6. Miscellaneous duplicates: {len(misc_dups)} sets")
    if misc_dups:
        print("   Examples:")
        for i, dup_set in enumerate(misc_dups[:3]):
            print(f"     Set {i+1}:")
            for f in dup_set['files']:
                print(f"       - {f}")
            if 'content_preview' in dup_set:
                preview = dup_set['content_preview'].replace('\n', '\\n')[:100]
                print(f"       Content preview: {preview}...")
            print()
    
    print(f"\nSummary:")
    print(f"- Most duplicates ({len(verus_dups)}) are VerusProofSynthesisBench files in both root and subdirs")
    print(f"- {len(humaneval_dups)} HumanEval files are duplicated in SubBench")
    print(f"- {len(autoverus_dups)} files are duplicated across autoverus directories")
    print(f"- {len(mbpp_dups)} MBPP tasks have identical content (may be legitimate)")
    print(f"- {len(artifacts_dups)} files involve the artifacts folder")
    print(f"- {len(misc_dups)} other miscellaneous duplicates exist")
    
    # Calculate space savings
    total_files = sum(len(dup_set['files']) for dup_set in duplicate_sets)
    duplicate_files = total_files - len(duplicate_sets)  # One original + extras
    total_wasted_space = sum((len(dup_set['files']) - 1) * dup_set.get('file_size', 0) for dup_set in duplicate_sets)
    
    print(f"\nPotential space savings: {duplicate_files} files could be removed")
    print(f"Total wasted space: {total_wasted_space:,} bytes ({total_wasted_space / 1024:.1f} KB)")
    
    # Show largest duplicates
    if duplicate_sets:
        largest_dups = sorted(duplicate_sets, key=lambda x: x.get('file_size', 0) * (len(x['files']) - 1), reverse=True)
        print(f"\nLargest space wasters:")
        for i, dup_set in enumerate(largest_dups[:3]):
            wasted = (len(dup_set['files']) - 1) * dup_set.get('file_size', 0)
            print(f"{i+1}. {wasted:,} bytes wasted by {len(dup_set['files'])} copies of {dup_set.get('file_size', 0):,} byte files")
            print(f"   Example: {os.path.basename(dup_set['files'][0])}")

if __name__ == "__main__":
    main()
