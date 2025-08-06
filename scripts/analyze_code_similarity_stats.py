#!/usr/bin/env python3
"""
Generate detailed statistics about code similarity in the benches directory.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def analyze_similarity_report(json_file="function_similarity.json"):
    """Analyze the similarity report and generate detailed statistics."""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    groups = data['summary']['groups']
    
    # Statistics collectors
    stats = {
        'total_groups': len(groups),
        'total_functions_in_groups': 0,
        'group_size_distribution': defaultdict(int),
        'similarity_distribution': defaultdict(int),
        'directory_patterns': defaultdict(int),
        'file_patterns': defaultdict(set),
        'cross_directory_duplicates': [],
        'exact_duplicates': 0,
        'near_duplicates': 0,
    }
    
    # Analyze each group
    for group in groups:
        group_size = group['function_count']
        avg_similarity = group['average_similarity']
        
        stats['total_functions_in_groups'] += group_size
        stats['group_size_distribution'][group_size] += 1
        
        # Bucket similarity into ranges
        if avg_similarity == 1.0:
            stats['similarity_distribution']['100%'] += 1
            stats['exact_duplicates'] += group_size
        elif avg_similarity >= 0.95:
            stats['similarity_distribution']['95-99%'] += 1
            stats['near_duplicates'] += group_size
        elif avg_similarity >= 0.90:
            stats['similarity_distribution']['90-94%'] += 1
            stats['near_duplicates'] += group_size
        elif avg_similarity >= 0.85:
            stats['similarity_distribution']['85-89%'] += 1
            stats['near_duplicates'] += group_size
        elif avg_similarity >= 0.80:
            stats['similarity_distribution']['80-84%'] += 1
            stats['near_duplicates'] += group_size
        else:
            stats['similarity_distribution']['75-79%'] += 1
            stats['near_duplicates'] += group_size
        
        # Analyze directory patterns
        directories = set()
        for func in group['functions']:
            file_path = Path(func['file'])
            # Get the subdirectory under benches
            if len(file_path.parts) > 1:
                subdir = file_path.parts[1]
                directories.add(subdir)
                stats['directory_patterns'][subdir] += 1
                
                # Track which files have duplicates
                stats['file_patterns'][subdir].add(file_path.name)
        
        # Check for cross-directory duplicates
        if len(directories) > 1:
            stats['cross_directory_duplicates'].append({
                'group_id': group['group_id'],
                'directories': list(directories),
                'function_names': [f['name'] for f in group['functions']],
                'similarity': avg_similarity
            })
    
    return stats

def generate_detailed_report(stats, output_file="code_similarity_analysis.md"):
    """Generate a detailed markdown report of the similarity analysis."""
    
    with open(output_file, 'w') as f:
        f.write("# Cross-File Code Similarity Analysis for benches Directory\n\n")
        f.write("*Note: This analysis only considers similarities between functions in different files.*\n\n")
        
        # Overview
        f.write("## Overview\n\n")
        f.write(f"- **Total similar function groups found**: {stats['total_groups']}\n")
        f.write(f"- **Total functions in similar groups**: {stats['total_functions_in_groups']}\n")
        f.write(f"- **Functions with exact duplicates (100% similar)**: {stats['exact_duplicates']}\n")
        f.write(f"- **Functions with near duplicates (75-99% similar)**: {stats['near_duplicates']}\n\n")
        
        # Group size distribution
        f.write("## Group Size Distribution\n\n")
        f.write("| Group Size | Count | Description |\n")
        f.write("|------------|-------|-------------|\n")
        
        for size in sorted(stats['group_size_distribution'].keys()):
            count = stats['group_size_distribution'][size]
            if size == 2:
                desc = "Pairs of similar functions"
            elif size <= 5:
                desc = "Small groups"
            elif size <= 10:
                desc = "Medium groups"
            else:
                desc = "Large groups (potential systematic duplication)"
            f.write(f"| {size} functions | {count} groups | {desc} |\n")
        
        # Similarity distribution
        f.write("\n## Similarity Distribution\n\n")
        f.write("| Similarity Range | Group Count | Interpretation |\n")
        f.write("|------------------|-------------|----------------|\n")
        
        similarity_order = ['100%', '95-99%', '90-94%', '85-89%', '80-84%', '75-79%']
        interpretations = {
            '100%': "Exact duplicates (identical implementation)",
            '95-99%': "Near-identical (minor differences)",
            '90-94%': "Very similar (same algorithm, small variations)",
            '85-89%': "Similar (same approach, moderate variations)",
            '80-84%': "Somewhat similar (related implementations)",
            '75-79%': "Loosely similar (shared patterns)"
        }
        
        for range_key in similarity_order:
            if range_key in stats['similarity_distribution']:
                count = stats['similarity_distribution'][range_key]
                f.write(f"| {range_key} | {count} | {interpretations[range_key]} |\n")
        
        # Directory analysis
        f.write("\n## Directory Analysis\n\n")
        f.write("### Functions with Duplicates by Directory\n\n")
        f.write("| Directory | Duplicate Functions | Unique Files with Duplicates |\n")
        f.write("|-----------|--------------------|--------------------------|\n")
        
        for dir_name in sorted(stats['directory_patterns'].keys()):
            count = stats['directory_patterns'][dir_name]
            unique_files = len(stats['file_patterns'][dir_name])
            f.write(f"| {dir_name} | {count} | {unique_files} |\n")
        
        # Cross-directory duplicates
        f.write("\n### Cross-Directory Duplicates\n\n")
        if stats['cross_directory_duplicates']:
            f.write(f"Found **{len(stats['cross_directory_duplicates'])}** groups with functions duplicated across different directories:\n\n")
            
            for i, cross_dup in enumerate(stats['cross_directory_duplicates'][:10], 1):
                f.write(f"{i}. **Group {cross_dup['group_id']}** (Similarity: {cross_dup['similarity']:.1%})\n")
                f.write(f"   - Directories: {', '.join(cross_dup['directories'])}\n")
                f.write(f"   - Functions: {', '.join(cross_dup['function_names'][:5])}")
                if len(cross_dup['function_names']) > 5:
                    f.write(f" and {len(cross_dup['function_names'])-5} more")
                f.write("\n\n")
            
            if len(stats['cross_directory_duplicates']) > 10:
                f.write(f"... and {len(stats['cross_directory_duplicates'])-10} more cross-directory groups\n\n")
        else:
            f.write("No cross-directory duplicates found.\n\n")
        
        # Key findings
        f.write("## Key Findings\n\n")
        
        # Calculate percentages
        total_funcs = 2396  # From the previous analysis
        pct_with_dups = (stats['total_functions_in_groups'] / total_funcs) * 100
        pct_exact = (stats['exact_duplicates'] / total_funcs) * 100
        
        f.write(f"1. **{pct_with_dups:.1f}%** of all functions have at least one similar counterpart\n")
        f.write(f"2. **{pct_exact:.1f}%** of functions are exact duplicates of another function\n")
        
        # Find the largest group
        largest_size = max(stats['group_size_distribution'].keys())
        f.write(f"3. The largest group contains **{largest_size}** similar functions\n")
        
        # Most affected directory
        if stats['directory_patterns']:
            most_affected = max(stats['directory_patterns'].items(), key=lambda x: x[1])
            f.write(f"4. The directory with most duplicate functions is **{most_affected[0]}** with {most_affected[1]} functions\n")
        
        f.write("\n## Recommendations\n\n")
        f.write("1. **Review exact duplicates**: Functions with 100% similarity should be consolidated\n")
        f.write("2. **Examine large groups**: Groups with many similar functions may indicate systematic duplication\n")
        f.write("3. **Cross-directory analysis**: Functions duplicated across directories might be candidates for a shared library\n")
        f.write("4. **Template detection**: Large groups might indicate code generation or templating patterns\n")

def main():
    print("Analyzing code similarity statistics...")
    
    # Check if the JSON report exists
    if not os.path.exists("function_similarity.json"):
        print("Error: function_similarity.json not found. Run analyze_function_similarity.py first.")
        return
    
    stats = analyze_similarity_report()
    generate_detailed_report(stats)
    
    print("\nAnalysis complete! Generated: code_similarity_analysis.md")
    
    # Print summary
    print(f"\nSummary:")
    print(f"- Total similar groups: {stats['total_groups']}")
    print(f"- Functions in groups: {stats['total_functions_in_groups']}")
    print(f"- Cross-directory duplicates: {len(stats['cross_directory_duplicates'])} groups")

if __name__ == "__main__":
    main()
