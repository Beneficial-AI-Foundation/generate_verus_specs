# Cross-File Function Similarity Analysis Update

## Changes Made

I've updated the function similarity analysis scripts to only compare functions across different files, not within the same file. This provides a more meaningful analysis of code duplication across your benchmark suite.

### 1. Updated Scripts

#### `analyze_function_similarity.py`
- Modified `find_similar_functions()` to skip comparisons between functions in the same file
- Added check: `if func1.file_path == func2.file_path: continue`
- Updated report headers to clarify "cross-file only" analysis
- Added notes in output to indicate the cross-file restriction

#### `analyze_code_similarity_stats.py`
- Updated report headers to reflect cross-file analysis
- Added clarification notes in the generated markdown

#### `analyze_function_similarity_optimized.py` (NEW)
- Created an optimized version using parallel processing
- Groups file comparisons to reduce redundant work
- Uses multiprocessing to compare file pairs in parallel
- Much faster for large datasets (470,935 file pairs in your case)

### 2. Key Differences in Results

#### Original Analysis (Within + Cross File)
- Found 157 groups of similar functions
- 829 functions (34.6%) had similarities
- Included many within-file duplicates (e.g., spec vs implementation functions)

#### Cross-File Only Analysis (HumanEval-RustBench subset)
- Found only 6 groups of similar functions
- 16 functions (5.0%) had cross-file similarities
- More focused on actual code duplication across different benchmarks

### 3. Performance Improvements

The optimized version includes:
- **Parallel processing**: Uses multiple CPU cores to compare file pairs
- **Hash-based filtering**: Quick exact match detection using MD5 hashes
- **Efficient grouping**: Uses BFS to find connected components
- **Progress tracking**: Shows real-time progress during analysis

### 4. Usage

```bash
# Regular version (slower but simpler)
python3 scripts/analyze_function_similarity.py <directory> [threshold]

# Optimized version (recommended for large directories)
python3 scripts/analyze_function_similarity_optimized.py <directory> [threshold] [num_processes]

# Example
python3 scripts/analyze_function_similarity_optimized.py benches 0.75 8
```

### 5. What This Reveals

The cross-file analysis is more useful for:
- Finding actual code duplication across different benchmark suites
- Identifying functions that could be moved to shared libraries
- Understanding which algorithms are reimplemented in multiple places
- Reducing maintenance burden by consolidating truly duplicate code

The much lower percentage of cross-file similarities (5% vs 34.6%) suggests that most "duplicates" were actually related functions within the same file (like test helpers, spec functions, etc.) rather than true cross-project duplication.
