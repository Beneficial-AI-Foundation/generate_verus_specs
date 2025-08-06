#!/usr/bin/env python3
"""
Script to find duplicate Verus files between specs_from_artifacts and specs_benches directories.
Compares files by content hash and reports duplicates.
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict

def get_file_hash(file_path):
    """Calculate SHA-256 hash of file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_files_with_hashes(directory):
    """Find all .rs files in directory and return dict of hash -> file_path."""
    hash_to_file = {}
    
    # Find all .rs files
    rs_files = list(Path(directory).rglob("*.rs"))
    print(f"Found {len(rs_files)} .rs files in {directory}")
    
    # Calculate hashes for all files
    for file_path in rs_files:
        file_hash = get_file_hash(file_path)
        if file_hash:
            hash_to_file[file_hash] = file_path
    
    return hash_to_file

def find_cross_directory_duplicates(dir1, dir2):
    """Find files that appear in both directories."""
    print(f"Comparing files between {dir1} and {dir2}")
    print("=" * 60)
    
    # Get hashes for both directories
    dir1_hashes = find_files_with_hashes(dir1)
    dir2_hashes = find_files_with_hashes(dir2)
    
    # Find common hashes
    common_hashes = set(dir1_hashes.keys()) & set(dir2_hashes.keys())
    
    if not common_hashes:
        print("No duplicate files found between directories!")
        return
    
    print(f"\nFound {len(common_hashes)} duplicate files:")
    print("=" * 60)
    
    for i, file_hash in enumerate(sorted(common_hashes), 1):
        file1 = dir1_hashes[file_hash]
        file2 = dir2_hashes[file_hash]
        
        print(f"\nDuplicate #{i}:")
        print(f"Hash: {file_hash[:16]}...")
        print(f"  specs_benches:     {file1}")
        print(f"  specs_from_artifacts: {file2}")
        
        # Show file sizes
        try:
            size1 = os.path.getsize(file1)
            size2 = os.path.getsize(file2)
            print(f"  Sizes: {size1} bytes vs {size2} bytes")
        except:
            pass

def main():
    scripts_dir = Path(__file__).parent
    specs_benches = scripts_dir / "specs_benches"
    specs_from_artifacts = scripts_dir / "specs_from_artifacts"
    
    if not specs_benches.exists():
        print(f"Error: Directory '{specs_benches}' not found!")
        return
    
    if not specs_from_artifacts.exists():
        print(f"Error: Directory '{specs_from_artifacts}' not found!")
        return
    
    find_cross_directory_duplicates(specs_benches, specs_from_artifacts)

if __name__ == "__main__":
    main()
