#!/usr/bin/env python3
"""
Script to pick an arbitrary (random) file from a folder and run Verus on it.
"""

import os
import random
import subprocess
import sys
import argparse
from pathlib import Path
from verus_config import get_config

def find_rust_files(directory):
    """Find all .rs files in the given directory and subdirectories."""
    rust_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.rs'):
                rust_files.append(os.path.join(root, file))
    return rust_files

def run_verus(file_path, verus_path="verus", timeout=60, extra_args=None):
    """Run Verus on the specified file."""
    try:
        print(f"Running Verus on: {file_path}")
        print("-" * 50)
        
        # Run verus command
        cmd = [verus_path, "--no-verify"] + (extra_args or []) + [file_path]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("\nSTDERR:")
            print(result.stderr)
        
        print(f"\nReturn code: {result.returncode}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"Timeout: Verus took longer than {timeout} seconds on {file_path}")
        return False
    except FileNotFoundError:
        print(f"Error: Verus not found at '{verus_path}'. Please ensure Verus is installed and in PATH, or specify the path with --verus-path")
        return False
    except Exception as e:
        print(f"Error running Verus: {e}")
        return False

def main():
    # Load configuration
    config = get_config()
    
    parser = argparse.ArgumentParser(description="Pick a random Rust file and run Verus on it")
    parser.add_argument("directory", nargs="?", help="Directory to search for Rust files")
    parser.add_argument("--verus-path", 
                       default=config.get_verus_path(),
                       help=f"Path to Verus executable (default: from config or {config.get_verus_path()})")
    parser.add_argument("--timeout", type=int,
                       default=config.get_timeout('VERUS_RANDOM_TIMEOUT', 60),
                       help=f"Timeout per file in seconds (default: {config.get_timeout('VERUS_RANDOM_TIMEOUT', 60)})")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible file selection")
    parser.add_argument("--count", type=int, default=1, help="Number of random files to test (default: 1)")
    parser.add_argument("--config", help="Show current configuration and exit", action="store_true")
    
    args = parser.parse_args()
    
    # Show configuration if requested
    if args.config:
        config.print_config()
        return
    
    # Require directory if not just showing config
    if not args.directory:
        parser.error("directory is required (unless using --config)")
        return
    
    # Validate Verus path
    if not config.validate_verus_path(args.verus_path):
        sys.exit(1)
    
    # Check if directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        sys.exit(1)
    
    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        print(f"Using random seed: {args.seed}")
    
    # Find all Rust files
    print(f"Searching for Rust files in: {args.directory}")
    rust_files = find_rust_files(args.directory)
    
    if not rust_files:
        print("No Rust files found in the specified directory")
        sys.exit(1)
    
    print(f"Found {len(rust_files)} Rust files")
    extra_args = config.get_extra_args()
    if extra_args:
        print(f"Extra Verus arguments: {' '.join(extra_args)}")
    
    # Process the requested number of files
    success_count = 0
    for i in range(args.count):
        if args.count > 1:
            print(f"\n{'='*60}")
            print(f"Testing file {i+1}/{args.count}")
            print(f"{'='*60}")
        
        # Pick a random file
        selected_file = random.choice(rust_files)
        print(f"Selected file: {selected_file}")
        
        # Run Verus on the selected file
        success = run_verus(selected_file, args.verus_path, args.timeout, extra_args)
        if success:
            success_count += 1
    
    if args.count > 1:
        print(f"\n{'='*60}")
        print(f"Summary: {success_count}/{args.count} files compiled successfully")
        print(f"Success rate: {success_count/args.count*100:.1f}%")

if __name__ == "__main__":
    main()
