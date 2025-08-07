# Failed Verus Compilation Files

This directory contains 39 files that failed to compile with `verus --no-verify`.

## Failure Categories:

1. **Platform-specific imports**: Files using Windows-specific modules on Linux
2. **Missing return statements**: Functions with empty bodies or incorrect default values
3. **Syntax errors**: Return statements in wrong contexts
4. **Type resolution errors**: Missing or undefined types
5. **Complex return types**: Tuples, references, and custom types not handled correctly

## Files:
- verina_basic_79/verina_basic_79.rs
- verina_basic_16/verina_basic_16.rs
- verina_advanced_41/verina_advanced_41.rs
- verina_advanced_27/verina_advanced_27.rs
- verina_basic_45/verina_basic_45.rs
- verina_basic_81/verina_basic_81.rs
- verina_basic_76/verina_basic_76.rs
- verina_advanced_6/verina_advanced_6.rs
- verina_basic_104/verina_basic_104.rs
- verina_basic_59/verina_basic_59.rs
- verina_advanced_3/verina_advanced_3.rs
- verina_basic_31/verina_basic_31.rs
- verina_basic_91/verina_basic_91.rs
- verina_advanced_21/verina_advanced_21.rs
- verina_basic_92/verina_basic_92.rs
- verina_advanced_42/verina_advanced_42.rs
- verina_basic_90/verina_basic_90.rs
- verina_advanced_2/verina_advanced_2.rs
- verina_basic_17/verina_basic_17.rs
- verina_basic_6/verina_basic_6.rs
- verina_basic_24/verina_basic_24.rs
- verina_basic_102/verina_basic_102.rs
- verina_advanced_19/verina_advanced_19.rs
- verina_advanced_10/verina_advanced_10.rs
- verina_advanced_55/verina_advanced_55.rs
- verina_basic_5/verina_basic_5.rs
- verina_advanced_60/verina_advanced_60.rs
- verina_basic_108/verina_basic_108.rs
- verina_basic_25/verina_basic_25.rs
- verina_basic_80/verina_basic_80.rs
- verina_basic_96/verina_basic_96.rs
- verina_basic_93/verina_basic_93.rs
- verina_advanced_20/verina_advanced_20.rs
- verina_advanced_59/verina_advanced_59.rs
- verina_advanced_78/verina_advanced_78.rs
- verina_basic_84/verina_basic_84.rs
- verina_basic_70/verina_basic_70.rs
- verina_advanced_66/verina_advanced_66.rs
- verina_basic_78/verina_basic_78.rs

## Next Steps:

These files need manual review and fixing before they can be used for Verus proof synthesis.
The detailed error messages are available in `verus_compilation_failures.txt`.

Generated on: 39 files moved from benchmarks_no_bodies/
