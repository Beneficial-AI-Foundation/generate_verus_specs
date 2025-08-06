#!/usr/bin/env python3
"""
Script to move failed compilation files to a separate folder.
Reads the failed_files_list.txt and moves those files to a separate failed directory.

Usage: python3 move_failed_files.py <source_directory> [failed_directory]
"""

import os
import shutil
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Move failed compilation files to a separate folder.",
        epilog="Example: python3 move_failed_files.py benchmarks_no_bodies benchmarks_no_bodies_failed"
    )
    parser.add_argument("source_dir", help="Source directory containing the files")
    parser.add_argument("failed_dir", nargs="?", help="Directory for failed files (default: <source_dir>_failed)")
    parser.add_argument("--failed-list", default="failed_files_list.txt", help="File containing list of failed files (default: failed_files_list.txt)")
    
    args = parser.parse_args()
    
    # Paths
    failed_files_list = args.failed_list
    source_dir = Path(args.source_dir)
    if args.failed_dir:
        failed_dir = Path(args.failed_dir)
    else:
        failed_dir = Path(f"{args.source_dir}_failed")
    
    # Check if the failed files list exists
    if not os.path.exists(failed_files_list):
        print(f"Error: {failed_files_list} not found.")
        print("Please run the test_verus_compilation.py script first.")
        sys.exit(1)
    
    # Check if source directory exists
    if not source_dir.exists():
        print(f"Error: Source directory {source_dir} not found.")
        sys.exit(1)
    
    # Create the failed directory if it doesn't exist
    failed_dir.mkdir(exist_ok=True)
    
    # Read the list of failed files (skip comment lines starting with #)
    with open(failed_files_list, 'r') as f:
        failed_files = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    
    print(f"Moving failed files from {source_dir} to {failed_dir}")
    print(f"Found {len(failed_files)} failed files to move...")
    print("-" * 60)
    
    moved_count = 0
    not_found_count = 0
    
    for relative_path in failed_files:
        source_file = source_dir / relative_path
        target_file = failed_dir / relative_path
        
        # Check if file exists at the expected path
        if source_file.exists():
            # Create target directory if it doesn't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Move the file
            shutil.move(str(source_file), str(target_file))
            print(f"Moved: {relative_path}")
            moved_count += 1
        else:
            # Try to find the file in subdirectories (e.g., artifacts/)
            found = False
            for possible_path in source_dir.rglob(relative_path):
                if possible_path.is_file():
                    # Create target directory if it doesn't exist
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Move the file
                    shutil.move(str(possible_path), str(target_file))
                    print(f"Moved: {relative_path} (found at {possible_path.relative_to(source_dir)})")
                    moved_count += 1
                    found = True
                    break
            
            if not found:
                print(f"Not found: {relative_path}")
                not_found_count += 1
    
    print("-" * 60)
    print(f"SUMMARY:")
    print(f"  Files moved: {moved_count}")
    print(f"  Files not found: {not_found_count}")
    print(f"  Total failed files: {len(failed_files)}")
    
    if moved_count > 0:
        print(f"\nFailed files have been moved to: {failed_dir}")
        print(f"Remaining files in {source_dir} should all compile successfully with Verus.")
    
    # Create a README in the failed directory
    readme_content = f"""# Failed Verus Compilation Files

This directory contains {moved_count} files that failed to compile with `verus --no-verify`.

## Failure Categories:

1. **Platform-specific imports**: Files using Windows-specific modules on Linux
2. **Missing return statements**: Functions with empty bodies or incorrect default values
3. **Syntax errors**: Return statements in wrong contexts
4. **Type resolution errors**: Missing or undefined types
5. **Complex return types**: Tuples, references, and custom types not handled correctly

## Files:
"""
    
    for relative_path in failed_files:
        if (failed_dir / relative_path).exists():
            readme_content += f"- {relative_path}\n"
    
    readme_content += f"""
## Next Steps:

These files need manual review and fixing before they can be used for Verus proof synthesis.
The detailed error messages are available in `verus_compilation_failures.txt`.

Generated on: {moved_count} files moved from benchmarks_no_bodies/
"""
    
    with open(failed_dir / "README.md", "w") as f:
        f.write(readme_content)
    
    print(f"Created README.md in {failed_dir} with details about the failed files.")

if __name__ == "__main__":
    main()
