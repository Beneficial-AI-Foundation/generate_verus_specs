#!/usr/bin/env python3
"""
Verus configuration loader that reads settings from environment files.

This module provides utilities for loading Verus configuration from .env files,
with fallbacks to command-line arguments and built-in defaults.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import Optional, Dict, Any, List


class VerusConfig:
    """Configuration loader for Verus tools."""
    
    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize the configuration loader.
        
        Args:
            env_file: Path to the environment file. If None, looks for .env, .env.local 
                     in the project root directory.
        """
        self.config = {}
        self.project_root = Path(__file__).parent.parent
        self._cached_auto_verus_path = None  # Cache for automatic search results
        
        # Load configuration from environment files
        self._load_env_files(env_file)
        
    def _load_env_files(self, env_file: Optional[str] = None):
        """Load configuration from environment files."""
        if env_file:
            env_files = [Path(env_file)]
        else:
            # Look for .env files in order of preference
            env_files = [
                self.project_root / ".env.local",  # Local overrides (not in git)
                self.project_root / ".env",        # Main config file
            ]
        
        for env_path in env_files:
            if env_path.exists():
                self._load_env_file(env_path)
                print(f"Loaded configuration from: {env_path}")
                break
        else:
            print("No .env file found. Using system environment variables and defaults.")
    
    def _load_env_file(self, env_path: Path):
        """Load variables from a single .env file."""
        try:
            with open(env_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse key=value pairs
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Remove quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        
                        self.config[key] = value
                    else:
                        print(f"Warning: Invalid line in {env_path}:{line_num}: {line}")
        except Exception as e:
            print(f"Warning: Could not load {env_path}: {e}")
    
    def _search_for_verus(self) -> Optional[str]:
        """
        Search for Verus executable in common installation locations.
        
        Returns:
            Path to Verus executable if found, None otherwise
        """
        # 1. Check if 'verus' is in PATH
        verus_in_path = shutil.which('verus')
        if verus_in_path:
            return verus_in_path
        
        # 2. Common installation directories to search
        search_dirs = [
            Path.home() / "Downloads",
            Path.home() / "tools",
            Path.home() / "bin", 
            Path.home() / ".local" / "bin",
            Path("/usr/local/bin"),
            Path("/opt"),
            Path("/usr/bin"),
            Path.home() / "verus",
            Path.home() / ".cargo" / "bin",  # Rust/Cargo installations
        ]
        
        # 3. Look for Verus executable patterns
        verus_patterns = [
            "verus",
            "verus-*",
            "**/verus",
            "**/verus-**/verus",
            "**/verus-**/verus-*",
            "**/verus-*/bin/verus",
        ]
        
        found_candidates = []
        
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue
                
            for pattern in verus_patterns:
                try:
                    # Use glob to find matching files
                    matches = list(search_dir.glob(pattern))
                    for match in matches:
                        if match.is_file() and os.access(match, os.X_OK):
                            match_str = str(match)
                            # Verify it's actually Verus by running --version
                            if self._verify_verus_executable(match) and match_str not in found_candidates:
                                found_candidates.append(match_str)
                except Exception:
                    # Skip directories we can't access
                    continue
        
        if found_candidates:
            # Return the first valid candidate
            # Could be enhanced to prefer certain paths or show multiple options
            return found_candidates[0]
        
        return None
    
    def _verify_verus_executable(self, path: Path) -> bool:
        """
        Verify that a file is actually a Verus executable.
        
        Args:
            path: Path to the potential Verus executable
            
        Returns:
            True if it's a valid Verus executable
        """
        try:
            # Try running verus --version with a short timeout
            result = subprocess.run(
                [str(path), "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            # Check if the output contains "verus" (case insensitive)
            return result.returncode == 0 and "verus" in result.stdout.lower()
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def get_verus_path(self, default: Optional[str] = None) -> str:
        """
        Get the Verus executable path.
        
        Search priority:
        1. VERUS_PATH environment variable
        2. VERUS_PATH in .env file
        3. Command line default parameter
        4. Automatic search in common locations
        5. Built-in fallback default
        
        Args:
            default: Fallback default if not found in config
            
        Returns:
            Path to Verus executable
        """
        # Priority 1-3: Explicit configuration
        explicit_path = (
            os.environ.get('VERUS_PATH') or
            self.config.get('VERUS_PATH') or
            default
        )
        
        if explicit_path:
            expanded_path = os.path.expanduser(explicit_path)
            # Verify the explicitly configured path exists
            if Path(expanded_path).exists():
                return expanded_path
            else:
                print(f"Warning: Configured Verus path does not exist: {expanded_path}")
        
        # Priority 4: Automatic search
        if self._cached_auto_verus_path is None:
            print("Searching for Verus installation...")
            self._cached_auto_verus_path = self._search_for_verus()
        
        if self._cached_auto_verus_path:
            print(f"Found Verus at: {self._cached_auto_verus_path}")
            return self._cached_auto_verus_path
        
        # Priority 5: Built-in fallback
        fallback_path = os.path.expanduser("~/Downloads/verus-0.2025.07.15.62362b0-x86-linux/verus-x86-linux/./verus")
        print(f"Warning: Verus not found automatically. Using fallback: {fallback_path}")
        print("Consider setting VERUS_PATH environment variable or adding it to .env file")
        
        return fallback_path
    
    def get_timeout(self, timeout_type: str = 'VERUS_TIMEOUT', default: int = 30) -> int:
        """
        Get timeout value for Verus operations.
        
        Args:
            timeout_type: Type of timeout ('VERUS_TIMEOUT' or 'VERUS_RANDOM_TIMEOUT')
            default: Default timeout value
            
        Returns:
            Timeout in seconds
        """
        timeout_str = (
            os.environ.get(timeout_type) or
            self.config.get(timeout_type) or
            str(default)
        )
        
        try:
            return int(timeout_str)
        except ValueError:
            print(f"Warning: Invalid {timeout_type} value '{timeout_str}', using default {default}")
            return default
    
    def get_bool(self, key: str, default: bool = False) -> bool:
        """
        Get a boolean configuration value.
        
        Args:
            key: Configuration key
            default: Default value if not found
            
        Returns:
            Boolean value
        """
        value = (
            os.environ.get(key) or
            self.config.get(key) or
            str(default)
        ).lower()
        
        return value in ('true', '1', 'yes', 'on')
    
    def get_string(self, key: str, default: str = "") -> str:
        """
        Get a string configuration value.
        
        Args:
            key: Configuration key  
            default: Default value if not found
            
        Returns:
            String value
        """
        return (
            os.environ.get(key) or
            self.config.get(key) or
            default
        )
    
    def get_extra_args(self) -> list:
        """
        Get additional Verus command line arguments.
        
        Returns:
            List of additional arguments
        """
        extra_args = self.get_string('VERUS_EXTRA_ARGS')
        if extra_args:
            return extra_args.split()
        return []
    
    def validate_verus_path(self, verus_path: str) -> bool:
        """
        Validate that the Verus executable exists and is executable.
        
        Args:
            verus_path: Path to validate
            
        Returns:
            True if valid, False otherwise
        """
        path = Path(verus_path)
        if not path.exists():
            print(f"Error: Verus executable not found at {verus_path}")
            
            # Try to provide helpful suggestions
            print("\nSuggestions:")
            print("1. Check if Verus is installed and the path is correct")
            print("2. Set VERUS_PATH environment variable: export VERUS_PATH=/path/to/verus")
            print("3. Add VERUS_PATH=/path/to/verus to your .env file")
            print("4. Install Verus from: https://github.com/verus-lang/verus")
            
            # Try automatic search to suggest alternatives
            print("\nSearching for Verus installations...")
            auto_found = self._cached_auto_verus_path or self._search_for_verus()
            if auto_found:
                print(f"Found alternative Verus installation at: {auto_found}")
                print(f"You can use: export VERUS_PATH={auto_found}")
            else:
                print("No Verus installations found automatically.")
            
            return False

        if not os.access(verus_path, os.X_OK):
            print(f"Error: Verus executable at {verus_path} is not executable")
            print(f"Try: chmod +x {verus_path}")
            return False

        # Additional validation: try to run verus --version
        if not self._verify_verus_executable(path):
            print(f"Warning: File at {verus_path} may not be a valid Verus executable")
            print("The file exists and is executable but doesn't respond to --version correctly")
            return False

        print(f"✓ Verus executable verified at: {verus_path}")
        return True
    
    def list_verus_installations(self) -> List[str]:
        """
        Find and list all Verus installations on the system.
        
        Returns:
            List of paths to valid Verus executables
        """
        print("Searching for all Verus installations...")
        
        # Search in all common locations
        search_dirs = [
            Path.home() / "Downloads",
            Path.home() / "tools",
            Path.home() / "bin", 
            Path.home() / ".local" / "bin",
            Path("/usr/local/bin"),
            Path("/opt"),
            Path("/usr/bin"),
            Path.home() / "verus",
            Path.home() / ".cargo" / "bin",
        ]
        
        verus_patterns = [
            "verus",
            "verus-*",
            "**/verus",
            "**/verus-**/verus",
            "**/verus-**/verus-*",
            "**/verus-*/bin/verus",
        ]
        
        found_installations = []
        
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue
                
            print(f"  Searching in: {search_dir}")
            
            for pattern in verus_patterns:
                try:
                    matches = list(search_dir.glob(pattern))
                    for match in matches:
                        if match.is_file() and os.access(match, os.X_OK):
                            match_str = str(match)
                            if self._verify_verus_executable(match) and match_str not in found_installations:
                                found_installations.append(match_str)
                                print(f"    ✓ Found: {match}")
                except Exception:
                    continue
        
        # Also check PATH
        verus_in_path = shutil.which('verus')
        if verus_in_path and verus_in_path not in found_installations:
            print(f"  ✓ Found in PATH: {verus_in_path}")
            found_installations.append(verus_in_path)
        
        if not found_installations:
            print("  No Verus installations found")
        
        return found_installations
    
    def print_config(self):
        """Print the current configuration for debugging."""
        print("Verus Configuration:")
        print(f"  Verus Path: {self.get_verus_path()}")
        print(f"  Default Timeout: {self.get_timeout()} seconds")
        print(f"  Random Test Timeout: {self.get_timeout('VERUS_RANDOM_TIMEOUT', 60)} seconds")
        print(f"  Extra Args: {' '.join(self.get_extra_args()) or 'None'}")
        print(f"  Skip Move Failed: {self.get_bool('SKIP_MOVE_FAILED')}")
        print(f"  Skip Summary: {self.get_bool('SKIP_SUMMARY')}")
        print(f"  No Timestamp: {self.get_bool('NO_TIMESTAMP')}")
        print(f"  Default Output Dir: {self.get_string('DEFAULT_OUTPUT_DIR') or 'Auto-generated'}")


# Global config instance
_config_instance = None


def get_config(env_file: Optional[str] = None) -> VerusConfig:
    """
    Get the global configuration instance.
    
    Args:
        env_file: Path to environment file (only used on first call)
        
    Returns:
        VerusConfig instance
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = VerusConfig(env_file)
    return _config_instance


def get_verus_path(default: Optional[str] = None) -> str:
    """Convenience function to get Verus path."""
    return get_config().get_verus_path(default)


def validate_verus_path(verus_path: str) -> bool:
    """Convenience function to validate Verus path."""
    return get_config().validate_verus_path(verus_path)


if __name__ == "__main__":
    # Enhanced CLI for testing configuration
    import argparse
    parser = argparse.ArgumentParser(
        description="Test Verus configuration loading and search for installations",
        epilog="""
Examples:
  python3 verus_config.py --validate         # Validate current config
  python3 verus_config.py --search           # Search for all Verus installations  
  python3 verus_config.py --env-file custom.env --validate
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--env-file", help="Path to .env file")
    parser.add_argument("--validate", action="store_true", help="Validate Verus path")
    parser.add_argument("--search", action="store_true", help="Search for all Verus installations")
    
    args = parser.parse_args()
    
    config = get_config(args.env_file)
    
    if args.search:
        installations = config.list_verus_installations()
        print(f"\nFound {len(installations)} Verus installation(s):")
        for i, path in enumerate(installations, 1):
            print(f"  {i}. {path}")
        
        if installations:
            print(f"\nTo use any of these, set:")
            print(f"  export VERUS_PATH={installations[0]}")
            print(f"Or add to .env file:")
            print(f"  VERUS_PATH={installations[0]}")
    else:
        config.print_config()
    
    if args.validate:
        verus_path = config.get_verus_path()
        is_valid = config.validate_verus_path(verus_path)
        print(f"\nVerus path validation: {'✓ PASS' if is_valid else '✗ FAIL'}")
        sys.exit(0 if is_valid else 1)
