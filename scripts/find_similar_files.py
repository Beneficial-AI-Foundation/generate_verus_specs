#!/usr/bin/env python3
"""
Script to find potentially similar files between specs_from_artifacts and specs_benches.
Looks for files with similar names, common prefixes, or overlapping content patterns.
"""

import os
from pathlib import Path
import re
from difflib import SequenceMatcher

def get_all_rust_files(directory):
    """Get all .rs files in directory with their relative paths."""
    files = []
    for file_path in Path(directory).rglob("*.rs"):
        relative_path = file_path.relative_to(directory)
        files.append((str(relative_path), file_path))
    return files

def extract_name_components(filename):
    """Extract meaningful components from filename."""
    # Remove .rs extension
    name = Path(filename).stem
    
    # Split on common separators
    components = re.split(r'[_\-\s]+', name.lower())
    
    # Remove common prefixes/suffixes
    filtered = []
    for comp in components:
        if comp and comp not in ['tmp', 'verus', 'code', 'spec', 'rs']:
            filtered.append(comp)
    
    return filtered

def name_similarity(name1, name2):
    """Calculate similarity between two filenames."""
    comp1 = extract_name_components(name1)
    comp2 = extract_name_components(name2)
    
    # Check for common components
    common = set(comp1) & set(comp2)
    total = set(comp1) | set(comp2)
    
    if not total:
        return 0.0
    
    return len(common) / len(total)

def find_similar_names(specs_benches_files, specs_artifacts_files, threshold=0.3):
    """Find files with similar names."""
    similar_pairs = []
    
    for artifacts_rel, artifacts_path in specs_artifacts_files:
        artifacts_name = Path(artifacts_rel).name
        
        for benches_rel, benches_path in specs_benches_files:
            benches_name = Path(benches_rel).name
            
            similarity = name_similarity(artifacts_name, benches_name)
            if similarity >= threshold:
                similar_pairs.append((
                    similarity,
                    benches_rel, benches_path,
                    artifacts_rel, artifacts_path
                ))
    
    return sorted(similar_pairs, key=lambda x: x[0], reverse=True)

def check_clover_matches(specs_benches_files, specs_artifacts_files):
    """Check for Clover benchmark matches specifically."""
    clover_artifacts = []
    clover_benches = []
    
    # Find Clover files in artifacts
    for rel_path, full_path in specs_artifacts_files:
        if 'clover' in rel_path.lower():
            clover_artifacts.append((rel_path, full_path))
    
    # Find Clover files in benches
    for rel_path, full_path in specs_benches_files:
        if 'clover' in rel_path.lower():
            clover_benches.append((rel_path, full_path))
    
    print(f"\nClover files in specs_from_artifacts: {len(clover_artifacts)}")
    for rel_path, _ in clover_artifacts[:10]:  # Show first 10
        print(f"  {rel_path}")
    if len(clover_artifacts) > 10:
        print(f"  ... and {len(clover_artifacts) - 10} more")
    
    print(f"\nClover files in specs_benches: {len(clover_benches)}")
    for rel_path, _ in clover_benches[:10]:  # Show first 10
        print(f"  {rel_path}")
    if len(clover_benches) > 10:
        print(f"  ... and {len(clover_benches) - 10} more")
    
    return clover_artifacts, clover_benches

def main():
    scripts_dir = Path(__file__).parent
    specs_benches = scripts_dir / "specs_benches"
    specs_from_artifacts = scripts_dir / "specs_from_artifacts"
    
    if not specs_benches.exists() or not specs_from_artifacts.exists():
        print("Error: One or both directories not found!")
        return
    
    print("Finding all Rust files...")
    benches_files = get_all_rust_files(specs_benches)
    artifacts_files = get_all_rust_files(specs_from_artifacts)
    
    print(f"Found {len(benches_files)} files in specs_benches")
    print(f"Found {len(artifacts_files)} files in specs_from_artifacts")
    
    # Check for Clover matches
    print("\n" + "="*60)
    print("CHECKING FOR CLOVER BENCHMARK MATCHES")
    print("="*60)
    clover_artifacts, clover_benches = check_clover_matches(benches_files, artifacts_files)
    
    # Find similar names
    print("\n" + "="*60)
    print("CHECKING FOR SIMILAR FILENAMES")
    print("="*60)
    similar_pairs = find_similar_names(benches_files, artifacts_files, threshold=0.2)
    
    if similar_pairs:
        print(f"\nFound {len(similar_pairs)} potentially similar file pairs:")
        for similarity, benches_rel, _, artifacts_rel, _ in similar_pairs[:20]:  # Show top 20
            print(f"  {similarity:.2f}: {benches_rel} <-> {artifacts_rel}")
        if len(similar_pairs) > 20:
            print(f"  ... and {len(similar_pairs) - 20} more")
    else:
        print("No files with similar names found.")

if __name__ == "__main__":
    main()
