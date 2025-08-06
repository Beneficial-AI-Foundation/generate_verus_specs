#!/usr/bin/env python3
"""
Complete pipeline script for generating Verus benchmarks from any source directory.
This script orchestrates all the individual tools to provide a complete workflow.

Usage: python3 benchmark_pipeline.py <source_directory> [options]
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from verus_config import get_config

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with return code {e.returncode}")
        return False
    except Exception as e:
        print(f"❌ {description} failed with error: {e}")
        return False

def main():
    # Load configuration
    config = get_config()
    
    parser = argparse.ArgumentParser(
        description="Complete pipeline for generating Verus benchmarks from source files.",
        epilog="""
Examples:
  python3 benchmark_pipeline.py benchmarks
  python3 benchmark_pipeline.py my_verus_files --output my_output --verus-path /path/to/verus
  python3 benchmark_pipeline.py benchmarks --no-timestamp  # Skip timestamp in folder names
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("source_dir", nargs="?", help="Source directory containing Verus files")
    parser.add_argument("--output", 
                       default=config.get_string("DEFAULT_OUTPUT_DIR"),
                       help="Output directory for processed files (default: <source_dir>_no_bodies_<timestamp> or from config)")
    parser.add_argument("--verus-path", 
                       default=config.get_verus_path(),
                       help=f"Path to Verus executable (default: from config or {config.get_verus_path()})")
    parser.add_argument("--skip-move", 
                       action="store_true",
                       default=config.get_bool("SKIP_MOVE_FAILED"),
                       help="Skip moving failed files to separate directory")
    parser.add_argument("--skip-summary", 
                       action="store_true",
                       default=config.get_bool("SKIP_SUMMARY"),
                       help="Skip generating final summary")
    parser.add_argument("--no-timestamp", 
                       action="store_true",
                       default=config.get_bool("NO_TIMESTAMP"),
                       help="Skip adding timestamp to generated folder names")
    parser.add_argument("--config", help="Show current configuration and exit", action="store_true")
    
    args = parser.parse_args()
    
    # Show configuration if requested
    if args.config:
        config.print_config()
        return
    
    # Require source_dir if not just showing config
    if not args.source_dir:
        parser.error("source_dir is required (unless using --config)")
        return
    
    # Validate Verus path
    if not config.validate_verus_path(args.verus_path):
        sys.exit(1)
    
    # Generate timestamp if needed
    timestamp = "" if args.no_timestamp else f"_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    source_dir = Path(args.source_dir)
    if args.output:
        output_dir = Path(args.output)
    else:
        output_dir = Path(f"{args.source_dir}_no_bodies{timestamp}")
    
    failed_dir = Path(f"{output_dir}_failed")
    
    # Validate source directory
    if not source_dir.exists():
        print(f"❌ Error: Source directory '{source_dir}' not found!")
        sys.exit(1)
    
    # Count source files
    rust_files = list(source_dir.rglob("*.rs"))
    print(f"🎯 VERUS BENCHMARK PIPELINE")
    print("=" * 60)
    print(f"Source directory: {source_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Failed directory: {failed_dir}")
    print(f"Found {len(rust_files)} Rust files to process")
    print(f"Verus executable: {args.verus_path}")
    
    success = True
    
    # Step 1: Remove function bodies
    cmd = ["python3", "remove_function_bodies.py", str(source_dir), str(output_dir)]
    if not run_command(cmd, "Removing function bodies"):
        success = False
    
    # Step 2: Test compilation
    if success:
        cmd = ["python3", "test_verus_compilation.py", str(output_dir), args.verus_path]
        # Note: test_verus_compilation.py returns non-zero if there are failures,
        # but we still want to continue and move the failed files
        run_command(cmd, "Testing Verus compilation")
    
    # Step 3: Move failed files (if requested and if there are failures)
    if not args.skip_move and os.path.exists("failed_files_list.txt"):
        with open("failed_files_list.txt", 'r') as f:
            failed_files = [line.strip() for line in f if line.strip()]
        
        if failed_files:
            cmd = ["python3", "move_failed_files.py", str(output_dir), str(failed_dir)]
            if not run_command(cmd, "Moving failed files"):
                success = False
        else:
            print("\n✅ No failed files to move - all files compiled successfully!")
    
    # Step 4: Generate summary
    if not args.skip_summary:
        cmd = ["python3", "project_summary.py", str(source_dir), str(output_dir), str(failed_dir)]
        run_command(cmd, "Generating project summary")
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 PIPELINE COMPLETED SUCCESSFULLY!")
        print(f"\n📁 Results:")
        print(f"  Working files: {output_dir}")
        if os.path.exists(failed_dir):
            print(f"  Failed files:  {failed_dir}")
        print(f"\n📋 Generated files:")
        if os.path.exists("verus_compilation_failures.txt"):
            print(f"  - verus_compilation_failures.txt (detailed error report)")
        if os.path.exists("failed_files_list.txt"):
            print(f"  - failed_files_list.txt (list of failed files)")
        
        print(f"\n🚀 Next steps:")
        print(f"  1. Use files in '{output_dir}' for synthesis experiments")
        if os.path.exists(failed_dir):
            print(f"  2. Review files in '{failed_dir}' for manual fixes if needed")
    else:
        print("❌ PIPELINE FAILED - Check error messages above")
        sys.exit(1)

if __name__ == "__main__":
    main()
