# File Similarity Analysis using Cosine Similarity

**Total files analyzed**: 578
**Similarity threshold**: 80.0%
**Similar file pairs found**: 1488
**Similarity clusters found**: 57
**Pairs similar by Cosine but not Jaccard**: 1234

## Summary Statistics

- **Average cosine similarity**: 86.8%
- **Average Jaccard similarity** (for same pairs): 64.1%
- **Max cosine similarity**: 99.8%
- **Min cosine similarity** (above threshold): 80.0%

## Files Similar by Cosine but not Jaccard

These pairs have high token frequency similarity but different token sets:

| File 1 | File 2 | Cosine Sim | Jaccard Sim | Difference |
|--------|--------|------------|-------------|------------|
| `autoverus/MBPP/verified/task_id_769.rs` | `autoverus/MBPP/verified/task_id_579.rs` | 99.2% | 78.6% | +20.6% |
| `RustBench/ground_truth/reverse.rs` | `RustBench/ground_truth/array_concat.rs` | 98.0% | 79.2% | +18.9% |
| `autoverus/MBPP/verified/task_id_618.rs` | `autoverus/MBPP/verified/task_id_616.rs` | 98.0% | 76.3% | +21.7% |
| `HumanEval-RustBench/043-pairs-sum-to-zero.rs` | `RustBench/ground_truth/two_sum.rs` | 97.9% | 79.4% | +18.5% |
| `autoverus/MBPP/verified/task_id_282.rs` | `autoverus/MBPP/verified/task_id_273.rs` | 97.9% | 67.4% | +30.5% |
| `autoverus/MBPP/unverified/task_id_447.rs` | `autoverus/MBPP/verified/task_id_447.rs` | 97.9% | 56.8% | +41.1% |
| `artifacts/dafnybench/Clover_binary_search/verus_code.rs` | `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_BinarySearch/verus_code.rs` | 97.8% | 76.7% | +21.1% |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_solved_1_select/verus_code.rs` | `artifacts/dafnybench/Clover_selectionsort/verus_code.rs` | 97.4% | 78.6% | +18.8% |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_06_n/verus_code.rs` | `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_error_data_completion_06_n/verus_code.rs` | 97.3% | 76.9% | +20.4% |
| `autoverus/MBPP/unverified/task_id_261.rs` | `autoverus/MBPP/verified/task_id_261.rs` | 96.9% | 75.0% | +21.9% |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_detailed_examples_SelectionSort/verus_code.rs` | `artifacts/dafnybench/Clover_selectionsort/verus_code.rs` | 96.8% | 73.3% | +23.4% |
| `RustBench/ground_truth/array_copy.rs` | `RustBench/ground_truth/reverse.rs` | 96.6% | 79.2% | +17.5% |
| `HumanEval-RustBench/043-pairs-sum-to-zero.rs` | `RustBench/preconditions_removed/two_sum.rs` | 96.4% | 70.6% | +25.8% |
| `autoverus/MBPP/unverified/task_id_282.rs` | `autoverus/MBPP/verified/task_id_282.rs` | 96.4% | 79.4% | +17.0% |
| `RustBench/ground_truth/reverse.rs` | `RustBench/ground_truth/array_append.rs` | 96.3% | 70.4% | +26.0% |
| `autoverus/MBPP/verified/task_id_261.rs` | `autoverus/MBPP/verified/task_id_616.rs` | 96.3% | 76.9% | +19.4% |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_15/verus_code.rs` | `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_15/verus_code.rs` | 96.2% | 75.0% | +21.2% |
| `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseReplace/verus_code.rs` | `RustBench/ground_truth/replace.rs` | 96.2% | 69.2% | +26.9% |
| `autoverus/MBPP/unverified/task_id_618.rs` | `autoverus/MBPP/verified/task_id_616.rs` | 96.2% | 79.4% | +16.8% |
| `autoverus/MBPP/verified/task_id_618.rs` | `autoverus/MBPP/verified/task_id_261.rs` | 96.1% | 70.7% | +25.4% |

... and 1214 more pairs

## Cosine Similarity Distribution

| Range | Count | Percentage |
|-------|-------|------------|
| 95%-100% | 140 | 9.4% |
| 90%-95% | 259 | 17.4% |
| 85%-90% | 400 | 26.9% |
| 80%-85% | 689 | 46.3% |

## Cosine vs Jaccard Comparison

Distribution of similarity differences (Cosine - Jaccard):

| Difference Range | Count | Interpretation |
|-----------------|-------|----------------|
| 0.5 to 1.0 | 9 | Cosine much higher |
| 0.3 to 0.5 | 440 | Cosine significantly higher |
| 0.1 to 0.3 | 786 | Cosine moderately higher |
| 0.0 to 0.1 | 230 | Similar scores |
| -0.1 to 0.0 | 23 | Jaccard slightly higher |

## Top Similarity Clusters

### Cluster 13 (102 files, avg similarity: 58.9%)

- `autoverus/MBPP/verified/task_id_426.rs`
- `autoverus/MBPP/verified/task_id_273.rs`
- `autoverus/MBPP/unverified/task_id_728.rs`
- `VerusProofSynthesisBench/MBPP/task_id_94.rs`
- `autoverus/MBPP/unverified/task_id_554.rs`
- `VerusProofSynthesisBench/MBPP/task_id_798.rs`
- `autoverus/MBPP/unverified/task_id_798.rs`
- `autoverus/MBPP/verified/task_id_307.rs`
- `autoverus/MBPP/unverified/task_id_426.rs`
- `autoverus/MBPP/verified/task_id_733.rs`
- ... and 92 more files

### Cluster 2 (95 files, avg similarity: 61.9%)

- `artifacts/dafnybench/Clover_find/verus_code.rs`
- `artifacts/dafnybench/Clover_slope_search/verus_code.rs`
- `RustBench/ground_truth/two_way_sort.rs`
- `RustBench/preconditions_removed/index_wise_addition.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_Minimum/verus_code.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_solved_1_select/verus_code.rs`
- `artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs`
- `VerusProofSynthesisBench/MBPP/task_id_457.rs`
- `artifacts/dafnybench/Clover_remove_front/verus_code.rs`
- `autoverus/MBPP/unverified/task_id_290.rs`
- ... and 85 more files

### Cluster 1 (21 files, avg similarity: 76.3%)

- `RustBench/ground_truth/string_xor.rs`
- `HumanEval-RustBench/011-string_xor.rs`
- `HumanEval-RustBench/042-incr-list.rs`
- `RustBench/ground_truth/unique.rs`
- `RustBench/ground_truth/array_concat.rs`
- `RustBench/invariants_removed/integer_square_root.rs`
- `RustBench/ground_truth/reverse.rs`
- `RustBench/ground_truth/abs.rs`
- `RustBench/ground_truth/replace_chars.rs`
- `RustBench/ground_truth/remove_element.rs`
- ... and 11 more files

### Cluster 29 (21 files, avg similarity: 76.3%)

- `VerusProofSynthesisBench/MBPP/task_id_602.rs`
- `autoverus/MBPP/unverified/task_id_557.rs`
- `VerusProofSynthesisBench/MBPP/task_id_557.rs`
- `autoverus/MBPP/verified/task_id_624.rs`
- `VerusProofSynthesisBench/MBPP/task_id_732.rs`
- `autoverus/MBPP/unverified/task_id_602.rs`
- `autoverus/MBPP/verified/task_id_557.rs`
- `autoverus/MBPP/verified/task_id_230.rs`
- `autoverus/MBPP/unverified/task_id_624.rs`
- `VerusProofSynthesisBench/MBPP/task_id_474.rs`
- ... and 11 more files

### Cluster 10 (15 files, avg similarity: 76.8%)

- `autoverus/Misc/verified/bubble_v1.rs`
- `artifacts/dafnybench/Dafny-Grind75_tmp_tmpsxfz3i4r_problems_twoSum/verus_code.rs`
- `artifacts/dafnybench/Clover_two_sum/verus_code.rs`
- `autoverus/Misc/verified/linearsearch.rs`
- `autoverus/Misc/verified/bubble_v2.rs`
- `RustBench/ground_truth/two_sum.rs`
- `RustBench/preconditions_removed/two_sum.rs`
- `autoverus/MBPP/unverified/task_id_447.rs`
- `autoverus/CloverBench/verified/two_sum.rs`
- `autoverus/MBPP/unverified/task_id_8.rs`
- ... and 5 more files

### Cluster 35 (11 files, avg similarity: 85.9%)

- `autoverus/MBPP/unverified/task_id_586.rs`
- `autoverus/MBPP/verified/task_id_743.rs`
- `autoverus/MBPP/verified/task_id_610.rs`
- `autoverus/MBPP/verified/task_id_644.rs`
- `autoverus/MBPP/unverified/task_id_610.rs`
- `VerusProofSynthesisBench/MBPP/task_id_743.rs`
- `autoverus/MBPP/verified/task_id_262.rs`
- `autoverus/MBPP/verified/task_id_586.rs`
- `VerusProofSynthesisBench/MBPP/task_id_610.rs`
- `autoverus/MBPP/unverified/task_id_743.rs`
- ... and 1 more files

### Cluster 37 (8 files, avg similarity: 82.3%)

- `autoverus/Diffy/unverified/res2o.rs`
- `autoverus/Misc/verified/cell_2_sum.rs`
- `autoverus/Misc/unverified/cell_2_sum.rs`
- `autoverus/Diffy/verified/res2.rs`
- `autoverus/Diffy/verified/s52if.rs`
- `autoverus/Diffy/verified/res2o.rs`
- `autoverus/Diffy/unverified/s52if.rs`
- `autoverus/Misc/verified/simple_nested.rs`

### Cluster 9 (7 files, avg similarity: 84.3%)

- `VerusProofSynthesisBench/MBPP/task_id_764.rs`
- `VerusProofSynthesisBench/MBPP/task_id_461.rs`
- `HumanEval-RustBench/066-digitSum.rs`
- `autoverus/MBPP/unverified/task_id_461.rs`
- `autoverus/MBPP/verified/task_id_461.rs`
- `autoverus/MBPP/unverified/task_id_764.rs`
- `autoverus/MBPP/verified/task_id_764.rs`

### Cluster 12 (7 files, avg similarity: 82.2%)

- `autoverus/CloverBench/verified/cal_div.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_Mult/verus_code.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_38/verus_code.rs`
- `artifacts/dafnybench/Clover_quotient/verus_code.rs`
- `artifacts/dafnybench/Clover_cal_sum/verus_code.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_41/verus_code.rs`
- `autoverus/CloverBench/unverified/cal_div.rs`

### Cluster 27 (6 files, avg similarity: 87.1%)

- `autoverus/MBPP/verified/task_id_605.rs`
- `autoverus/MBPP/verified/task_id_3.rs`
- `autoverus/MBPP/unverified/task_id_3.rs`
- `VerusProofSynthesisBench/MBPP/task_id_605.rs`
- `autoverus/MBPP/unverified/task_id_605.rs`
- `VerusProofSynthesisBench/MBPP/task_id_3.rs`


## Top 20 Most Similar File Pairs (by Cosine)

| File 1 | File 2 | Cosine Sim | Jaccard Sim | Token Info |
|--------|--------|------------|-------------|------------|
| `autoverus/MBPP/unverified/task_id_769.rs` | `autoverus/MBPP/unverified/task_id_579.rs` | 99.8% | 93.9% | 127/32 vs 129/32 |
| `autoverus/MBPP/unverified/task_id_618.rs` | `autoverus/MBPP/unverified/task_id_616.rs` | 99.7% | 93.1% | 74/28 vs 74/28 |
| `autoverus/MBPP/unverified/task_id_728.rs` | `autoverus/MBPP/unverified/task_id_282.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_728.rs` | `autoverus/MBPP/unverified/task_id_445.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_282.rs` | `autoverus/MBPP/unverified/task_id_445.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_610.rs` | `autoverus/MBPP/unverified/task_id_586.rs` | 99.6% | 92.3% | 63/25 vs 63/25 |
| `autoverus/Diffy/verified/res2o.rs` | `autoverus/Diffy/verified/res2.rs` | 99.6% | 83.3% | 106/25 vs 112/30 |
| `RustBench/invariants_removed/integer_square_root.rs` | `RustBench/ground_truth/integer_square_root.rs` | 99.6% | 94.7% | 48/18 vs 52/19 |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_detailed_examples_SelectionSort/verus_code.rs` | `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_solved_1_select/verus_code.rs` | 99.4% | 92.6% | 80/27 vs 75/25 |
| `RustBench/preconditions_removed/two_sum.rs` | `RustBench/ground_truth/two_sum.rs` | 99.4% | 90.0% | 98/27 vs 124/30 |
| `autoverus/MBPP/unverified/task_id_576.rs` | `autoverus/MBPP/unverified/task_id_69.rs` | 99.4% | 87.9% | 106/31 vs 106/31 |
| `VerusProofSynthesisBench/Misc/fib.rs` | `autoverus/Misc/verified/fib.rs` | 99.4% | 92.7% | 100/39 vs 100/40 |
| `autoverus/MBPP/unverified/task_id_476.rs` | `autoverus/MBPP/unverified/task_id_588.rs` | 99.3% | 90.5% | 123/40 vs 123/40 |
| `RustBench/preconditions_removed/barrier.rs` | `RustBench/ground_truth/barrier.rs` | 99.3% | 93.1% | 78/28 vs 81/28 |
| `VerusProofSynthesisBench/MBPP/task_id_572.rs` | `autoverus/MBPP/verified/task_id_572.rs` | 99.3% | 91.5% | 191/44 vs 201/46 |
| `autoverus/MBPP/verified/task_id_769.rs` | `autoverus/MBPP/verified/task_id_579.rs` | 99.2% | 78.6% | 294/50 vs 296/50 |
| `VerusProofSynthesisBench/MBPP/task_id_579.rs` | `autoverus/MBPP/verified/task_id_579.rs` | 99.1% | 84.0% | 270/42 vs 296/50 |
| `HumanEval-RustBench/056-correct_bracketing.rs` | `HumanEval-RustBench/061-correct_bracketing.rs` | 99.1% | 92.9% | 109/40 vs 117/41 |
| `VerusProofSynthesisBench/MBPP/task_id_755.rs` | `autoverus/MBPP/verified/task_id_755.rs` | 99.0% | 94.9% | 191/38 vs 201/38 |
| `VerusProofSynthesisBench/MBPP/task_id_579.rs` | `autoverus/MBPP/verified/task_id_769.rs` | 99.0% | 80.4% | 270/42 vs 294/50 |
