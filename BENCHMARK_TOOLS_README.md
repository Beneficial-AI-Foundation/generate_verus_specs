# Verus Benchmark Generation Tools

This directory contains a set of Python scripts for generating Verus benchmarks by removing function bodies from existing Verus files while preserving function signatures and specifications.

## Scripts Overview

### 1. `remove_function_bodies.py`
Removes function bodies from Verus files and inserts appropriate default return values.

**Usage:**
```bash
python3 remove_function_bodies.py <input_directory> [output_directory]
```

**Examples:**
```bash
# Process benchmarks directory, output to benchmarks_no_bodies
python3 remove_function_bodies.py benchmarks

# Process custom directory with custom output
python3 remove_function_bodies.py my_verus_files my_output_files
```

### 2. `test_verus_compilation.py`
Tests compilation of all processed files using `verus --no-verify` and generates reports.

**Usage:**
```bash
python3 test_verus_compilation.py <directory> [verus_path]
```

**Examples:**
```bash
# Test files in benchmarks_no_bodies with default Verus path
python3 test_verus_compilation.py benchmarks_no_bodies

# Test with custom Verus executable
python3 test_verus_compilation.py my_output_files /path/to/verus
```

**Generated files:**
- `verus_compilation_failures.txt` - Detailed error report
- `failed_files_list.txt` - Simple list of failed files

### 3. `move_failed_files.py`
Moves files that failed compilation to a separate directory for easier management.

**Usage:**
```bash
python3 move_failed_files.py <source_directory> [failed_directory]
```

**Examples:**
```bash
# Move failed files to default location
python3 move_failed_files.py benchmarks_no_bodies

# Move to custom failed directory
python3 move_failed_files.py my_output_files my_failed_files
```

### 4. `project_summary.py`
Generates a summary report of the entire benchmark generation process.

**Usage:**
```bash
python3 project_summary.py [source_dir] [working_dir] [failed_dir]
```

**Examples:**
```bash
# Default directories
python3 project_summary.py

# Custom directories
python3 project_summary.py my_source my_working my_failed
```

### 5. `benchmark_pipeline.py` (Complete Pipeline)
Orchestrates all the above scripts to provide a complete automated workflow.

**Usage:**
```bash
python3 benchmark_pipeline.py <source_directory> [options]
```

**Options:**
- `--output DIR` - Custom output directory
- `--verus-path PATH` - Path to Verus executable
- `--skip-move` - Don't move failed files
- `--skip-summary` - Don't generate summary

**Examples:**
```bash
# Complete pipeline with defaults
python3 benchmark_pipeline.py benchmarks

# Custom pipeline
python3 benchmark_pipeline.py my_verus_files --output my_benchmarks --verus-path /usr/local/bin/verus
```

## Workflow

### Manual Step-by-Step
1. **Generate benchmarks**: `python3 remove_function_bodies.py benchmarks`
2. **Test compilation**: `python3 test_verus_compilation.py benchmarks_no_bodies`
3. **Move failed files**: `python3 move_failed_files.py benchmarks_no_bodies`
4. **Generate summary**: `python3 project_summary.py`

### Automated Pipeline
```bash
python3 benchmark_pipeline.py benchmarks
```

## Output Structure

After running the complete pipeline, you'll have:

```
benchmarks_no_bodies/          # Working files (compile successfully)
benchmarks_no_bodies_failed/   # Failed files (need manual review)
verus_compilation_failures.txt # Detailed error report
failed_files_list.txt         # List of failed files
```

## Requirements

- Python 3.6+
- Verus executable (download from Verus releases)
- Original Verus source files

## Features

- **Smart return value generation**: Automatically generates appropriate default values based on return types
- **Comprehensive error reporting**: Detailed compilation failure analysis
- **Flexible directory handling**: Works with any source directory structure
- **Robust file processing**: Handles complex Verus syntax and edge cases
- **Complete automation**: Single command pipeline for the entire workflow

## Tips

1. **Custom Verus path**: Update the default Verus path in scripts or use command line arguments
2. **Large codebases**: The pipeline can handle hundreds of files efficiently
3. **Error analysis**: Check `verus_compilation_failures.txt` for detailed error information
4. **Manual fixes**: Files in the `_failed` directory may need manual review for complex return types

## Example Full Workflow

```bash
# 1. Clone or prepare your Verus source files
# 2. Run the complete pipeline
python3 benchmark_pipeline.py my_verus_source --output my_benchmarks

# 3. Use the generated benchmarks
# Working files are in: my_benchmarks/
# Failed files are in: my_benchmarks_failed/

# 4. Review the summary
cat project_summary_output.txt
```
