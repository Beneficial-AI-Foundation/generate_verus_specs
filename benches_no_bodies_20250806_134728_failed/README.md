# Failed Verus Compilation Files

This directory contains 0 files that failed to compile with `verus --no-verify`.

## Failure Categories:

1. **Platform-specific imports**: Files using Windows-specific modules on Linux
2. **Missing return statements**: Functions with empty bodies or incorrect default values
3. **Syntax errors**: Return statements in wrong contexts
4. **Type resolution errors**: Missing or undefined types
5. **Complex return types**: Tuples, references, and custom types not handled correctly

## Files:

## Next Steps:

These files need manual review and fixing before they can be used for Verus proof synthesis.
The detailed error messages are available in `verus_compilation_failures.txt`.

Generated on: 0 files moved from benchmarks_no_bodies/
