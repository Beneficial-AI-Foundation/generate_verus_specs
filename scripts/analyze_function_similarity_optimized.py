#!/usr/bin/env python3
"""
Optimized script to find functions with different names but similar implementations across different files.
Uses hashing for initial filtering and parallel processing for better performance.
"""

import os
import sys
import re
import hashlib
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
import json
from typing import List, Tuple, Dict, Set
import multiprocessing as mp
from functools import partial

# Simple Rust function parser (regex-based for basic analysis)
RUST_FUNCTION_PATTERN = re.compile(
    r'(?:pub\s+)?(?:spec\s+)?(?:fn|proof\s+fn)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*'
    r'(?:<[^>]+>)?\s*\([^)]*\)\s*(?:->\s*[^{]+)?\s*{',
    re.MULTILINE | re.DOTALL
)

class FunctionInfo:
    def __init__(self, name, signature, body, file_path, start_line):
        self.name = name
        self.signature = signature
        self.body = body
        self.file_path = file_path
        self.start_line = start_line
        self.normalized_body = self.normalize_body(body)
        self.body_hash = self.compute_hash(self.normalized_body)
        self.signature_hash = self.compute_hash(self.normalize_signature(signature))
        
    def normalize_body(self, body):
        """Normalize function body by removing comments and normalizing whitespace."""
        # Remove single-line comments
        body = re.sub(r'//[^\n]*', '', body)
        # Remove multi-line comments
        body = re.sub(r'/\*.*?\*/', '', body, flags=re.DOTALL)
        # Normalize whitespace
        body = re.sub(r'\s+', ' ', body)
        # Remove leading/trailing whitespace
        body = body.strip()
        return body
    
    def normalize_signature(self, sig):
        """Normalize function signature."""
        # Remove function name from signature for comparison
        sig = re.sub(r'fn\s+[a-zA-Z_][a-zA-Z0-9_]*', 'fn FUNC', sig)
        # Normalize whitespace
        sig = re.sub(r'\s+', ' ', sig)
        return sig.strip()
    
    def compute_hash(self, text):
        """Compute hash of normalized text."""
        return hashlib.md5(text.encode()).hexdigest()

def extract_functions_from_file(file_path):
    """Extract all functions from a Rust/Verus file."""
    functions = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return functions
    
    # Find all function matches
    for match in RUST_FUNCTION_PATTERN.finditer(content):
        func_name = match.group(1)
        func_start = match.start()
        
        # Extract the full function body by finding matching braces
        brace_count = 1
        body_start = match.end() - 1  # Start from the opening brace
        i = match.end()
        
        while i < len(content) and brace_count > 0:
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
            i += 1
        
        if brace_count == 0:
            func_body = content[body_start:i]
            func_signature = content[func_start:body_start]
            start_line = content[:func_start].count('\n') + 1
            
            func_info = FunctionInfo(
                name=func_name,
                signature=func_signature,
                body=func_body,
                file_path=str(file_path),
                start_line=start_line
            )
            functions.append(func_info)
    
    return functions

def calculate_similarity(func1, func2):
    """Calculate similarity between two functions using normalized bodies."""
    # Quick check: if hashes match, they're identical (ignoring names)
    if func1.body_hash == func2.body_hash:
        return 1.0
    
    # Use SequenceMatcher on normalized bodies
    return SequenceMatcher(None, func1.normalized_body, func2.normalized_body).ratio()

def process_file_pair(args):
    """Process a pair of files for similarity comparison."""
    file1_funcs, file2_funcs, threshold = args
    similar_pairs = []
    
    for func1 in file1_funcs:
        for func2 in file2_funcs:
            # Skip if same function name
            if func1.name == func2.name:
                continue
            
            # Quick hash check for exact matches
            if func1.body_hash == func2.body_hash:
                similar_pairs.append((func1, func2, 1.0))
            else:
                # Calculate similarity
                similarity = calculate_similarity(func1, func2)
                if similarity >= threshold:
                    similar_pairs.append((func1, func2, similarity))
    
    return similar_pairs

def find_similar_functions_optimized(file_functions_map, threshold=0.8, num_processes=None):
    """Find similar functions across different files using parallel processing."""
    if num_processes is None:
        num_processes = mp.cpu_count()
    
    # Create list of file pairs to compare
    file_paths = list(file_functions_map.keys())
    file_pairs = []
    
    for i in range(len(file_paths)):
        for j in range(i + 1, len(file_paths)):
            file_pairs.append((
                file_functions_map[file_paths[i]],
                file_functions_map[file_paths[j]],
                threshold
            ))
    
    print(f"Comparing {len(file_pairs)} file pairs using {num_processes} processes...")
    
    # Process file pairs in parallel
    with mp.Pool(num_processes) as pool:
        results = pool.map(process_file_pair, file_pairs)
    
    # Collect all similar pairs
    all_similar_pairs = []
    for pairs in results:
        all_similar_pairs.extend(pairs)
    
    # Group similar functions
    print("Grouping similar functions...")
    similar_groups = group_similar_functions(all_similar_pairs)
    
    return similar_groups

def group_similar_functions(similar_pairs):
    """Group similar functions into clusters."""
    # Build adjacency list
    adjacency = defaultdict(list)
    similarity_map = {}
    
    for func1, func2, similarity in similar_pairs:
        key1 = (func1.file_path, func1.name, func1.start_line)
        key2 = (func2.file_path, func2.name, func2.start_line)
        
        adjacency[key1].append((key2, func2))
        adjacency[key2].append((key1, func1))
        
        similarity_map[(key1, key2)] = similarity
        similarity_map[(key2, key1)] = similarity
    
    # Find connected components
    visited = set()
    groups = []
    
    for start_key in adjacency:
        if start_key in visited:
            continue
        
        # BFS to find connected component
        group = []
        queue = [(start_key, None)]
        group_funcs = {}
        
        while queue:
            key, func = queue.pop(0)
            if key in visited:
                continue
            
            visited.add(key)
            
            # Get function object
            if func is None:
                # Find function from adjacency
                for _, f in adjacency[key]:
                    if (f.file_path, f.name, f.start_line) == key:
                        func = f
                        break
            
            if func and key not in group_funcs:
                group_funcs[key] = func
                group.append(func)
            
            # Add neighbors
            for neighbor_key, neighbor_func in adjacency[key]:
                if neighbor_key not in visited:
                    queue.append((neighbor_key, neighbor_func))
        
        if len(group) > 1:
            # Calculate average similarity for the group
            total_sim = 0
            count = 0
            
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    key1 = (group[i].file_path, group[i].name, group[i].start_line)
                    key2 = (group[j].file_path, group[j].name, group[j].start_line)
                    
                    sim = similarity_map.get((key1, key2), 0)
                    if sim > 0:
                        total_sim += sim
                        count += 1
            
            avg_similarity = total_sim / count if count > 0 else 0
            groups.append((group, avg_similarity))
    
    # Sort by average similarity
    groups.sort(key=lambda x: x[1], reverse=True)
    
    return groups

def analyze_directory(directory, threshold=0.8, num_processes=None):
    """Analyze all Rust files in a directory for similar functions."""
    file_functions_map = {}
    file_count = 0
    total_functions = 0
    
    print(f"Scanning directory: {directory}")
    
    for rust_file in Path(directory).rglob("*.rs"):
        functions = extract_functions_from_file(rust_file)
        if functions:
            file_functions_map[str(rust_file)] = functions
            total_functions += len(functions)
        file_count += 1
        
        if file_count % 50 == 0:
            print(f"  Processed {file_count} files, found {total_functions} functions...")
    
    print(f"\nTotal files processed: {file_count}")
    print(f"Total functions found: {total_functions}")
    print(f"Files with functions: {len(file_functions_map)}")
    
    if len(file_functions_map) < 2:
        print("Not enough files with functions to compare.")
        return [], []
    
    print("\nAnalyzing function similarity across files...")
    similar_groups = find_similar_functions_optimized(file_functions_map, threshold, num_processes)
    
    # Flatten all functions for reporting
    all_functions = []
    for funcs in file_functions_map.values():
        all_functions.extend(funcs)
    
    return similar_groups, all_functions

def generate_report(similar_groups, all_functions, output_file="function_similarity_report.md"):
    """Generate a detailed report of similar functions across different files."""
    with open(output_file, 'w') as f:
        f.write("# Cross-File Function Similarity Analysis Report\n\n")
        f.write("*Note: This analysis only considers similarities between functions in different files.*\n\n")
        f.write(f"Total functions analyzed: {len(all_functions)}\n")
        f.write(f"Similar function groups found (cross-file only): {len(similar_groups)}\n\n")
        
        # Summary statistics
        total_duplicates = sum(len(group[0]) for group in similar_groups)
        f.write(f"Total functions in similar groups: {total_duplicates}\n")
        f.write(f"Percentage of functions with cross-file similarities: {total_duplicates/len(all_functions)*100:.1f}%\n\n")
        
        # Detailed groups
        f.write("## Similar Function Groups\n\n")
        
        for i, (group, avg_similarity) in enumerate(similar_groups, 1):
            f.write(f"### Group {i} (Average Similarity: {avg_similarity:.2%})\n\n")
            f.write(f"Functions in this group ({len(group)} total):\n\n")
            
            for func in group:
                f.write(f"- **{func.name}** in `{func.file_path}` (line {func.start_line})\n")
            
            f.write("\n**Sample code from first function:**\n```rust\n")
            f.write(group[0].body[:500] + ("..." if len(group[0].body) > 500 else ""))
            f.write("\n```\n\n")
            
            # Show pairwise similarities
            if len(group) <= 5:  # Only show details for small groups
                f.write("**Pairwise similarities:**\n")
                for j in range(len(group)):
                    for k in range(j+1, len(group)):
                        sim = calculate_similarity(group[j], group[k])
                        f.write(f"- {group[j].name} vs {group[k].name}: {sim:.2%}\n")
                f.write("\n")
            
            f.write("---\n\n")

def generate_json_report(similar_groups, output_file="function_similarity.json"):
    """Generate a JSON report for programmatic processing."""
    report_data = {
        "summary": {
            "description": "Cross-file function similarity analysis",
            "total_groups": len(similar_groups),
            "groups": []
        }
    }
    
    for i, (group, avg_similarity) in enumerate(similar_groups):
        group_data = {
            "group_id": i + 1,
            "average_similarity": avg_similarity,
            "function_count": len(group),
            "functions": []
        }
        
        for func in group:
            func_data = {
                "name": func.name,
                "file": func.file_path,
                "line": func.start_line,
                "body_hash": func.body_hash,
                "body_length": len(func.normalized_body)
            }
            group_data["functions"].append(func_data)
        
        report_data["summary"]["groups"].append(group_data)
    
    with open(output_file, 'w') as f:
        json.dump(report_data, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_function_similarity_optimized.py <directory> [threshold] [num_processes]")
        print("Example: python analyze_function_similarity_optimized.py benches 0.8 4")
        sys.exit(1)
    
    directory = sys.argv[1]
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
    num_processes = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    print(f"Analyzing functions in '{directory}' with similarity threshold {threshold:.0%}")
    print("Note: Only comparing functions across different files, not within the same file.")
    print("=" * 60)
    
    similar_groups, all_functions = analyze_directory(directory, threshold, num_processes)
    
    print(f"\nFound {len(similar_groups)} groups of similar functions across different files")
    
    # Generate reports
    generate_report(similar_groups, all_functions)
    generate_json_report(similar_groups)
    
    print("\nReports generated:")
    print("  - function_similarity_report.md (human-readable)")
    print("  - function_similarity.json (machine-readable)")
    
    # Print summary
    if similar_groups:
        print("\nTop 5 most similar function groups:")
        for i, (group, avg_similarity) in enumerate(similar_groups[:5], 1):
            print(f"\n{i}. Average similarity: {avg_similarity:.2%}")
            print(f"   Functions: {', '.join(f.name for f in group[:3])}" + 
                  (f" and {len(group)-3} more" if len(group) > 3 else ""))

if __name__ == "__main__":
    main()
