# File Similarity Analysis using Cosine Similarity

**Total files analyzed**: 655
**Similarity threshold**: 50.0%
**Similar file pairs found**: 26938
**Similarity clusters found**: 3
**Pairs similar by Cosine but not Jaccard**: 19254

## Summary Statistics

- **Average cosine similarity**: 61.9%
- **Average Jaccard similarity** (for same pairs): 44.6%
- **Max cosine similarity**: 99.8%
- **Min cosine similarity** (above threshold): 50.0%

## Files Similar by Cosine but not Jaccard

These pairs have high token frequency similarity but different token sets:

| File 1 | File 2 | Cosine Sim | Jaccard Sim | Difference |
|--------|--------|------------|-------------|------------|
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_447.rs` | `autoverus/MBPP/verified/task_id_447.rs` | 95.9% | 44.4% | +51.5% |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_rand/verus_code.rs` | `artifacts/dafnybench/Dafny_tmp_tmpj88zq5zt_2-Kontrakte_max/verus_code.rs` | 91.3% | 45.2% | +46.2% |
| `HumanEval-RustBench/042-incr-list.rs` | `RustBench/ground_truth/remove_duplicates.rs` | 90.3% | 45.0% | +45.3% |
| `autoverus/Misc/verified/remove_all_greater.rs` | `RustBench/ground_truth/remove_duplicates.rs` | 90.3% | 44.4% | +45.8% |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_618.rs` | `autoverus/MBPP/verified/task_id_261.rs` | 89.6% | 47.5% | +42.1% |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_616.rs` | `autoverus/MBPP/verified/task_id_261.rs` | 89.6% | 47.5% | +42.1% |
| `autoverus/Misc/verified/bubble_v1.rs` | `RustBench/ground_truth/two_sum.rs` | 89.2% | 36.5% | +52.6% |
| `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSelSort/verus_code.rs` | `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session3Exercises_ExerciseMaximum/verus_code.rs` | 88.9% | 47.4% | +41.5% |
| `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session3Exercises_ExerciseMaximum/verus_code.rs` | `RustBench/preconditions_removed/max_dafny_lsp.rs` | 88.7% | 47.1% | +41.6% |
| `autoverus/Misc/verified/remove_all_greater_v2.rs` | `RustBench/ground_truth/array_concat.rs` | 88.7% | 47.4% | +41.3% |
| `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session3Exercises_ExerciseMaximum/verus_code.rs` | `RustBench/ground_truth/smallest_missing_number.rs` | 88.5% | 47.1% | +41.4% |
| `autoverus/Misc/verified/remove_all_greater_v2.rs` | `RustBench/ground_truth/array_copy.rs` | 88.4% | 47.4% | +41.0% |
| `HumanEval-RustBench/043-pairs-sum-to-zero.rs` | `autoverus/Misc/verified/bubble_v1.rs` | 88.3% | 38.5% | +49.8% |
| `autoverus/Misc/verified/bubble_v1.rs` | `RustBench/preconditions_removed/two_sum.rs` | 88.3% | 38.8% | +49.5% |
| `artifacts/dafnybench/CS494-final-project_tmp_tmp7nof55uq_bubblesort/verus_code.rs` | `artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session3Exercises_ExerciseMaximum/verus_code.rs` | 87.7% | 41.5% | +46.3% |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_8.rs` | `autoverus/MBPP/verified/task_id_447.rs` | 87.7% | 36.2% | +51.5% |
| `autoverus/Misc/unverified/remove_all_greater.rs` | `RustBench/ground_truth/remove_duplicates.rs` | 87.6% | 46.3% | +41.3% |
| `autoverus/Misc/verified/bubble_v2.rs` | `RustBench/ground_truth/two_sum.rs` | 87.5% | 35.2% | +52.3% |
| `autoverus/Misc/verified/remove_all_greater_v2.rs` | `RustBench/ground_truth/array_append.rs` | 87.2% | 47.5% | +39.7% |
| `HumanEval-RustBench/042-incr-list.rs` | `autoverus/Misc/verified/remove_all_greater.rs` | 87.2% | 48.6% | +38.5% |

... and 19234 more pairs

## Cosine Similarity Distribution

| Range | Count | Percentage |
|-------|-------|------------|
| 95%-100% | 168 | 0.6% |
| 90%-95% | 319 | 1.2% |
| 85%-90% | 536 | 2.0% |
| 80%-85% | 871 | 3.2% |
| 75%-80% | 1501 | 5.6% |
| 70%-75% | 2152 | 8.0% |
| 65%-70% | 2843 | 10.6% |
| 60%-65% | 4069 | 15.1% |
| 55%-60% | 5922 | 22.0% |
| 50%-55% | 8557 | 31.8% |

## Cosine vs Jaccard Comparison

Distribution of similarity differences (Cosine - Jaccard):

| Difference Range | Count | Interpretation |
|-----------------|-------|----------------|
| 0.5 to 1.0 | 40 | Cosine much higher |
| 0.3 to 0.5 | 3116 | Cosine significantly higher |
| 0.1 to 0.3 | 17303 | Cosine moderately higher |
| 0.0 to 0.1 | 4989 | Similar scores |
| -0.1 to 0.0 | 1261 | Jaccard slightly higher |
| -1.0 to -0.1 | 229 | Jaccard significantly higher |

## Top Similarity Clusters

### Cluster 1 (633 files, avg similarity: 32.6%)

- `autoverus/Diffy/unverified/res2o.rs`
- `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_normal_data_completion_MaxPerdV2/verus_code.rs`
- `autoverus/MBPP/verified/task_id_431.rs`
- `VerusProofSynthesisBench/MBPP/task_id_605.rs`
- `VerusProofSynthesisBench/MBPP/task_id_554.rs`
- `autoverus/MBPP/unverified/task_id_576.rs`
- `VerusProofSynthesisBench/MBPP/task_id_18.rs`
- `RustBench/ground_truth/binary_search.rs`
- `VerusProofSynthesisBench/MBPP_no_bodies/task_id_476.rs`
- `VerusProofSynthesisBench/MBPP_no_bodies/task_id_809.rs`
- ... and 623 more files

### Cluster 2 (2 files, avg similarity: 99.1%)

- `HumanEval-RustBench/056-correct_bracketing.rs`
- `HumanEval-RustBench/061-correct_bracketing.rs`

### Cluster 3 (2 files, avg similarity: 63.4%)

- `HumanEval-RustBench/001-separate-paren-groups.rs`
- `HumanEval-RustBench/030-get-positive.rs`


## Top 20 Most Similar File Pairs (by Cosine)

| File 1 | File 2 | Cosine Sim | Jaccard Sim | Token Info |
|--------|--------|------------|-------------|------------|
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_477.rs` | `VerusProofSynthesisBench/MBPP/task_id_477.rs` | 99.8% | 94.4% | 141/36 vs 140/34 |
| `autoverus/MBPP/unverified/task_id_769.rs` | `autoverus/MBPP/unverified/task_id_579.rs` | 99.8% | 93.9% | 127/32 vs 129/32 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_769.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_579.rs` | 99.8% | 94.1% | 94/33 vs 94/33 |
| `autoverus/MBPP/unverified/task_id_618.rs` | `autoverus/MBPP/unverified/task_id_616.rs` | 99.7% | 93.1% | 74/28 vs 74/28 |
| `autoverus/MBPP/unverified/task_id_728.rs` | `autoverus/MBPP/unverified/task_id_282.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_728.rs` | `autoverus/MBPP/unverified/task_id_445.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_282.rs` | `autoverus/MBPP/unverified/task_id_445.rs` | 99.7% | 92.9% | 69/27 vs 69/27 |
| `autoverus/MBPP/unverified/task_id_610.rs` | `autoverus/MBPP/unverified/task_id_586.rs` | 99.6% | 92.3% | 63/25 vs 63/25 |
| `autoverus/Diffy/verified/res2o.rs` | `autoverus/Diffy/verified/res2.rs` | 99.6% | 83.3% | 106/25 vs 112/30 |
| `RustBench/invariants_removed/integer_square_root.rs` | `RustBench/ground_truth/integer_square_root.rs` | 99.6% | 94.7% | 48/18 vs 52/19 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_618.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_616.rs` | 99.5% | 91.7% | 55/23 vs 55/23 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_576.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_69.rs` | 99.5% | 85.2% | 73/25 vs 73/25 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_728.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_445.rs` | 99.4% | 91.3% | 50/22 vs 50/22 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_728.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_273.rs` | 99.4% | 91.3% | 50/22 vs 50/22 |
| `VerusProofSynthesisBench/MBPP_no_bodies/task_id_445.rs` | `VerusProofSynthesisBench/MBPP_no_bodies/task_id_273.rs` | 99.4% | 91.3% | 50/22 vs 50/22 |
| `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_detailed_examples_SelectionSort/verus_code.rs` | `artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_solved_1_select/verus_code.rs` | 99.4% | 92.6% | 80/27 vs 75/25 |
| `RustBench/preconditions_removed/two_sum.rs` | `RustBench/ground_truth/two_sum.rs` | 99.4% | 90.0% | 98/27 vs 124/30 |
| `autoverus/MBPP/unverified/task_id_576.rs` | `autoverus/MBPP/unverified/task_id_69.rs` | 99.4% | 87.9% | 106/31 vs 106/31 |
| `VerusProofSynthesisBench/Misc/fib.rs` | `autoverus/Misc/verified/fib.rs` | 99.4% | 92.7% | 100/39 vs 100/40 |
| `autoverus/MBPP/unverified/task_id_476.rs` | `autoverus/MBPP/unverified/task_id_588.rs` | 99.3% | 90.5% | 123/40 vs 123/40 |
