#!/usr/bin/env python3
"""
Summary script showing the final state of the Verus benchmark generation project.

Usage: python3 project_summary.py <source_directory> <working_directory> <failed_directory>
"""

import os
import sys
import argparse
from pathlib import Path

def count_files(directory):
    """Count .rs files in a directory recursively."""
    if not os.path.exists(directory):
        return 0
    
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len([f for f in files if f.endswith('.rs')])
    return count

def main():
    parser = argparse.ArgumentParser(
        description="Generate a summary report of the Verus benchmark generation project.",
        epilog="Example: python3 project_summary.py benchmarks benchmarks_no_bodies benchmarks_no_bodies_failed"
    )
    parser.add_argument("source_dir", nargs="?", default="benchmarks", help="Original source directory (default: benchmarks)")
    parser.add_argument("working_dir", nargs="?", default="benchmarks_no_bodies", help="Working directory (default: benchmarks_no_bodies)")
    parser.add_argument("failed_dir", nargs="?", default="benchmarks_no_bodies_failed", help="Failed files directory (default: benchmarks_no_bodies_failed)")
    
    args = parser.parse_args()
    
    print("🎯 VERUS BENCHMARK GENERATION - FINAL SUMMARY")
    print("=" * 60)
    
    # Count files in each directory
    original_count = count_files(args.source_dir)
    working_count = count_files(args.working_dir) 
    failed_count = count_files(args.failed_dir)
    
    print(f"📁 DIRECTORY BREAKDOWN:")
    print(f"  Original benchmarks ({args.source_dir}):      {original_count:3d} files")
    print(f"  Working benchmarks ({args.working_dir}):  {working_count:3d} files ✅")
    print(f"  Failed benchmarks ({args.failed_dir}):   {failed_count:3d} files ❌")
    print(f"  Total processed:                        {working_count + failed_count:3d} files")
    
    success_rate = (working_count / (working_count + failed_count)) * 100 if (working_count + failed_count) > 0 else 0
    
    print(f"\n📊 SUCCESS METRICS:")
    print(f"  Success rate:                           {success_rate:.1f}%")
    print(f"  Verus-compatible files:                 {working_count}")
    print(f"  Files needing manual fixes:             {failed_count}")
    
    print(f"\n🛠️  GENERATED TOOLS:")
    tools = [
        ("remove_function_bodies.py", "Removes function bodies and generates default returns"),
        ("test_verus_compilation.py", "Tests all files with verus --no-verify"), 
        ("move_failed_files.py", "Moves failed files to separate directory"),
        ("verus_compilation_failures.txt", "Detailed error report for failed files"),
        ("failed_files_list.txt", "Simple list of failed file names")
    ]
    
    for tool, description in tools:
        status = "✅" if os.path.exists(tool) else "❌"
        print(f"  {status} {tool:<30} - {description}")
    
    print(f"\n🎯 USAGE:")
    print(f"  • For synthesis: Use files in 'benchmarks_no_bodies/' (all compile with verus --no-verify)")
    print(f"  • For debugging: Check 'benchmarks_no_bodies_failed/' for problematic files")
    print(f"  • For errors: Review 'verus_compilation_failures.txt' for detailed error messages")
    
    print(f"\n✨ ACHIEVEMENT UNLOCKED:")
    print(f"  Successfully created {working_count} Verus-compatible benchmark files!")
    print(f"  Ready for proof synthesis and automated verification workflows! 🚀")

if __name__ == "__main__":
    main()
