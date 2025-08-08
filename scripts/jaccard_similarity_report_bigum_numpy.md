# File Similarity Analysis using Jaccard Similarity

**Total files analyzed**: 70
**Similarity threshold**: 50.0%
**Similar file pairs found**: 541
**Similarity clusters found**: 1

## Summary Statistics

- **Average similarity**: 60.0%
- **Max similarity**: 89.5%
- **Min similarity** (above threshold): 50.0%

## Similarity Distribution

| Range | Count | Percentage |
|-------|-------|------------|
| 85%-90% | 7 | 1.3% |
| 80%-85% | 8 | 1.5% |
| 75%-80% | 13 | 2.4% |
| 70%-75% | 47 | 8.7% |
| 65%-70% | 56 | 10.4% |
| 60%-65% | 103 | 19.0% |
| 55%-60% | 140 | 25.9% |
| 50%-55% | 167 | 30.9% |

## Top Similarity Clusters

### Cluster 1 (66 files, avg similarity: 40.6%)

- `numpy_specs/np_mod.rs`
- `numpy_specs/np_substract.rs`
- `numpy_specs/np_polyder.rs`
- `numpy_specs/np_broadcast.rs`
- `numpy_specs/np_power.rs`
- `numpy_specs/np_cum_sum.rs`
- `numpy_specs/np_floor_divide.rs`
- `numpy_specs/np_column_stack.rs`
- `numpy_specs/np_cum_prod.rs`
- `numpy_specs/np_bitwise_and.rs`
- ... and 56 more files


## Top 20 Most Similar File Pairs

| File 1 | File 2 | Similarity | Common Tokens |
|--------|--------|------------|---------------|
| `numpy_specs/np_copy.rs` | `numpy_specs/np_square.rs` | 89.5% | 17 |
| `numpy_specs/np_equal.rs` | `numpy_specs/np_not_equal.rs` | 88.9% | 24 |
| `numpy_specs/np_less_equal.rs` | `numpy_specs/np_greater_equal.rs` | 88.9% | 24 |
| `numpy_specs/np_greater_equal.rs` | `numpy_specs/np_not_equal.rs` | 88.9% | 24 |
| `bignum_specs/bn_spec_1_Add_atoms_2_11_40_41_46.rs` | `bignum_specs/bn_spec_2_AddAuxTop_atoms_11_31-35_40_46.rs` | 87.8% | 43 |
| `numpy_specs/np_equal.rs` | `numpy_specs/np_greater_equal.rs` | 85.7% | 24 |
| `numpy_specs/np_less_equal.rs` | `numpy_specs/np_not_equal.rs` | 85.2% | 23 |
| `numpy_specs/np_gcd.rs` | `numpy_specs/np_lcm.rs` | 84.6% | 22 |
| `bignum_specs/bn_spec_5_Bound_atoms_11_40.rs` | `bignum_specs/bn_spec_4_BitStringDecomposition_atoms_11_40_46.rs` | 82.9% | 29 |
| `bignum_specs/bn_spec_41_Str2IntLemma_atoms_11_40_46.rs` | `bignum_specs/bn_spec_4_BitStringDecomposition_atoms_11_40_46.rs` | 82.4% | 28 |
| `numpy_specs/np_equal.rs` | `numpy_specs/np_less_equal.rs` | 82.1% | 23 |
| `numpy_specs/np_column_stack.rs` | `numpy_specs/np_flatten.rs` | 81.8% | 18 |
| `numpy_specs/np_greater.rs` | `numpy_specs/np_floor_divide.rs` | 81.0% | 17 |
| `bignum_specs/bn_spec_41_Str2IntLemma_atoms_11_40_46.rs` | `bignum_specs/bn_spec_30_NormalizeBitString_atoms_11_40_41_46.rs` | 80.6% | 29 |
| `numpy_specs/np_mod.rs` | `numpy_specs/np_cum_prod.rs` | 80.0% | 16 |
| `numpy_specs/np_cum_sum.rs` | `numpy_specs/np_mod.rs` | 78.9% | 15 |
| `numpy_specs/np_cum_sum.rs` | `numpy_specs/np_cum_prod.rs` | 78.9% | 15 |
| `bignum_specs/bn_spec_1_Add_atoms_11_13_29_38_40_41_46_30.rs` | `bignum_specs/bn_spec_27_Mul_atoms_11_13_29_38_40_41_46_1_30.rs` | 78.8% | 41 |
| `bignum_specs/bn_spec_7_Compare_atoms_11_40_46.rs` | `bignum_specs/bn_spec_leftShift_atoms_11_31_40.rs` | 78.4% | 29 |
| `numpy_specs/np_right_shift.rs` | `numpy_specs/np_bitwise_and.rs` | 77.5% | 31 |

## Cross-Directory Similarities

**Cross-directory similar pairs**: 1

Top cross-directory similarities:

| File 1 | File 2 | Similarity |
|--------|--------|------------|
| `numpy_specs/np_power.rs` | `bignum_specs/bn_spec_leftShift_atoms_11_31_40.rs` | 50.0% |
