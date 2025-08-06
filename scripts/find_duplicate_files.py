#!/usr/bin/env python3
"""
Script to find duplicate Verus files in the benches directory.
Compares files by content hash and reports duplicates.
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
import argparse

def get_file_hash(file_path):
    """Calculate SHA-256 hash of file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_duplicates(directory):
    """Find duplicate files in the given directory."""
    # Dictionary to store hash -> list of files with that hash
    hash_to_files = defaultdict(list)
    
    # Find all .rs files
    rs_files = list(Path(directory).rglob("*.rs"))
    print(f"Found {len(rs_files)} .rs files in {directory}")
    
    # Calculate hashes for all files
    print("Calculating file hashes...")
    for file_path in rs_files:
        file_hash = get_file_hash(file_path)
        if file_hash:
            hash_to_files[file_hash].append(file_path)
    
    # Find duplicates (hashes with more than one file)
    duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}
    
    return duplicates

def get_file_size(file_path):
    """Get file size in bytes."""
    try:
        return os.path.getsize(file_path)
    except:
        return 0

def main():
    parser = argparse.ArgumentParser(description="Find duplicate Verus files")
    parser.add_argument("directory", nargs="?", default="benches", 
                       help="Directory to search for duplicates (default: benches)")
    parser.add_argument("--show-content", action="store_true", 
                       help="Show first few lines of duplicate files")
    
    args = parser.parse_args()
    
    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory '{directory}' not found!")
        return
    
    print(f"Searching for duplicate files in: {directory}")
    print("=" * 50)
    
    duplicates = find_duplicates(directory)
    
    if not duplicates:
        print("No duplicate files found!")
        return
    
    print(f"\nFound {len(duplicates)} sets of duplicate files:")
    print("=" * 50)
    
    total_duplicates = 0
    for i, (file_hash, files) in enumerate(duplicates.items(), 1):
        print(f"\nDuplicate Set #{i} ({len(files)} files):")
        print(f"Hash: {file_hash[:16]}...")
        
        # Sort files by path for consistent output
        files = sorted(files)
        
        # Show file info
        for j, file_path in enumerate(files):
            size = get_file_size(file_path)
            print(f"  {j+1}. {file_path} ({size} bytes)")
        
        total_duplicates += len(files) - 1  # Count extra copies
        
        # Show content preview if requested
        if args.show_content and files:
            try:
                with open(files[0], 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:10]  # First 10 lines
                print("    Content preview:")
                for line in lines:
                    print(f"    > {line.rstrip()}")
                if len(lines) == 10:
                    print("    > ...")
            except Exception as e:
                print(f"    Error reading content: {e}")
    
    print(f"\nSummary:")
    print(f"- Found {len(duplicates)} sets of duplicates")
    print(f"- Total duplicate files: {total_duplicates}")
    print(f"- Space could be saved by removing duplicates")

if __name__ == "__main__":
    main()
