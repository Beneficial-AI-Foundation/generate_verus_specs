#!/usr/bin/env python3
"""
Script to find and compare Clover benchmark files between the two directories.
"""

import os
from pathlib import Path
import re

def extract_clover_function_name(file_path):
    """Extract the Clover function name from the file path."""
    path_str = str(file_path)
    
    # Look for Clover_ prefix in artifacts
    match = re.search(r'Clover_([^/]+)', path_str)
    if match:
        return match.group(1)
    
    # Look for function name in benches
    if 'CloverBench' in path_str:
        filename = Path(file_path).stem
        # Remove common suffixes
        name = re.sub(r'(_strong|_weak)$', '', filename)
        return name
    
    return None

def read_file_content(file_path, max_lines=100):
    """Read file content safely."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return ''.join(lines[:max_lines])
    except Exception as e:
        return f"Error reading file: {e}"

def find_clover_pairs(specs_benches, specs_artifacts):
    """Find matching Clover benchmark pairs."""
    
    # Get all Clover files from artifacts
    artifacts_clover = {}
    for file_path in Path(specs_artifacts).rglob("*.rs"):
        if 'Clover_' in str(file_path):
            func_name = extract_clover_function_name(file_path)
            if func_name:
                artifacts_clover[func_name] = file_path
    
    # Get all Clover files from benches
    benches_clover = {}
    for file_path in Path(specs_benches).rglob("*.rs"):
        if 'CloverBench' in str(file_path):
            func_name = extract_clover_function_name(file_path)
            if func_name:
                if func_name not in benches_clover:
                    benches_clover[func_name] = []
                benches_clover[func_name].append(file_path)
    
    print(f"Found {len(artifacts_clover)} Clover functions in specs_from_artifacts")
    print(f"Found {len(benches_clover)} Clover functions in specs_benches")
    
    # Find matches
    matches = []
    for func_name in artifacts_clover:
        if func_name in benches_clover:
            matches.append((func_name, artifacts_clover[func_name], benches_clover[func_name]))
    
    return matches

def main():
    scripts_dir = Path(__file__).parent
    specs_benches = scripts_dir / "specs_benches"
    specs_from_artifacts = scripts_dir / "specs_from_artifacts"
    
    print("Finding Clover benchmark matches...")
    print("="*60)
    
    matches = find_clover_pairs(specs_benches, specs_from_artifacts)
    
    if not matches:
        print("No matching Clover functions found!")
        return
    
    print(f"\nFound {len(matches)} matching Clover functions:")
    print("="*60)
    
    for func_name, artifacts_file, benches_files in matches:
        print(f"\nFunction: {func_name}")
        print(f"  specs_from_artifacts: {artifacts_file}")
        
        for bench_file in benches_files:
            print(f"  specs_benches:        {bench_file}")
        
        # Show brief content comparison for first few
        if len([m for m in matches if m[0] <= func_name]) <= 3:
            print("\n  Content preview (artifacts):")
            content = read_file_content(artifacts_file, 20)
            for i, line in enumerate(content.split('\n')[:10]):
                print(f"    {i+1:2d}: {line}")
            
            if benches_files:
                print(f"\n  Content preview (benches - {Path(benches_files[0]).name}):")
                content = read_file_content(benches_files[0], 20)
                for i, line in enumerate(content.split('\n')[:10]):
                    print(f"    {i+1:2d}: {line}")
        
        print("-" * 40)

if __name__ == "__main__":
    main()
