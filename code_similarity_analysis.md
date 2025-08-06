# Code Similarity Analysis for benches Directory

## Overview

- **Total similar function groups found**: 157
- **Total functions in similar groups**: 829
- **Functions with exact duplicates (100% similar)**: 49
- **Functions with near duplicates (75-99% similar)**: 780

## Group Size Distribution

| Group Size | Count | Description |
|------------|-------|-------------|
| 2 functions | 63 groups | Pairs of similar functions |
| 3 functions | 29 groups | Small groups |
| 4 functions | 15 groups | Small groups |
| 5 functions | 8 groups | Small groups |
| 6 functions | 7 groups | Medium groups |
| 7 functions | 7 groups | Medium groups |
| 8 functions | 3 groups | Medium groups |
| 9 functions | 3 groups | Medium groups |
| 10 functions | 1 groups | Medium groups |
| 11 functions | 6 groups | Large groups (potential systematic duplication) |
| 12 functions | 3 groups | Large groups (potential systematic duplication) |
| 13 functions | 1 groups | Large groups (potential systematic duplication) |
| 15 functions | 2 groups | Large groups (potential systematic duplication) |
| 16 functions | 1 groups | Large groups (potential systematic duplication) |
| 18 functions | 2 groups | Large groups (potential systematic duplication) |
| 19 functions | 2 groups | Large groups (potential systematic duplication) |
| 20 functions | 1 groups | Large groups (potential systematic duplication) |
| 26 functions | 1 groups | Large groups (potential systematic duplication) |
| 38 functions | 1 groups | Large groups (potential systematic duplication) |
| 45 functions | 1 groups | Large groups (potential systematic duplication) |

## Similarity Distribution

| Similarity Range | Group Count | Interpretation |
|------------------|-------------|----------------|
| 100% | 6 | Exact duplicates (identical implementation) |
| 95-99% | 9 | Near-identical (minor differences) |
| 90-94% | 17 | Very similar (same algorithm, small variations) |
| 85-89% | 35 | Similar (same approach, moderate variations) |
| 80-84% | 46 | Somewhat similar (related implementations) |
| 75-79% | 44 | Loosely similar (shared patterns) |

## Directory Analysis

### Functions with Duplicates by Directory

| Directory | Duplicate Functions | Unique Files with Duplicates |
|-----------|--------------------|--------------------------|
| HumanEval-RustBench | 96 | 49 |
| RustBench | 47 | 21 |
| VerusProofSynthesisBench | 225 | 86 |
| artifacts | 240 | 1 |
| autoverus | 221 | 97 |

### Cross-Directory Duplicates

Found **66** groups with functions duplicated across different directories:

1. **Group 6** (Similarity: 100.0%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: sub_array_at_index, is_sub_list_at_index, is_sub_list_at_index

2. **Group 7** (Similarity: 99.1%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: difference, find_dissimilar, find_dissimilar

3. **Group 8** (Similarity: 98.8%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: max_rcur, min_rcur, min_rcur, min_rcur, min_rcur and 4 more

4. **Group 9** (Similarity: 98.6%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: is_sub_array, is_sub_list, is_sub_list

5. **Group 15** (Similarity: 95.0%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: prime_num, is_non_prime, is_non_prime

6. **Group 16** (Similarity: 94.7%)
   - Directories: HumanEval-RustBench, VerusProofSynthesisBench, autoverus
   - Functions: count, count_frequency_spec, count_frequency_rcr, count_frequency_rcr, count_frequency_rcr and 5 more

7. **Group 17** (Similarity: 94.6%)
   - Directories: HumanEval-RustBench, VerusProofSynthesisBench, autoverus
   - Functions: intersperse_spec, sum_to, sum_to, sum_to, sum_to and 4 more

8. **Group 18** (Similarity: 94.4%)
   - Directories: HumanEval-RustBench, VerusProofSynthesisBench, autoverus
   - Functions: count_uppercase_sum, special_filter_spec, count_uppercase_recursively, count_digits_recursively, count_boolean and 13 more

9. **Group 19** (Similarity: 93.9%)
   - Directories: HumanEval-RustBench, autoverus
   - Functions: is_vowel_spec, is_vowel, is_vowel, is_ascii_digit_spec, is_ascii_digit and 2 more

10. **Group 21** (Similarity: 93.5%)
   - Directories: VerusProofSynthesisBench, autoverus
   - Functions: remove_elements, remove_chars, remove_chars

... and 56 more cross-directory groups

## Key Findings

1. **34.6%** of all functions have at least one similar counterpart
2. **2.0%** of functions are exact duplicates of another function
3. The largest group contains **45** similar functions
4. The directory with most duplicate functions is **artifacts** with 240 functions

## Recommendations

1. **Review exact duplicates**: Functions with 100% similarity should be consolidated
2. **Examine large groups**: Groups with many similar functions may indicate systematic duplication
3. **Cross-directory analysis**: Functions duplicated across directories might be candidates for a shared library
4. **Template detection**: Large groups might indicate code generation or templating patterns
