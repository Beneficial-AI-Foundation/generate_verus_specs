#!/usr/bin/env python3
"""
Script to find similar files in the benches directory using Cosine similarity.
Cosine similarity measures the cosine of the angle between two vectors in multi-dimensional space.
Unlike Jaccard, it considers token frequencies, not just presence/absence.
"""

import os
import re
from pathlib import Path
from collections import defaultdict, Counter
import json
from typing import Dict, List, Tuple
import argparse
import math

def tokenize_file(file_path: Path) -> Counter:
    """
    Tokenize a file into a Counter of token frequencies.
    Removes comments and normalizes tokens for better comparison.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return Counter()
    
    # Remove single-line comments
    content = re.sub(r'//[^\n]*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Tokenize: split on non-alphanumeric characters
    # This captures identifiers, keywords, and numbers
    tokens = re.findall(r'\b\w+\b', content.lower())
    
    # Filter out very short tokens (likely not meaningful)
    tokens = [t for t in tokens if len(t) > 1]
    
    return Counter(tokens)

def cosine_similarity(vec1: Counter, vec2: Counter) -> float:
    """
    Calculate cosine similarity between two token frequency vectors.
    Returns a value between 0 and 1, where 1 means identical vectors.
    """
    if not vec1 or not vec2:
        return 0.0
    
    # Get all unique tokens
    all_tokens = set(vec1.keys()) | set(vec2.keys())
    
    # Calculate dot product
    dot_product = sum(vec1[token] * vec2[token] for token in all_tokens)
    
    # Calculate magnitudes
    magnitude1 = math.sqrt(sum(count ** 2 for count in vec1.values()))
    magnitude2 = math.sqrt(sum(count ** 2 for count in vec2.values()))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    # Calculate cosine similarity
    return dot_product / (magnitude1 * magnitude2)

def jaccard_similarity(counter1: Counter, counter2: Counter) -> float:
    """
    Calculate Jaccard similarity for comparison.
    Uses sets derived from the counters.
    """
    if not counter1 and not counter2:
        return 1.0
    if not counter1 or not counter2:
        return 0.0
    
    set1 = set(counter1.keys())
    set2 = set(counter2.keys())
    
    intersection = set1 & set2
    union = set1 | set2
    
    return len(intersection) / len(union)

def find_rust_files(directory: Path) -> List[Path]:
    """Find all Rust files in the given directory."""
    return list(directory.rglob("*.rs"))

def analyze_file_similarity(directory: Path, threshold: float = 0.5) -> Dict:
    """
    Analyze similarity between all Rust files in the directory using cosine similarity.
    Also computes Jaccard similarity for comparison.
    Returns a dictionary with similarity information.
    """
    rust_files = find_rust_files(directory)
    print(f"Found {len(rust_files)} Rust files in {directory}")
    
    # Tokenize all files (get frequency counts)
    file_tokens = {}
    print("Tokenizing files...")
    for i, file_path in enumerate(rust_files):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(rust_files)} files...")
        file_tokens[file_path] = tokenize_file(file_path)
    
    # Calculate pairwise similarities
    similarities = []
    cosine_only_similar = []  # Pairs similar by cosine but not by Jaccard
    total_comparisons = len(rust_files) * (len(rust_files) - 1) // 2
    comparison_count = 0
    
    print(f"\nCalculating similarities ({total_comparisons} comparisons)...")
    for i, file1 in enumerate(rust_files):
        for j in range(i + 1, len(rust_files)):
            file2 = rust_files[j]
            
            cosine_sim = cosine_similarity(file_tokens[file1], file_tokens[file2])
            jaccard_sim = jaccard_similarity(file_tokens[file1], file_tokens[file2])
            
            if cosine_sim >= threshold:
                similarity_data = {
                    'file1': str(file1.relative_to(directory)),
                    'file2': str(file2.relative_to(directory)),
                    'cosine_similarity': cosine_sim,
                    'jaccard_similarity': jaccard_sim,
                    'similarity_difference': cosine_sim - jaccard_sim,
                    'total_tokens_file1': sum(file_tokens[file1].values()),
                    'total_tokens_file2': sum(file_tokens[file2].values()),
                    'unique_tokens_file1': len(file_tokens[file1]),
                    'unique_tokens_file2': len(file_tokens[file2])
                }
                similarities.append(similarity_data)
                
                # Track pairs where cosine finds similarity but Jaccard doesn't
                if cosine_sim >= threshold and jaccard_sim < threshold:
                    cosine_only_similar.append(similarity_data)
            
            comparison_count += 1
            if comparison_count % 10000 == 0:
                print(f"  Completed {comparison_count}/{total_comparisons} comparisons...")
    
    # Sort by cosine similarity
    similarities.sort(key=lambda x: x['cosine_similarity'], reverse=True)
    cosine_only_similar.sort(key=lambda x: x['cosine_similarity'], reverse=True)
    
    # Group files by similarity clusters
    clusters = find_similarity_clusters(rust_files, file_tokens, threshold)
    
    return {
        'total_files': len(rust_files),
        'threshold': threshold,
        'similar_pairs': similarities,
        'cosine_only_similar': cosine_only_similar,
        'clusters': clusters
    }

def find_similarity_clusters(files: List[Path], file_tokens: Dict[Path, Counter], threshold: float) -> List[Dict]:
    """
    Find clusters of similar files using cosine similarity.
    Files are in the same cluster if they have similarity >= threshold with at least one other file in the cluster.
    """
    # Build adjacency list
    adjacency = defaultdict(set)
    for i, file1 in enumerate(files):
        for j in range(i + 1, len(files)):
            file2 = files[j]
            if cosine_similarity(file_tokens[file1], file_tokens[file2]) >= threshold:
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
                total_sim += cosine_similarity(file_tokens[file1], file_tokens[file2])
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

def generate_report(results: Dict, output_file: str = "cosine_similarity_report.md"):
    """Generate a markdown report of the similarity analysis."""
    with open(output_file, 'w') as f:
        f.write("# File Similarity Analysis using Cosine Similarity\n\n")
        f.write(f"**Total files analyzed**: {results['total_files']}\n")
        f.write(f"**Similarity threshold**: {results['threshold']:.1%}\n")
        f.write(f"**Similar file pairs found**: {len(results['similar_pairs'])}\n")
        f.write(f"**Similarity clusters found**: {len(results['clusters'])}\n")
        f.write(f"**Pairs similar by Cosine but not Jaccard**: {len(results['cosine_only_similar'])}\n\n")
        
        # Summary statistics
        if results['similar_pairs']:
            cosine_sims = [p['cosine_similarity'] for p in results['similar_pairs']]
            jaccard_sims = [p['jaccard_similarity'] for p in results['similar_pairs']]
            f.write("## Summary Statistics\n\n")
            f.write(f"- **Average cosine similarity**: {sum(cosine_sims)/len(cosine_sims):.1%}\n")
            f.write(f"- **Average Jaccard similarity** (for same pairs): {sum(jaccard_sims)/len(jaccard_sims):.1%}\n")
            f.write(f"- **Max cosine similarity**: {max(cosine_sims):.1%}\n")
            f.write(f"- **Min cosine similarity** (above threshold): {min(cosine_sims):.1%}\n\n")
        
        # Files found by Cosine but not Jaccard
        if results['cosine_only_similar']:
            f.write("## Files Similar by Cosine but not Jaccard\n\n")
            f.write("These pairs have high token frequency similarity but different token sets:\n\n")
            f.write("| File 1 | File 2 | Cosine Sim | Jaccard Sim | Difference |\n")
            f.write("|--------|--------|------------|-------------|------------|\n")
            
            for pair in results['cosine_only_similar'][:20]:  # Top 20
                f.write(f"| `{pair['file1']}` | `{pair['file2']}` | "
                       f"{pair['cosine_similarity']:.1%} | {pair['jaccard_similarity']:.1%} | "
                       f"+{pair['similarity_difference']:.1%} |\n")
            
            if len(results['cosine_only_similar']) > 20:
                f.write(f"\n... and {len(results['cosine_only_similar']) - 20} more pairs\n")
        
        # Similarity distribution
        f.write("\n## Cosine Similarity Distribution\n\n")
        f.write("| Range | Count | Percentage |\n")
        f.write("|-------|-------|------------|\n")
        
        ranges = [(1.0, 0.95), (0.95, 0.90), (0.90, 0.85), (0.85, 0.80), 
                  (0.80, 0.75), (0.75, 0.70), (0.70, 0.65), (0.65, 0.60), 
                  (0.60, 0.55), (0.55, 0.50)]
        
        for high, low in ranges:
            count = sum(1 for p in results['similar_pairs'] if low <= p['cosine_similarity'] < high)
            if count > 0:
                percentage = count / len(results['similar_pairs']) * 100
                f.write(f"| {low:.0%}-{high:.0%} | {count} | {percentage:.1f}% |\n")
        
        # Comparison with Jaccard
        f.write("\n## Cosine vs Jaccard Comparison\n\n")
        f.write("Distribution of similarity differences (Cosine - Jaccard):\n\n")
        f.write("| Difference Range | Count | Interpretation |\n")
        f.write("|-----------------|-------|----------------|\n")
        
        diff_ranges = [(0.5, 1.0, "Cosine much higher"), 
                       (0.3, 0.5, "Cosine significantly higher"),
                       (0.1, 0.3, "Cosine moderately higher"),
                       (0.0, 0.1, "Similar scores"),
                       (-0.1, 0.0, "Jaccard slightly higher"),
                       (-1.0, -0.1, "Jaccard significantly higher")]
        
        for low, high, interpretation in diff_ranges:
            count = sum(1 for p in results['similar_pairs'] 
                       if low <= p['similarity_difference'] < high)
            if count > 0:
                f.write(f"| {low:.1f} to {high:.1f} | {count} | {interpretation} |\n")
        
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
        f.write("\n## Top 20 Most Similar File Pairs (by Cosine)\n\n")
        f.write("| File 1 | File 2 | Cosine Sim | Jaccard Sim | Token Info |\n")
        f.write("|--------|--------|------------|-------------|------------|\n")
        
        for pair in results['similar_pairs'][:20]:
            token_info = f"{pair['total_tokens_file1']}/{pair['unique_tokens_file1']} vs {pair['total_tokens_file2']}/{pair['unique_tokens_file2']}"
            f.write(f"| `{pair['file1']}` | `{pair['file2']}` | "
                   f"{pair['cosine_similarity']:.1%} | {pair['jaccard_similarity']:.1%} | "
                   f"{token_info} |\n")

def main():
    parser = argparse.ArgumentParser(description='Find similar files using Cosine similarity')
    parser.add_argument('--directory', '-d', type=str, default='benches',
                        help='Directory to analyze (default: benches)')
    parser.add_argument('--threshold', '-t', type=float, default=0.5,
                        help='Similarity threshold (0.0-1.0, default: 0.5)')
    parser.add_argument('--output', '-o', type=str, default='cosine_similarity_report.md',
                        help='Output report file (default: cosine_similarity_report.md)')
    parser.add_argument('--json', '-j', type=str, help='Also save results as JSON')
    
    args = parser.parse_args()
    
    # Convert to Path object
    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return
    
    print(f"Analyzing files in '{directory}' with cosine similarity threshold {args.threshold:.1%}")
    
    # Run analysis
    results = analyze_file_similarity(directory, args.threshold)
    
    # Generate report
    print(f"\nGenerating report to '{args.output}'...")
    generate_report(results, args.output)
    
    # Save JSON if requested
    if args.json:
        print(f"Saving JSON results to '{args.json}'...")
        # Convert Path objects to strings for JSON serialization
        json_results = {
            'total_files': results['total_files'],
            'threshold': results['threshold'],
            'similar_pairs': results['similar_pairs'],
            'cosine_only_similar': results['cosine_only_similar'],
            'clusters': results['clusters']
        }
        with open(args.json, 'w') as f:
            json.dump(json_results, f, indent=2)
    
    print(f"\nAnalysis complete!")
    print(f"Found {len(results['similar_pairs'])} similar file pairs")
    print(f"Found {len(results['cosine_only_similar'])} pairs similar by Cosine but not Jaccard")
    print(f"Found {len(results['clusters'])} similarity clusters")
    print(f"Report saved to: {args.output}")

if __name__ == "__main__":
    main()
