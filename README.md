# Verus Benchmark Analysis & Generation Tools

A comprehensive toolkit for analyzing Verus verification benchmarks and generating specification-only benchmarks by processing existing Verus codebases. This project provides scripts to systemaGenerates comprehensive statistics by combining results from all similarity analysis tools.

**Usage:**
```bash
cd scripts
python3 analyze_code_similarity_stats.py
``` analyze code similarity, detect duplicates, remove function bodies while preserving specifications, and create datasets for verifica### Similarity Analysis Parameters

Fine-tune analysis with different thresholds:

```bash
cd scripts

# Conservative similarity (high precision)
python3 analyze_function_similarity_optimized.py ../benches 0.9 8

# Liberal similarity (high recall)
python3 analyze_function_similarity_optimized.py ../benches 0.7 8

# File-level analysis with different approaches
python3 find_similar_files_cosine.py --threshold 0.7 --json cosine_results.json
python3 find_similar_files_jaccard.py --threshold 0.5 --json jaccard_results.json
```
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

### Setup

1. **Configure Verus Path**: Create a `.env` file to set up your environment
   ```bash
   cp .env.example .env
   # Edit .env to set VERUS_PATH=/path/to/your/verus/executable
   ```

2. **Verify Configuration**: Test that everything is set up correctly
   ```bash
   cd scripts
   python3 verus_config.py --validate
   ```

### Important: Working Directory

**All scripts must be run from the `scripts` directory** due to internal dependencies and file path expectations:

```bash
cd scripts
python3 benchmark_pipeline.py /path/to/verus/source
```

This is required because:
- Scripts call other Python scripts without path prefixes
- Generated files (like `failed_files_list.txt`) are expected in the current directory
- The pipeline orchestrates multiple tools that depend on being in the scripts directory

### Analysis Tools

```bash
# Change to scripts directory first
cd scripts

# Analyze function similarity across files
python3 analyze_function_similarity_optimized.py ../benches 0.8 8

# Find duplicate files by content
python3 analyze_duplicates.py

# Find similar files using cosine similarity
python3 find_similar_files_cosine.py --directory ../benches --threshold 0.5

# Find similar files using Jaccard similarity
python3 find_similar_files_jaccard.py --directory ../benches --threshold 0.3

# Generate comprehensive similarity statistics
python3 analyze_code_similarity_stats.py
```

### Benchmark Generation

```bash
# Change to scripts directory first
cd scripts

# Run the complete pipeline (uses .env configuration)
python3 benchmark_pipeline.py /path/to/verus/source

# View current configuration
python3 benchmark_pipeline.py --config

# Override configuration with command-line options
python3 benchmark_pipeline.py ../benchmarks \
  --output ../benchmarks_processed \
  --verus-path /usr/local/bin/verus \
  --timeout 45
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
cd scripts
python3 analyze_function_similarity_optimized.py <directory> [threshold] [num_processes]
```

**Features:**
- Cross-file function comparison (ignores within-file similarities)
- Parallel processing for large codebases
- Token, structural, and line-based similarity metrics
- Detailed clustering of similar function groups

**Example:**
```bash
cd scripts
python3 analyze_function_similarity_optimized.py ../benches 0.8 8
```

### `analyze_duplicates.py` - Content-Based Duplicate Detection

Finds files with identical content using MD5 hashing and categorizes duplicate patterns.

**Usage:**
```bash
cd scripts
python3 analyze_duplicates.py
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
cd scripts
python3 find_similar_files_cosine.py --directory <dir> --threshold <threshold>
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
cd scripts
python3 find_similar_files_jaccard.py --directory <dir> --threshold <threshold>
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

**Important**: Must be run from the `scripts` directory:

**Usage:**
```bash
cd scripts
python3 benchmark_pipeline.py <source_directory> [options]
```

**Options:**
- `--output`: Output directory for processed files
- `--verus-path`: Path to Verus executable
- `--skip-move`: Don't move failed files to separate directory
- `--skip-summary`: Don't generate final summary report

**Example:**
```bash
cd scripts
python3 benchmark_pipeline.py ../my_verus_project \
  --output ../benchmarks \
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
cd scripts
python3 remove_function_bodies.py <input_directory> [output_directory]
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
cd scripts
python3 test_verus_compilation.py <directory> [verus_path]
```

### `move_failed_files.py` - Organization

Moves files that failed compilation to a separate directory for analysis.

**Usage:**
```bash
cd scripts
python3 move_failed_files.py <source_directory> [failed_directory]
```

### `project_summary.py` - Reporting

Generates comprehensive statistics about the processing results.

**Usage:**
```bash
cd scripts
python3 project_summary.py <source_dir> <working_dir> <failed_dir>
```

## Advanced Usage

### Comprehensive Analysis Workflow

For a complete analysis of your benchmark suite:

```bash
# Change to scripts directory first
cd scripts

# Step 1: Analyze function-level similarities
python3 analyze_function_similarity_optimized.py ../benches 0.8 8

# Step 2: Generate statistical analysis
python3 analyze_code_similarity_stats.py

# Step 3: Find file-level similarities (multiple approaches)
python3 find_similar_files_cosine.py --directory ../benches --threshold 0.5
python3 find_similar_files_jaccard.py --directory ../benches --threshold 0.3

# Step 4: Detect content-based duplicates
python3 analyze_duplicates.py

# Step 5: Generate removal plan (if needed)
python3 find_removable_duplicates.py
```

### Custom Processing Workflow

You can run individual benchmark generation scripts for more control:

```bash
# Change to scripts directory first
cd scripts

# Step 1: Remove function bodies
python3 remove_function_bodies.py ../source_files ../output_files

# Step 2: Test compilation
python3 test_verus_compilation.py ../output_files /path/to/verus

# Step 3: Organize failed files
python3 move_failed_files.py ../output_files ../output_files_failed

# Step 4: Generate summary
python3 project_summary.py ../source_files ../output_files ../output_files_failed
```

### Batch Processing Multiple Projects

```bash
#!/bin/bash
cd scripts  # Make sure we're in the scripts directory
for project in ../project1 ../project2 ../project3; do
    echo "Processing $project..."
    python3 benchmark_pipeline.py "$project" --output "${project}_specs"
    
    echo "Analyzing $project for similarities..."
    python3 analyze_function_similarity_optimized.py "${project}_specs"
done
```

### Similarity Analysis Parameters

Fine-tune analysis with different thresholds:

```bash
cd scripts

# Conservative similarity (high precision)
python3 analyze_function_similarity_optimized.py ../benches 0.9 8

# Liberal similarity (high recall)
python3 analyze_function_similarity_optimized.py ../benches 0.7 8

# File-level analysis with different approaches
python3 find_similar_files_cosine.py --threshold 0.7 --json cosine_results.json
python3 find_similar_files_jaccard.py --threshold 0.5 --json jaccard_results.json
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
    return 0;
}
```

## Configuration

### Environment-Based Configuration

The tools now support configuration through environment files (`.env`) for convenient setup:

#### 1. Create a Configuration File

Copy the example configuration file:
```bash
cp .env.example .env
```

#### 2. Edit Configuration

Edit `.env` to match your setup:
```bash
# Verus Configuration Environment Variables
VERUS_PATH=~/Downloads/verus-0.2025.07.15.62362b0-x86-linux/verus-x86-linux/./verus
VERUS_TIMEOUT=30
VERUS_RANDOM_TIMEOUT=60
VERUS_EXTRA_ARGS=
DEFAULT_OUTPUT_DIR=
SKIP_MOVE_FAILED=false
SKIP_SUMMARY=false
NO_TIMESTAMP=false
```

#### 3. Configuration Priority

Configuration is loaded in this order (highest to lowest priority):
1. Command line arguments (`--verus-path`, `--timeout`, etc.)
2. System environment variables (`VERUS_PATH`, etc.)
3. `.env.local` file (for local overrides, not tracked in git)
4. `.env` file (main configuration)
5. Built-in defaults

#### 4. View Current Configuration

```bash
cd scripts

# View configuration for any script
python3 benchmark_pipeline.py --config
python3 test_verus_compilation.py --config
python3 run_verus_random_file.py --config

# Test configuration directly
python3 verus_config.py --validate
```

### Configuration Options

| Option | Environment Variable | Default | Description |
|--------|---------------------|---------|-------------|
| Verus Path | `VERUS_PATH` | `~/Downloads/verus-...` | Path to Verus executable |
| Compilation Timeout | `VERUS_TIMEOUT` | 30 | Timeout per file (seconds) |
| Random Test Timeout | `VERUS_RANDOM_TIMEOUT` | 60 | Timeout for random testing (seconds) |
| Extra Arguments | `VERUS_EXTRA_ARGS` | *(empty)* | Additional Verus command line args |
| Default Output Dir | `DEFAULT_OUTPUT_DIR` | *(auto)* | Default output directory |
| Skip Move Failed | `SKIP_MOVE_FAILED` | false | Skip moving failed files |
| Skip Summary | `SKIP_SUMMARY` | false | Skip generating summary reports |
| No Timestamp | `NO_TIMESTAMP` | false | Skip timestamps in folder names |

### Legacy Configuration

You can still use command-line arguments to override any setting:

```bash
cd scripts

# Override Verus path
python3 benchmark_pipeline.py ../benchmarks --verus-path /custom/path/to/verus

# Override timeout
python3 test_verus_compilation.py ../benchmarks_no_bodies --timeout 60
```

### Debug Mode

For verbose output during processing:
```bash
cd scripts
python3 -u benchmark_pipeline.py ../source_dir 2>&1 | tee processing.log
```

For analysis debugging:
```bash
cd scripts
python3 -u analyze_function_similarity_optimized.py ../benches 0.8 4 2>&1 | tee analysis.log
```

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

