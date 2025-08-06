#!/usr/bin/env python3
"""
Script to generate cleanup commands for duplicate Verus files.
This script creates shell commands to remove duplicates safely.
"""

import os
import subprocess
from pathlib import Path

def generate_cleanup_commands():
    """Generate cleanup commands for the duplicates."""
    
    print("#!/bin/bash")
    print("# Auto-generated script to clean up duplicate Verus files")
    print("# Review each command before execution!")
    print("")
    
    # Get duplicate data
    result = subprocess.run(['python3', 'scripts/find_duplicate_files.py', 'benches'], 
                          capture_output=True, text=True, 
                          cwd='/home/lacra/git_repos/generate_verus_specs')
    
    lines = result.stdout.strip().split('\n')
    
    current_set = None
    duplicate_sets = []
    
    for line in lines:
        if line.startswith('Duplicate Set #'):
            if current_set:
                duplicate_sets.append(current_set)
            current_set = {'files': []}
        elif line.strip().startswith('Hash:'):
            pass  # We don't need the hash for cleanup
        elif line.strip() and '.' in line and '/' in line:
            # Extract file path
            if '. ' in line and ' (' in line:
                file_path = line.split('. ')[1].split(' (')[0]
                current_set['files'].append(file_path)
    
    if current_set:
        duplicate_sets.append(current_set)
    
    print("# 1. VerusProofSynthesisBench duplicates - Remove files from root, keep in subdirectories")
    print("echo 'Cleaning up VerusProofSynthesisBench duplicates...'")
    
    verus_count = 0
    for dup_set in duplicate_sets:
        files = dup_set['files']
        if len(files) == 2:
            verus_files = [f for f in files if 'VerusProofSynthesisBench/' in f]
            if len(verus_files) == 2:
                # Check if one is in root and one in subdirectory
                root_files = [f for f in verus_files if f.count('/') == 2]
                subdir_files = [f for f in verus_files if f.count('/') > 2]
                
                if len(root_files) == 1 and len(subdir_files) == 1:
                    print(f"rm '{root_files[0]}'  # Duplicate of {subdir_files[0]}")
                    verus_count += 1
    
    print(f"# Removed {verus_count} VerusProofSynthesisBench root duplicates")
    print("")
    
    print("# 2. HumanEval SubBench duplicates - Remove from SubBench directory")
    print("echo 'Cleaning up HumanEval SubBench duplicates...'")
    
    humaneval_count = 0
    for dup_set in duplicate_sets:
        files = dup_set['files']
        if len(files) == 2:
            humaneval_files = [f for f in files if 'HumanEval-RustBench/' in f]
            if len(humaneval_files) == 2:
                regular_files = [f for f in humaneval_files if '/SubBench/' not in f]
                subench_files = [f for f in humaneval_files if '/SubBench/' in f]
                
                if len(regular_files) == 1 and len(subench_files) == 1:
                    print(f"rm '{subench_files[0]}'  # Duplicate of {regular_files[0]}")
                    humaneval_count += 1
    
    print(f"# Removed {humaneval_count} HumanEval SubBench duplicates")
    print("")
    
    print("# 3. Autoverus cross-directory duplicates - Manual review needed")
    print("echo 'Autoverus cross-directory duplicates (review manually):'")
    
    autoverus_count = 0
    for dup_set in duplicate_sets:
        files = dup_set['files']
        if len(files) == 2:
            autoverus_files = [f for f in files if 'autoverus/' in f]
            if len(autoverus_files) == 2 and not any('VerusProofSynthesisBench' in f for f in files):
                print(f"# MANUAL REVIEW: {files[0]} == {files[1]}")
                autoverus_count += 1
    
    print(f"# Found {autoverus_count} autoverus cross-directory duplicates for manual review")
    print("")
    
    print("# 4. MBPP no_bodies duplicates - Manual review needed")
    print("echo 'MBPP no_bodies duplicates (review manually):'")
    
    mbpp_count = 0
    for dup_set in duplicate_sets:
        files = dup_set['files']
        if any('MBPP_no_bodies' in f for f in files):
            print(f"# MANUAL REVIEW: Different task IDs with same content:")
            for f in files:
                print(f"#   {f}")
            mbpp_count += 1
    
    print(f"# Found {mbpp_count} MBPP no_bodies duplicates for manual review")
    print("")
    
    print("# 5. Miscellaneous duplicates")
    print("echo 'Miscellaneous duplicates:'")
    
    misc_count = 0
    for dup_set in duplicate_sets:
        files = dup_set['files']
        # Check if it's not one of the above categories
        is_verus = len(files) == 2 and len([f for f in files if 'VerusProofSynthesisBench/' in f]) == 2
        is_humaneval = len(files) == 2 and len([f for f in files if 'HumanEval-RustBench/' in f]) == 2
        is_autoverus = len(files) == 2 and len([f for f in files if 'autoverus/' in f]) == 2 and not any('VerusProofSynthesisBench' in f for f in files)
        is_mbpp = any('MBPP_no_bodies' in f for f in files)
        
        if not (is_verus or is_humaneval or is_autoverus or is_mbpp):
            print(f"# REVIEW: Miscellaneous duplicate:")
            for f in files:
                print(f"#   {f}")
            # For the WIP file, suggest keeping ground_truth version
            if any('WIP' in f for f in files) and any('ground_truth' in f for f in files):
                wip_file = [f for f in files if 'WIP' in f][0]
                print(f"rm '{wip_file}'  # Keep ground_truth version")
            misc_count += 1
    
    print(f"# Found {misc_count} miscellaneous duplicates")
    print("")
    
    print("echo 'Cleanup complete! Review the manual items above.'")
    print(f"echo 'Automatically removed: {verus_count + humaneval_count + (1 if misc_count > 0 else 0)} files'")

def main():
    generate_cleanup_commands()

if __name__ == "__main__":
    main()
