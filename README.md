# Verus Benchmark Analysis & Generation Tools

A comprehensive toolkit for analyzing Verus verification benchmarks and generating specification-only benchmarks by processing existing Verus codebases. This project provides scripts to systematically analyze code similarity, detect duplicates, remove function bodies while preserving specifications, and create datasets for verification research.

## Overview

This repository contains a collection of Python scripts designed to analyze and transform Verus programs. The toolkit serves multiple purposes:

- **Code Analysis**: Comprehensive analysis of code similarity, duplicate detection, and benchmark organization
- **Verification Research**: Creating benchmarks for specification synthesis experiments
- **Benchmark Management**: Tools for organizing, deduplicating, and cleaning benchmark suites
- **Verus Development**: Testing specification completeness and consistency

## Features

### � Advanced Code Analysis
- **Function similarity detection**: Multi-threaded analysis using cosine and Jaccard similarity
- **Cross-file duplicate detection**: Identifies code duplication across different files and directories
- **Statistical reporting**: Comprehensive analysis with detailed markdown reports and JSON outputs
- **Similarity clustering**: Groups related functions and identifies patterns

### 📊 Comprehensive Benchmark Analysis
- **Content-based duplicate detection**: Finds identical files using MD5 hashing
- **Directory pattern analysis**: Categorizes duplicates by directory structure and patterns
- **Removal recommendations**: Intelligent suggestions for cleaning duplicate files
- **Cross-directory analysis**: Identifies functions duplicated across different benchmark suites

### �🔄 Complete Pipeline Automation
- **One-command processing**: Transform entire directories with a single script
- **Error handling**: Robust pipeline with comprehensive error reporting
- **Progress tracking**: Real-time feedback during processing
- **Batch processing**: Support for processing multiple projects

### 🔧 Intelligent Function Body Removal
- **Specification preservation**: Keeps `requires`, `ensures`, `invariant` clauses intact
- **Signature retention**: Maintains function names, parameters, and return types
- **Smart parsing**: Handles complex nested structures and edge cases
- **Automatic return value generation**: Creates appropriate stub implementations

### ✅ Compilation Verification
- **Automatic testing**: Validates generated specifications compile with Verus
- **Detailed reporting**: Comprehensive error logs for debugging
- **Success metrics**: Statistics on compilation success rates
- **Timeout protection**: Handles long-running compilation attempts

### � Detailed Reporting & Analytics
- **File organization**: Separates working and failed files automatically
- **Summary reports**: Detailed statistics and success metrics
- **Failure analysis**: Categorized error reporting for debugging
- **Multi-format outputs**: Both human-readable markdown and machine-readable JSON

## Quick Start

### Prerequisites

- Python 3.6 or higher
- Verus executable installed and accessible (for benchmark generation)
- Source directory with Verus (.rs) files

### Analysis Tools

```bash
# Analyze function similarity across files
python3 scripts/analyze_function_similarity_optimized.py benches 0.8 8

# Find duplicate files by content
python3 scripts/analyze_duplicates.py

# Find similar files using cosine similarity
python3 scripts/find_similar_files_cosine.py --directory benches --threshold 0.5

# Find similar files using Jaccard similarity
python3 scripts/find_similar_files_jaccard.py --directory benches --threshold 0.3

# Generate comprehensive similarity statistics
python3 scripts/analyze_code_similarity_stats.py
```

### Benchmark Generation

```bash
# Run the complete pipeline on a directory of Verus files
python3 scripts/benchmark_pipeline.py /path/to/verus/source

# With custom output directory and Verus path
python3 scripts/benchmark_pipeline.py benchmarks \
  --output benchmarks_processed \
  --verus-path /usr/local/bin/verus
```

### Output Structure

After running analysis tools, you'll have:

```
function_similarity_report.md       # Detailed similarity analysis
function_similarity.json           # Machine-readable results
code_similarity_analysis.md        # Statistical summary
cosine_similarity_report.md        # File-level similarity (cosine)
jaccard_similarity_report.md       # File-level similarity (Jaccard)
duplicate_analysis_report.md       # Content-based duplicate analysis
```

After running the benchmark pipeline, you'll have:

```
benchmarks_processed/           # Successfully processed files
benchmarks_processed_failed/    # Files that failed compilation
verus_compilation_failures.txt  # Detailed error report
failed_files_list.txt          # List of failed file paths
```

## Script Documentation

## Code Analysis Tools

### `analyze_function_similarity_optimized.py` - Function Similarity Analysis

Multi-threaded analysis to find similar functions across different files using token-based similarity.

**Usage:**
```bash
python3 scripts/analyze_function_similarity_optimized.py <directory> [threshold] [num_processes]
```

**Features:**
- Cross-file function comparison (ignores within-file similarities)
- Parallel processing for large codebases
- Token, structural, and line-based similarity metrics
- Detailed clustering of similar function groups

**Example:**
```bash
python3 scripts/analyze_function_similarity_optimized.py benches 0.8 8
```

### `analyze_duplicates.py` - Content-Based Duplicate Detection

Finds files with identical content using MD5 hashing and categorizes duplicate patterns.

**Usage:**
```bash
python3 scripts/analyze_duplicates.py
```

**Features:**
- Content-based duplicate detection across directory structures
- Pattern analysis (cross-directory, subdirectory duplicates)
- Removal recommendations for cleanup
- File size and content preview for verification

### `find_similar_files_cosine.py` - Cosine Similarity Analysis

File-level similarity analysis using cosine similarity on token frequency vectors.

**Usage:**
```bash
python3 scripts/find_similar_files_cosine.py --directory <dir> --threshold <threshold>
```

**Options:**
- `--directory`: Directory to analyze (default: benches)
- `--threshold`: Similarity threshold 0.0-1.0 (default: 0.5)
- `--output`: Output report file
- `--json`: Also save results as JSON

### `find_similar_files_jaccard.py` - Jaccard Similarity Analysis

File-level similarity analysis using Jaccard similarity on token sets.

**Usage:**
```bash
python3 scripts/find_similar_files_jaccard.py --directory <dir> --threshold <threshold>
```

**Features:**
- Token set-based similarity (different from cosine frequency-based)
- High/low threshold reporting options
- Cluster detection and analysis
- Comparative analysis with cosine results

### `analyze_code_similarity_stats.py` - Statistical Analysis

Generates comprehensive statistics from function similarity analysis results.

**Usage:**
```bash
python3 scripts/analyze_code_similarity_stats.py
```

**Features:**
- Detailed statistical breakdowns of similarity patterns
- Directory-wise analysis of duplicate distribution
- Cross-directory duplicate identification
- Recommendations for code cleanup

## Benchmark Generation Tools

### `benchmark_pipeline.py` - Main Pipeline

The complete orchestration script that runs all processing steps in sequence.

**Usage:**
```bash
python3 scripts/benchmark_pipeline.py <source_directory> [options]
```

**Options:**
- `--output`: Output directory for processed files
- `--verus-path`: Path to Verus executable
- `--skip-move`: Don't move failed files to separate directory
- `--skip-summary`: Don't generate final summary report

**Example:**
```bash
python3 scripts/benchmark_pipeline.py my_verus_project \
  --output benchmarks \
  --verus-path ~/tools/verus/verus
```

### `remove_function_bodies.py` - Core Processing

Removes function implementations while preserving specifications and signatures.

**Features:**
- Preserves `requires`, `ensures`, `invariant` clauses
- Maintains function signatures and return types
- Handles nested functions and complex structures
- Generates appropriate return statements for type consistency

**Usage:**
```bash
python3 scripts/remove_function_bodies.py <input_directory> [output_directory]
```

### `test_verus_compilation.py` - Verification

Tests all processed files for compilation using `verus --no-verify`.

**Features:**
- Batch compilation testing
- Timeout protection (30s per file)
- Detailed error capture and reporting
- Success rate statistics

**Usage:**
```bash
python3 scripts/test_verus_compilation.py <directory> [verus_path]
```

### `move_failed_files.py` - Organization

Moves files that failed compilation to a separate directory for analysis.

**Usage:**
```bash
python3 scripts/move_failed_files.py <source_directory> [failed_directory]
```

### `project_summary.py` - Reporting

Generates comprehensive statistics about the processing results.

**Usage:**
```bash
python3 scripts/project_summary.py <source_dir> <working_dir> <failed_dir>
```

## Advanced Usage

### Comprehensive Analysis Workflow

For a complete analysis of your benchmark suite:

```bash
# Step 1: Analyze function-level similarities
python3 scripts/analyze_function_similarity_optimized.py benches 0.8 8

# Step 2: Generate statistical analysis
python3 scripts/analyze_code_similarity_stats.py

# Step 3: Find file-level similarities (multiple approaches)
python3 scripts/find_similar_files_cosine.py --directory benches --threshold 0.5
python3 scripts/find_similar_files_jaccard.py --directory benches --threshold 0.3

# Step 4: Detect content-based duplicates
python3 scripts/analyze_duplicates.py

# Step 5: Generate removal plan (if needed)
python3 scripts/find_removable_duplicates.py
```

### Custom Processing Workflow

You can run individual benchmark generation scripts for more control:

```bash
# Step 1: Remove function bodies
python3 scripts/remove_function_bodies.py source_files output_files

# Step 2: Test compilation
python3 scripts/test_verus_compilation.py output_files /path/to/verus

# Step 3: Organize failed files
python3 scripts/move_failed_files.py output_files output_files_failed

# Step 4: Generate summary
python3 scripts/project_summary.py source_files output_files output_files_failed
```

### Batch Processing Multiple Projects

```bash
#!/bin/bash
for project in project1 project2 project3; do
    echo "Processing $project..."
    python3 scripts/benchmark_pipeline.py "$project" --output "${project}_specs"
    
    echo "Analyzing $project for similarities..."
    python3 scripts/analyze_function_similarity_optimized.py "${project}_specs"
done
```

### Similarity Analysis Parameters

Fine-tune analysis with different thresholds:

```bash
# Conservative similarity (high precision)
python3 scripts/analyze_function_similarity_optimized.py benches 0.9 8

# Liberal similarity (high recall)
python3 scripts/analyze_function_similarity_optimized.py benches 0.7 8

# File-level analysis with different thresholds
python3 scripts/find_similar_files_cosine.py --threshold 0.7 --json cosine_results.json
python3 scripts/find_similar_files_jaccard.py --threshold 0.5 --json jaccard_results.json
```

## Example Transformation

### Before (Original Verus Code)
```rust
fn factorial(n: u32) -> u32
    requires n <= 10
    ensures result == spec_factorial(n)
{
    if n <= 1 {
        1
    } else {
        n * factorial(n - 1)
    }
}
```

### After (Generated Specification)
```rust
fn factorial(n: u32) -> u32
    requires n <= 10
    ensures result == spec_factorial(n)
{
    arbitrary()
}
```

## Configuration

### Default Verus Path
The scripts use this default Verus path:
```
~/Downloads/verus-0.2025.07.15.62362b0-x86-linux/verus-x86-linux/./verus
```

Update the path using the `--verus-path` option or modify the default in the scripts.

### Timeout Settings
Compilation testing uses a 30-second timeout per file. Modify `timeout=30` in `test_verus_compilation.py` if needed.

## Troubleshooting

### Common Issues

1. **Verus executable not found**
   ```
   Error: Verus executable not found at /path/to/verus
   ```
   **Solution**: Use `--verus-path` to specify correct Verus location

2. **No .rs files found**
   ```
   No .rs files found in directory
   ```
   **Solution**: Ensure the source directory contains Rust/Verus files

3. **Permission errors**
   ```
   Permission denied when creating directories
   ```
   **Solution**: Ensure write permissions for output directories

4. **Analysis taking too long**
   ```
   Function similarity analysis running for hours
   ```
   **Solution**: Use the optimized version with parallel processing:
   ```bash
   python3 scripts/analyze_function_similarity_optimized.py benches 0.8 8
   ```

5. **Memory issues with large codebases**
   ```
   MemoryError or system slowdown during analysis
   ```
   **Solution**: 
   - Reduce the number of processes: `python3 script.py benches 0.8 2`
   - Increase similarity threshold to reduce comparisons: `0.85` instead of `0.8`
   - Process subdirectories separately

6. **Missing analysis dependencies**
   ```
   ImportError: No module named 'multiprocessing'
   ```
   **Solution**: Ensure Python 3.6+ is being used

### Debug Mode

For verbose output during processing:
```bash
python3 -u scripts/benchmark_pipeline.py source_dir 2>&1 | tee processing.log
```

For analysis debugging:
```bash
python3 -u scripts/analyze_function_similarity_optimized.py benches 0.8 4 2>&1 | tee analysis.log
```

### Performance Tips

1. **Use parallel processing**: Always specify the number of processes for large datasets
2. **Adjust thresholds**: Higher similarity thresholds (0.85-0.9) reduce computation time
3. **Target specific directories**: Analyze subdirectories separately for better control
4. **Monitor memory usage**: Use `htop` or `top` to monitor system resources during analysis

## Contributing

This toolkit is designed for research and development in Verus verification and benchmark analysis. Contributions welcome for:

### Analysis Tools
- Additional similarity metrics and algorithms
- Support for other programming languages beyond Rust/Verus
- Enhanced clustering and pattern detection
- Performance optimizations for large codebases

### Benchmark Generation
- Enhanced parsing for complex Verus constructs
- Additional specification preservation features
- Support for more Rust/Verus language features
- Better error handling and recovery

### General Improvements
- Extended reporting formats (HTML, CSV, etc.)
- Integration with CI/CD pipelines
- Visualization tools for similarity analysis
- Database storage for large-scale analysis results

## License

This project is provided as-is for research and educational purposes. Please respect any licensing terms of Verus and associated tools when using this toolkit.

## Project Structure

```
├── scripts/                           # All Python analysis and generation tools
│   ├── analyze_function_similarity_optimized.py  # Multi-threaded function similarity
│   ├── analyze_function_similarity.py            # Basic function similarity analysis  
│   ├── analyze_duplicates.py                     # Content-based duplicate detection
│   ├── analyze_code_similarity_stats.py          # Statistical analysis generator
│   ├── find_similar_files_cosine.py             # File similarity (cosine)
│   ├── find_similar_files_jaccard.py            # File similarity (Jaccard)
│   ├── find_removable_duplicates.py             # Duplicate removal planning
│   ├── benchmark_pipeline.py                     # Complete generation pipeline
│   ├── remove_function_bodies.py                # Core body removal logic
│   ├── test_verus_compilation.py                # Compilation verification
│   └── project_summary.py                       # Summary generation
├── benches/                           # Main benchmark directories
│   ├── autoverus/                     # Auto-generated Verus benchmarks
│   ├── HumanEval-RustBench/          # HumanEval Rust translations
│   ├── RustBench/                    # General Rust benchmarks
│   └── VerusProofSynthesisBench/     # Verus-specific synthesis benchmarks
├── *.md                              # Analysis reports and documentation
├── *.json                            # Machine-readable analysis results
├── cleanup_duplicates.sh             # Automated cleanup scripts
└── README.md                         # This file
```

## Analysis Reports Generated

The toolkit generates comprehensive reports in multiple formats:

- **Human-readable Markdown**: Detailed analysis with tables and summaries
- **JSON format**: Machine-readable results for further processing
- **CSV files**: Statistical data for spreadsheet analysis
- **Shell scripts**: Automated cleanup recommendations

## Related Projects

- [Verus](https://github.com/verus-lang/verus) - The Verus verification language
- [Rust](https://www.rust-lang.org/) - The Rust programming language
- [HumanEval](https://github.com/openai/human-eval) - Code generation benchmark
- [MBPP](https://github.com/google-research/google-research/tree/master/mbpp) - Python programming benchmark

---

*This toolkit was developed to support verification research, benchmark analysis, and Verus ecosystem development. The analysis tools are language-agnostic and can be adapted for other programming languages. For questions or contributions, please refer to the project's issue tracker.*
