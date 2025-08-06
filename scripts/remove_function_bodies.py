#!/usr/bin/env python3
"""
Script to create a benchmark by removing function bodies from Verus files.
Preserves function signatures, requires, ensures, and invariant clauses.

Usage: python3 remove_function_bodies.py <input_directory> [output_directory]
"""

import os
import re
import shutil
import sys
import argparse
from pathlib import Path

def find_function_start(lines, start_idx):
    """Find the start of a function definition."""
    for i in range(start_idx, len(lines)):
        line = lines[i].strip()
        if line.startswith('fn ') or line.startswith('pub fn '):
            return i
    return -1

def find_brace_balance(lines, start_idx):
    """Find the matching closing brace for an opening brace."""
    brace_count = 0
    found_opening = False
    
    for i in range(start_idx, len(lines)):
        line = lines[i]
        for char in line:
            if char == '{':
                brace_count += 1
                found_opening = True
            elif char == '}':
                brace_count -= 1
                if found_opening and brace_count == 0:
                    return i
    return -1

def extract_return_type(function_str):
    """Extract the return type from a function signature."""
    # Look for -> pattern
    arrow_match = re.search(r'->\s*([^{]+)', function_str)
    if arrow_match:
        return_part = arrow_match.group(1).strip()
        
        # Remove ensures and other clauses
        lines = return_part.split('\n')
        return_type_line = lines[0].strip()
        
        # Remove trailing comma if present
        if return_type_line.endswith(','):
            return_type_line = return_type_line[:-1].strip()
        
        # Handle parenthesized return types like (r: bool) or (result: bool)
        paren_match = re.match(r'\(\s*\w+\s*:\s*(.+)\s*\)', return_type_line)
        if paren_match:
            print(f"DEBUG: Found parenthesized return type: {paren_match.group(1)}")
            return paren_match.group(1).strip()
        
        print(f"DEBUG: Using raw return type: {return_type_line}")
        return return_type_line
    
    return None

def generate_default_value(return_type):
    """Generate an appropriate default value for a given return type."""
    if not return_type:
        return "// TODO: Remove this comment and implement the function body"
    
    # Clean up the return type string
    return_type = return_type.strip()
    
    # Handle common Verus/Rust types
    if return_type in ['bool']:
        return "return false;  // TODO: Remove this line and implement the function body"
    elif return_type in ['i32', 'i64', 'isize', 'u32', 'u64', 'usize', 'int', 'nat']:
        return "return 0;  // TODO: Remove this line and implement the function body" 
    elif return_type.startswith('Vec<') or return_type.endswith('Vec<T>'):
        return "return Vec::new();  // TODO: Remove this line and implement the function body"
    elif return_type == 'String':
        return "return String::new();  // TODO: Remove this line and implement the function body"
    elif return_type.startswith('Option<'):
        return "return None;  // TODO: Remove this line and implement the function body"
    elif return_type.startswith('Result<'):
        # For Result types, we'll use a generic error
        return "return Err(());  // TODO: Remove this line and implement the function body"
    elif return_type == '()':
        return "// TODO: Remove this comment and implement the function body"
    else:
        # For unknown types, try to determine a reasonable default or use assume(false)
        if 'bool' in return_type.lower():
            return "return false;  // TODO: Remove this line and implement the function body"
        elif any(num_type in return_type for num_type in ['i32', 'i64', 'u32', 'u64', 'usize', 'isize', 'int', 'nat']):
            return "return 0;  // TODO: Remove this line and implement the function body"
        else:
            # For completely unknown types, use assume(false) as a last resort
            return f"assume(false);  // TODO: Replace with appropriate return value of type {return_type}"

def remove_function_bodies(content):
    """Remove function bodies while preserving signatures and specifications."""
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this line starts a function
        if line.startswith('fn ') or line.startswith('pub fn '):
            # This is a function definition - we need to handle it specially
            func_start = i
            
            # Check if this is an empty function body like "fn main() {}"
            current_line = lines[i]
            if current_line.strip().endswith('{}'):
                # This is an empty function, keep it as is
                result_lines.append(lines[i])
                i += 1
                continue
            
            # Find the opening brace of the function body
            brace_line = -1
            j = i
            while j < len(lines):
                if '{' in lines[j]:
                    brace_line = j
                    break
                j += 1
            
            if brace_line == -1:
                # No opening brace found, just copy the line and continue
                result_lines.append(lines[i])
                i += 1
                continue
            
            # Check if opening and closing braces are on the same line (empty function)
            brace_pos = lines[brace_line].find('{')
            closing_pos = lines[brace_line].find('}', brace_pos)
            if closing_pos != -1:
                # Empty function body on same line, keep as is
                result_lines.append(lines[brace_line])
                i = brace_line + 1
                continue
            
            # Copy everything up to and including the opening brace
            for k in range(func_start, brace_line + 1):
                result_lines.append(lines[k])
            
            # Find the matching closing brace
            closing_brace = find_brace_balance(lines, brace_line)
            
            if closing_brace == -1:
                # No matching brace found, something's wrong
                result_lines.append(lines[i])
                i += 1
                continue
            
            # Extract return type and generate appropriate default value
            function_str = '\n'.join(lines[func_start:brace_line + 1])
            return_type = extract_return_type(function_str)
            default_value = generate_default_value(return_type)
            
            # Add the default return statement or comment
            if default_value.strip().startswith('//'):
                result_lines.append(f"    {default_value}")
            else:
                result_lines.append(f"    {default_value}")
            result_lines.append(lines[closing_brace])  # Add the closing brace
            
            # Skip to after the function
            i = closing_brace + 1
        else:
            # Not a function, just copy the line
            result_lines.append(lines[i])
            i += 1
    
    return '\n'.join(result_lines)

def process_rust_file(input_path, output_path):
    """Process a single Rust file to remove function bodies."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove function bodies
        modified_content = remove_function_bodies(content)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the modified content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print(f"Processed: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    """Main function to process all Rust files in specified directory."""
    parser = argparse.ArgumentParser(
        description="Remove function bodies from Verus files, preserving signatures and specifications.",
        epilog="Example: python3 remove_function_bodies.py benchmarks benchmarks_no_bodies"
    )
    parser.add_argument("input_dir", help="Input directory containing Verus files")
    parser.add_argument("output_dir", nargs="?", help="Output directory (default: <input_dir>_no_bodies)")
    
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        # Check if input directory already ends with "_no_bodies" to avoid infinite recursion
        input_dir_str = str(input_dir)
        if input_dir_str.endswith('_no_bodies'):
            # Remove the existing suffix to get the base name
            base_name = input_dir_str[:-len('_no_bodies')]
            output_dir = Path(f"{base_name}_no_bodies")
        else:
            output_dir = Path(f"{input_dir_str}_no_bodies")
    
    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' not found!")
        sys.exit(1)
    
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    # Remove existing output directory if it exists
    if output_dir.exists():
        shutil.rmtree(output_dir)
    
    # Create output directory
    output_dir.mkdir()
    
    # Process all .rs files recursively
    processed_count = 0
    for rust_file in input_dir.rglob("*.rs"):
        # Calculate relative path from input directory
        rel_path = rust_file.relative_to(input_dir)
        output_path = output_dir / rel_path
        
        process_rust_file(rust_file, output_path)
        processed_count += 1
    
    # Copy non-Rust files as well (like README.md, shell scripts, etc.)
    copied_count = 0
    for item in input_dir.rglob("*"):
        if item.is_file() and not item.name.endswith('.rs'):
            rel_path = item.relative_to(input_dir)
            output_path = output_dir / rel_path
            
            # Create directory if needed
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Copy the file
            shutil.copy2(item, output_path)
            print(f"Copied: {item} -> {output_path}")
            copied_count += 1
    
    print(f"\nBenchmark creation complete!")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Processed {processed_count} Rust files")
    print(f"Copied {copied_count} additional files")
    print("All function bodies have been replaced with appropriate default return values.")

if __name__ == "__main__":
    main()
