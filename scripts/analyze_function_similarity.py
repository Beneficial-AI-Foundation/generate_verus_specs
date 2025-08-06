#!/usr/bin/env python3
"""
Script to find functions with different names but similar implementations in Rust/Verus code.
Uses AST-based analysis and various similarity metrics.
"""

import os
import sys
import re
import ast
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
import json
import hashlib
from typing import List, Tuple, Dict, Set

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
    
    def compute_hash(self, text):
        """Compute hash of normalized body for quick exact match detection."""
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

def tokenize_code(code):
    """Simple tokenization of code for similarity comparison."""
    # Remove string literals
    code = re.sub(r'"[^"]*"', 'STRING', code)
    code = re.sub(r"'[^']*'", 'CHAR', code)
    
    # Replace numbers with NUMBER token
    code = re.sub(r'\b\d+\b', 'NUMBER', code)
    
    # Extract identifiers and keywords
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b|[{}()\[\];,<>=!&|+\-*/]', code)
    
    return tokens

def calculate_token_similarity(func1, func2):
    """Calculate similarity based on token sequences."""
    tokens1 = tokenize_code(func1.normalized_body)
    tokens2 = tokenize_code(func2.normalized_body)
    
    if not tokens1 or not tokens2:
        return 0.0
    
    # Use SequenceMatcher for token-based similarity
    return SequenceMatcher(None, tokens1, tokens2).ratio()

def calculate_structural_similarity(func1, func2):
    """Calculate similarity based on code structure."""
    # Extract control flow keywords
    control_flow_pattern = r'\b(if|else|for|while|loop|match|return|break|continue)\b'
    
    cf1 = re.findall(control_flow_pattern, func1.normalized_body)
    cf2 = re.findall(control_flow_pattern, func2.normalized_body)
    
    if not cf1 and not cf2:
        return 1.0  # Both have no control flow
    elif not cf1 or not cf2:
        return 0.0  # One has control flow, other doesn't
    
    return SequenceMatcher(None, cf1, cf2).ratio()

def calculate_line_similarity(func1, func2):
    """Calculate similarity based on normalized lines."""
    lines1 = [line.strip() for line in func1.body.strip().split('\n') if line.strip()]
    lines2 = [line.strip() for line in func2.body.strip().split('\n') if line.strip()]
    
    if not lines1 or not lines2:
        return 0.0
    
    return SequenceMatcher(None, lines1, lines2).ratio()

def calculate_similarity(func1, func2):
    """Calculate overall similarity between two functions."""
    # Quick check: if hashes match, they're identical (ignoring names)
    if func1.body_hash == func2.body_hash:
        return 1.0
    
    # Calculate different similarity metrics
    token_sim = calculate_token_similarity(func1, func2)
    struct_sim = calculate_structural_similarity(func1, func2)
    line_sim = calculate_line_similarity(func1, func2)
    
    # Weighted average
    return (token_sim * 0.5 + struct_sim * 0.3 + line_sim * 0.2)

def find_similar_functions(functions, threshold=0.8):
    """Find groups of similar functions across different files only."""
    similar_groups = []
    processed = set()
    
    for i, func1 in enumerate(functions):
        if i in processed:
            continue
            
        group = [func1]
        processed.add(i)
        
        for j, func2 in enumerate(functions[i+1:], i+1):
            if j in processed:
                continue
                
            # Skip if from the same file
            if func1.file_path == func2.file_path:
                continue
                
            # Skip if same function name (likely overloaded or from different files)
            if func1.name == func2.name:
                continue
                
            similarity = calculate_similarity(func1, func2)
            
            if similarity >= threshold:
                group.append(func2)
                processed.add(j)
        
        if len(group) > 1:
            # Calculate average similarity for the group
            total_sim = 0
            count = 0
            for k in range(len(group)):
                for l in range(k+1, len(group)):
                    # Only calculate similarity between functions from different files
                    if group[k].file_path != group[l].file_path:
                        total_sim += calculate_similarity(group[k], group[l])
                        count += 1
            
            avg_similarity = total_sim / count if count > 0 else 0
            similar_groups.append((group, avg_similarity))
    
    # Sort by average similarity
    similar_groups.sort(key=lambda x: x[1], reverse=True)
    
    return similar_groups

def analyze_directory(directory, threshold=0.8):
    """Analyze all Rust files in a directory for similar functions."""
    all_functions = []
    file_count = 0
    
    print(f"Scanning directory: {directory}")
    
    for rust_file in Path(directory).rglob("*.rs"):
        functions = extract_functions_from_file(rust_file)
        all_functions.extend(functions)
        file_count += 1
        
        if file_count % 50 == 0:
            print(f"  Processed {file_count} files, found {len(all_functions)} functions...")
    
    print(f"\nTotal files processed: {file_count}")
    print(f"Total functions found: {len(all_functions)}")
    
    print("\nAnalyzing function similarity...")
    similar_groups = find_similar_functions(all_functions, threshold)
    
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
        f.write(f"Percentage of similar functions: {total_duplicates/len(all_functions)*100:.1f}%\n\n")
        
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
        print("Usage: python analyze_function_similarity.py <directory> [threshold]")
        print("Example: python analyze_function_similarity.py benches 0.8")
        sys.exit(1)
    
    directory = sys.argv[1]
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    print(f"Analyzing functions in '{directory}' with similarity threshold {threshold:.0%}")
    print("Note: Only comparing functions across different files, not within the same file.")
    print("=" * 60)
    
    similar_groups, all_functions = analyze_directory(directory, threshold)
    
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
