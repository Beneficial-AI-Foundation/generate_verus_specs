# Failed Verus Compilation Files

This directory contains 21 files that failed to compile with `verus --no-verify`.

## Failure Categories:

1. **Platform-specific imports**: Files using Windows-specific modules on Linux
2. **Missing return statements**: Functions with empty bodies or incorrect default values
3. **Syntax errors**: Return statements in wrong contexts
4. **Type resolution errors**: Missing or undefined types
5. **Complex return types**: Tuples, references, and custom types not handled correctly

## Files:
- numpy_specs/np_arange.rs
- numpy_specs/np_clip.rs
- numpy_specs/np_transpose.rs
- numpy_specs/np_sign.rs
- numpy_specs/np_abs.rs
- numpy_specs/np_piecewise.rs
- numpy_specs/np_zeros.rs
- numpy_specs/np_intersect.rs
- numpy_specs/np_broadcast.rs
- numpy_specs/np_diagonal.rs
- numpy_specs/np_center.rs
- numpy_specs/np_select.rs
- numpy_specs/np_where.rs
- numpy_specs/np_reshape.rs
- numpy_specs/np_bitwise_xor.rs
- numpy_specs/np_shape.rs
- bignum_specs/bn_spec_leftShift_atoms_11_31_40.rs
- bignum_specs/bn_spec_1_Add_atoms_11_13_29_38_40_41_46_30.rs
- bignum_specs/bn_spec_27_Mul_atoms_1_11_31_13_30_40_leftShift.rs
- bignum_specs/bn_spec_27_Mul_atoms_11_40_41_46.rs
- bignum_specs/bn_spec_27_Mul_atoms_11_13_29_38_40_41_46_1_30.rs

## Next Steps:

These files need manual review and fixing before they can be used for Verus proof synthesis.
The detailed error messages are available in `verus_compilation_failures.txt`.

Generated on: 21 files moved from benchmarks_no_bodies/
