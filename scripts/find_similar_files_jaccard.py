#!/usr/bin/env python3
"""
Script to find similar files in the benches directory using Jaccard similarity.
Jaccard similarity = |A ∩ B| / |A ∪ B| where A and B are sets of tokens from each file.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json
from typing import Set, Dict, List, Tuple
import argparse

def tokenize_file(file_path: Path) -> Set[str]:
    """
    Tokenize a file into a set of tokens.
    Removes comments and normalizes tokens for better comparison.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()
    
    # Remove single-line comments
    content = re.sub(r'//[^\n]*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Tokenize: split on non-alphanumeric characters
    # This captures identifiers, keywords, and numbers
    tokens = re.findall(r'\b\w+\b', content.lower())
    
    # Filter out very short tokens (likely not meaningful)
    tokens = [t for t in tokens if len(t) > 1]
    
    return set(tokens)

def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    """
    Calculate Jaccard similarity between two sets.
    Returns a value between 0 and 1, where 1 means identical sets.
    """
    if not set1 and not set2:
        return 1.0
    if not set1 or not set2:
        return 0.0
    
    intersection = set1 & set2
    union = set1 | set2
    
    return len(intersection) / len(union)

def find_rust_files(directory: Path) -> List[Path]:
    """Find all Rust files in the given directory."""
    return list(directory.rglob("*.rs"))

def analyze_file_similarity(directory: Path, threshold: float = 0.5) -> Dict:
    """
    Analyze similarity between all Rust files in the directory.
    Returns a dictionary with similarity information.
    """
    rust_files = find_rust_files(directory)
    print(f"Found {len(rust_files)} Rust files in {directory}")
    
    # Tokenize all files
    file_tokens = {}
    print("Tokenizing files...")
    for i, file_path in enumerate(rust_files):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(rust_files)} files...")
        file_tokens[file_path] = tokenize_file(file_path)
    
    # Calculate pairwise similarities
    similarities = []
    total_comparisons = len(rust_files) * (len(rust_files) - 1) // 2
    comparison_count = 0
    
    print(f"\nCalculating similarities ({total_comparisons} comparisons)...")
    for i, file1 in enumerate(rust_files):
        for j in range(i + 1, len(rust_files)):
            file2 = rust_files[j]
            
            similarity = jaccard_similarity(file_tokens[file1], file_tokens[file2])
            
            if similarity >= threshold:
                similarities.append({
                    'file1': str(file1.relative_to(directory)),
                    'file2': str(file2.relative_to(directory)),
                    'similarity': similarity,
                    'common_tokens': len(file_tokens[file1] & file_tokens[file2]),
                    'total_unique_tokens': len(file_tokens[file1] | file_tokens[file2])
                })
            
            comparison_count += 1
            if comparison_count % 10000 == 0:
                print(f"  Completed {comparison_count}/{total_comparisons} comparisons...")
    
    # Sort by similarity
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    
    # Group files by similarity clusters
    clusters = find_similarity_clusters(rust_files, file_tokens, threshold)
    
    return {
        'total_files': len(rust_files),
        'threshold': threshold,
        'similar_pairs': similarities,
        'clusters': clusters
    }

def find_similarity_clusters(files: List[Path], file_tokens: Dict[Path, Set[str]], threshold: float) -> List[Dict]:
    """
    Find clusters of similar files using a simple clustering approach.
    Files are in the same cluster if they have similarity >= threshold with at least one other file in the cluster.
    """
    # Build adjacency list
    adjacency = defaultdict(set)
    for i, file1 in enumerate(files):
        for j in range(i + 1, len(files)):
            file2 = files[j]
            if jaccard_similarity(file_tokens[file1], file_tokens[file2]) >= threshold:
                adjacency[file1].add(file2)
                adjacency[file2].add(file1)
    
    # Find connected components
    visited = set()
    clusters = []
    
    for file in files:
        if file not in visited:
            # BFS to find all connected files
            cluster = set()
            queue = [file]
            
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.add(current)
                    cluster.add(current)
                    queue.extend(adjacency[current] - visited)
            
            if len(cluster) > 1:  # Only keep clusters with more than one file
                clusters.append(cluster)
    
    # Convert clusters to list format with statistics
    cluster_list = []
    for i, cluster in enumerate(clusters):
        cluster_files = list(cluster)
        
        # Calculate average similarity within cluster
        total_sim = 0
        count = 0
        for j, file1 in enumerate(cluster_files):
            for k in range(j + 1, len(cluster_files)):
                file2 = cluster_files[k]
                total_sim += jaccard_similarity(file_tokens[file1], file_tokens[file2])
                count += 1
        
        avg_similarity = total_sim / count if count > 0 else 0
        
        cluster_list.append({
            'cluster_id': i + 1,
            'size': len(cluster),
            'average_similarity': avg_similarity,
            'files': [str(f.relative_to(files[0].parent.parent)) for f in cluster_files]
        })
    
    # Sort clusters by size and average similarity
    cluster_list.sort(key=lambda x: (x['size'], x['average_similarity']), reverse=True)
    
    return cluster_list

def generate_report(results: Dict, output_file: str = "jaccard_similarity_report.md"):
    """Generate a markdown report of the similarity analysis."""
    with open(output_file, 'w') as f:
        f.write("# File Similarity Analysis using Jaccard Similarity\n\n")
        f.write(f"**Total files analyzed**: {results['total_files']}\n")
        f.write(f"**Similarity threshold**: {results['threshold']:.1%}\n")
        f.write(f"**Similar file pairs found**: {len(results['similar_pairs'])}\n")
        f.write(f"**Similarity clusters found**: {len(results['clusters'])}\n\n")
        
        # Summary statistics
        if results['similar_pairs']:
            similarities = [p['similarity'] for p in results['similar_pairs']]
            f.write("## Summary Statistics\n\n")
            f.write(f"- **Average similarity**: {sum(similarities)/len(similarities):.1%}\n")
            f.write(f"- **Max similarity**: {max(similarities):.1%}\n")
            f.write(f"- **Min similarity** (above threshold): {min(similarities):.1%}\n\n")
        
        # Similarity distribution
        f.write("## Similarity Distribution\n\n")
        f.write("| Range | Count | Percentage |\n")
        f.write("|-------|-------|------------|\n")
        
        ranges = [(1.0, 0.95), (0.95, 0.90), (0.90, 0.85), (0.85, 0.80), 
                  (0.80, 0.75), (0.75, 0.70), (0.70, 0.65), (0.65, 0.60), 
                  (0.60, 0.55), (0.55, 0.50)]
        
        for high, low in ranges:
            count = sum(1 for p in results['similar_pairs'] if low <= p['similarity'] < high)
            if count > 0:
                percentage = count / len(results['similar_pairs']) * 100
                f.write(f"| {low:.0%}-{high:.0%} | {count} | {percentage:.1f}% |\n")
        
        # Top similarity clusters
        f.write("\n## Top Similarity Clusters\n\n")
        for i, cluster in enumerate(results['clusters'][:10]):  # Top 10 clusters
            f.write(f"### Cluster {cluster['cluster_id']} "
                   f"({cluster['size']} files, avg similarity: {cluster['average_similarity']:.1%})\n\n")
            for file in cluster['files'][:10]:  # Show up to 10 files per cluster
                f.write(f"- `{file}`\n")
            if len(cluster['files']) > 10:
                f.write(f"- ... and {len(cluster['files']) - 10} more files\n")
            f.write("\n")
        
        # Most similar file pairs
        f.write("\n## Top 20 Most Similar File Pairs\n\n")
        f.write("| File 1 | File 2 | Similarity | Common Tokens |\n")
        f.write("|--------|--------|------------|---------------|\n")
        
        for pair in results['similar_pairs'][:20]:
            f.write(f"| `{pair['file1']}` | `{pair['file2']}` | "
                   f"{pair['similarity']:.1%} | {pair['common_tokens']} |\n")
        
        # Cross-directory analysis
        f.write("\n## Cross-Directory Similarities\n\n")
        cross_dir_pairs = []
        for pair in results['similar_pairs']:
            dir1 = Path(pair['file1']).parts[0] if len(Path(pair['file1']).parts) > 0 else ''
            dir2 = Path(pair['file2']).parts[0] if len(Path(pair['file2']).parts) > 0 else ''
            if dir1 != dir2:
                cross_dir_pairs.append(pair)
        
        f.write(f"**Cross-directory similar pairs**: {len(cross_dir_pairs)}\n\n")
        if cross_dir_pairs:
            f.write("Top cross-directory similarities:\n\n")
            f.write("| File 1 | File 2 | Similarity |\n")
            f.write("|--------|--------|------------|\n")
            for pair in cross_dir_pairs[:10]:
                f.write(f"| `{pair['file1']}` | `{pair['file2']}` | {pair['similarity']:.1%} |\n")

def main():
    parser = argparse.ArgumentParser(description='Find similar files using Jaccard similarity')
    parser.add_argument('--directory', '-d', type=str, default='benches',
                        help='Directory to analyze (default: benches)')
    parser.add_argument('--threshold', '-t', type=float, default=0.5,
                        help='Similarity threshold (0.0-1.0, default: 0.5)')
    parser.add_argument('--output', '-o', type=str, default='jaccard_similarity_report.md',
                        help='Output report file (default: jaccard_similarity_report.md)')
    parser.add_argument('--json', '-j', type=str, help='Also save results as JSON')
    
    args = parser.parse_args()
    
    # Convert to Path object
    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return
    
    print(f"Analyzing files in '{directory}' with threshold {args.threshold:.1%}")
    
    # Run analysis
    results = analyze_file_similarity(directory, args.threshold)
    
    # Generate report
    print(f"\nGenerating report to '{args.output}'...")
    generate_report(results, args.output)
    
    # Save JSON if requested
    if args.json:
        print(f"Saving JSON results to '{args.json}'...")
        with open(args.json, 'w') as f:
            # Convert Path objects to strings for JSON serialization
            json_results = {
                'total_files': results['total_files'],
                'threshold': results['threshold'],
                'similar_pairs': results['similar_pairs'],
                'clusters': results['clusters']
            }
            json.dump(json_results, f, indent=2)
    
    print(f"\nAnalysis complete!")
    print(f"Found {len(results['similar_pairs'])} similar file pairs")
    print(f"Found {len(results['clusters'])} similarity clusters")
    print(f"Report saved to: {args.output}")

if __name__ == "__main__":
    main()
