#!/usr/bin/env python3
"""
Script to test compilation of all generated Verus files using verus --no-verify.
Reports the number of files that compiled successfully and lists failed files.

Usage: python3 test_verus_compilation.py <directory> [verus_path]
"""

import os
import subprocess
import sys
import argparse
from pathlib import Path

def run_verus_on_file(verus_path, file_path):
    """
    Run verus --no-verify on a single file.
    Returns (success: bool, output: str, error: str)
    """
    try:
        cmd = [verus_path, "--no-verify", str(file_path)]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout per file
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout (30s)"
    except Exception as e:
        return False, "", f"Exception: {e}"

def find_rust_files(directory):
    """Find all .rs files in the directory recursively."""
    rust_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.rs'):
                rust_files.append(Path(root) / file)
    return rust_files

def main():
    parser = argparse.ArgumentParser(
        description="Test compilation of Verus files using verus --no-verify.",
        epilog="Example: python3 test_verus_compilation.py benchmarks_no_bodies"
    )
    parser.add_argument("directory", help="Directory containing Verus files to test")
    parser.add_argument("verus_path", nargs="?", 
                       default=os.path.expanduser("~/Downloads/verus-0.2025.07.15.62362b0-x86-linux/verus-x86-linux/./verus"),
                       help="Path to Verus executable (default: ~/Downloads/verus-0.2025.07.15.62362b0-x86-linux/verus-x86-linux/./verus)")
    
    args = parser.parse_args()
    
    verus_path = args.verus_path
    test_dir = Path(args.directory)
    
    # Check if verus exists
    if not os.path.exists(verus_path):
        print(f"Error: Verus executable not found at {verus_path}")
        print("Please provide the correct path to the Verus executable.")
        sys.exit(1)
    
    # Check if directory exists
    if not test_dir.exists():
        print(f"Error: Directory {test_dir} not found.")
        sys.exit(1)
    
    # Find all Rust files
    rust_files = find_rust_files(test_dir)
    
    if not rust_files:
        print(f"No .rs files found in {test_dir}")
        sys.exit(1)
    
    print(f"Testing directory: {test_dir}")
    print(f"Found {len(rust_files)} Rust files to test...")
    print(f"Using Verus executable: {verus_path}")
    print("-" * 60)
    
    successful_files = []
    failed_files = []
    
    for i, file_path in enumerate(rust_files, 1):
        relative_path = file_path.relative_to(test_dir)
        print(f"[{i:3d}/{len(rust_files)}] Testing {relative_path}... ", end="", flush=True)
        
        success, stdout, stderr = run_verus_on_file(verus_path, file_path)
        
        if success:
            print("✓ SUCCESS")
            successful_files.append(file_path)
        else:
            print("✗ FAILED")
            failed_files.append((file_path, stderr))
    
    print("-" * 60)
    print(f"SUMMARY:")
    print(f"  Total files tested: {len(rust_files)}")
    print(f"  Successful: {len(successful_files)} ({len(successful_files)/len(rust_files)*100:.1f}%)")
    print(f"  Failed: {len(failed_files)} ({len(failed_files)/len(rust_files)*100:.1f}%)")
    
    if failed_files:
        print(f"\nFAILED FILES:")
        print("=" * 60)
        
        # Write detailed failure report to file
        with open("verus_compilation_failures.txt", "w") as f:
            f.write(f"Verus Compilation Failure Report\n")
            f.write(f"Generated on: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n")
            f.write(f"Total files tested: {len(rust_files)}\n")
            f.write(f"Failed files: {len(failed_files)}\n")
            f.write("=" * 60 + "\n\n")
            
            for file_path, error in failed_files:
                relative_path = file_path.relative_to(test_dir)
                print(f"  - {relative_path}")
                
                f.write(f"File: {relative_path}\n")
                f.write("-" * 40 + "\n")
                f.write(f"Error output:\n{error}\n")
                f.write("\n" + "=" * 60 + "\n\n")
        
        print(f"\nDetailed failure report written to: verus_compilation_failures.txt")
        
        # Also create a simple list of failed files
        with open("failed_files_list.txt", "w") as f:
            for file_path, _ in failed_files:
                relative_path = file_path.relative_to(test_dir)
                f.write(f"{relative_path}\n")
        
        print(f"List of failed files written to: failed_files_list.txt")
    
    else:
        print("\n🎉 All files compiled successfully!")
    
    return len(failed_files) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
