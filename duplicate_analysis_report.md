# Duplicate Code Analysis: specs_from_artifacts vs specs_benches

## Summary

Based on the analysis performed on July 18, 2025, I found **NO exact duplicate files** between the `specs_from_artifacts` and `specs_benches` directories. However, there are **3 matching Clover benchmark functions** that implement the same algorithms with different specifications and type signatures.

## File Counts
- **specs_from_artifacts**: 84 Rust files
- **specs_benches**: 685 Rust files

## Clover Benchmark Matches

The analysis identified **3 pairs of related Clover benchmark files** that implement the same algorithms but with different specifications:

### 1. Binary Search
- **specs_from_artifacts**: `dafnybench/Clover_binary_search/verus_code.rs`
- **specs_benches**: 
  - `autoverus/CloverBench/unverified/binary_search.rs`
  - `autoverus/CloverBench/verified/binary_search.rs`

**Key Differences**:
- Artifacts version uses `&[int]` vs benches version uses `&Vec<u64>`
- Different specifications (artifacts finds insertion point, benches assumes element exists)

### 2. Array Append
- **specs_from_artifacts**: `dafnybench/Clover_array_append/verus_code.rs`
- **specs_benches**:
  - `autoverus/CloverBench/unverified/array_append_strong.rs`
  - `autoverus/CloverBench/verified/array_append_strong.rs`

**Key Differences**:
- Different parameter types (`int` vs `u64`)
- Different length constraints and postconditions

### 3. Linear Search 2
- **specs_from_artifacts**: `dafnybench/Clover_linear_search2/verus_code.rs`
- **specs_benches**:
  - `autoverus/CloverBench/unverified/linear_search2.rs`
  - `autoverus/CloverBench/verified/linear_search2.rs`

**Key Differences**:
- Parameter types (`&[int]` vs `&Vec<i32>`)
- Similar preconditions but different implementations

## Conclusion

**No duplicate code was found** between the directories. The files are related benchmarks for the same algorithms but represent different variations with:
- Different type signatures
- Different specifications
- Different verification requirements
- Different implementation approaches

These are **complementary benchmark sets** rather than duplicates.

## Additional Clover Functions

**specs_from_artifacts** contains 24 Clover functions including:
- avg, compare, selectionsort, find, even_list, triple, is_even, cal_sum, double_array_elements, and others

**specs_benches** contains 9 Clover functions including:
- array_sum_strong, array_product_strong, array_concat_strong, array_copy_strong, all_digits_strong, is_prime, and others

Most of these are unique to their respective directories.
