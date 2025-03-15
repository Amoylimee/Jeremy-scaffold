#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

def create_run_bash(project_path: Path) -> None:
    """Create and initialize run.bash with pipeline structure."""
    run_bash_content = '''#!/bin/bash

# Create bash directory if it doesn't exist
mkdir -p bash

# Set log file paths
LOG_FILE="bash/pipeline_execution.log"
ERROR_LOG="bash/pipeline_errors.log"

# Clear previous logs
> "$LOG_FILE"
> "$ERROR_LOG"

# Record start time
echo "Pipeline execution started at $(date)" | tee -a "$LOG_FILE"

# Define script list
SCRIPTS=(
    "script1.py"
    "script2.py"
    "script3.py"
    # Add more scripts here
)

# Run each script
for script in "${SCRIPTS[@]}"; do
    echo -e "\n=== Running $script ===" | tee -a "$LOG_FILE"
    
    # Check if file exists
    if [ ! -f "$script" ]; then
        echo "Error: Script $script not found!" | tee -a "$ERROR_LOG"
        continue
    fi
    
    # Record start time
    start_time=$(date +%s)
    start_datetime=$(date)
    
    # Run Python script and wait for completion
    python "$script" 2>> "$ERROR_LOG" && wait
    
    if [ $? -eq 0 ]; then
        # Calculate execution time
        end_time=$(date +%s)
        end_datetime=$(date)
        duration=$((end_time - start_time))
        
        # Convert duration to readable format
        hours=$((duration / 3600))
        minutes=$(( (duration % 3600) / 60 ))
        seconds=$((duration % 60))
        
        echo "✓ Successfully completed $script" | tee -a "$LOG_FILE"
        echo "Started at: $start_datetime" | tee -a "$LOG_FILE"
        echo "Finished at: $end_datetime" | tee -a "$LOG_FILE"
        echo "Duration: ${hours}h ${minutes}m ${seconds}s" | tee -a "$LOG_FILE"
    else
        echo "✗ Failed to execute $script" | tee -a "$LOG_FILE"
        echo "Check $ERROR_LOG for details"
        
        read -p "Continue with next script? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Pipeline execution stopped by user" | tee -a "$LOG_FILE"
            exit 1
        fi
    fi
done

echo -e "\nPipeline execution completed at $(date)" | tee -a "$LOG_FILE"
'''
    
    with open(project_path / 'run.bash', 'w') as f:
        f.write(run_bash_content)
    os.chmod(project_path / 'run.bash', 0o755)

def create_helpers(project_path: Path) -> None:
    """Create and initialize helpers.py with basic utilities."""
    helpers_content = '''import os
from pathlib import Path

def set_working_directory() -> Path:
    """
    Set the working directory to the project root.
    This function should be called at the beginning of each script.
    
    Returns:
        Path: Project root directory path
    """
    # Get the directory of the current script
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Set working directory to project root (parent of current script)
    os.chdir(current_dir)
    
    return current_dir

def setup_paths() -> dict:
    """
    Create a dictionary of important project paths.
    
    Returns:
        dict: Dictionary containing paths for different project directories
    """
    root_dir = set_working_directory()
    
    paths = {
        'root': root_dir,
        'data': root_dir / 'data',
        'output': root_dir / 'output',
        'logs': root_dir / 'logs',
        'bash': root_dir / 'bash'
    }
    
    return paths

# Example usage:
if __name__ == "__main__":
    # Set working directory
    project_dir = set_working_directory()
    print(f"Working directory set to: {project_dir}")
    
    # Get project paths
    paths = setup_paths()
    print("Project paths:")
    for key, path in paths.items():
        print(f"{key}: {path}")
'''
    
    with open(project_path / 'helpers.py', 'w') as f:
        f.write(helpers_content)

def create_license(project_path: Path) -> None:
    """Create LICENSE file with MIT license."""
    current_year = datetime.now().year
    license_content = f'''MIT License

Copyright (c) {current_year} Jeremy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    with open(project_path / 'LICENSE', 'w') as f:
        f.write(license_content)

def create_gitignore(project_path: Path) -> None:
    """Create .gitignore file that ignores everything except specific files."""
    gitignore_content = '''# Ignore everything
*

# But not these files...
!.gitignore
!README.md
!LICENSE
'''
    with open(project_path / '.gitignore', 'w') as f:
        f.write(gitignore_content)

def create_readme(project_path: Path) -> None:
    """Create README.md with basic project information."""

    readme_content = '''# Project Title'''

    with open(project_path / 'README.md', 'w') as f:
        f.write(readme_content)

def create_project(project_name: str, base_path: Path) -> None:
    """Create a new project with basic structure."""
    project_path = base_path / project_name
    
    # Create basic directories
    directories = [
        'data',            # Raw data
        'output',           # Output files
        'logs',            # Log files
        'bash'             # Bash scripts
    ]
    
    for dir_path in directories:
        (project_path / dir_path).mkdir(parents=True, exist_ok=True)

    # Create configuration file
    (project_path / 'config.py').touch()
    
    # Create and initialize functions_helpers.py etc.
    create_helpers(project_path)
    create_gitignore(project_path)
    create_license(project_path)
    create_readme(project_path)
    
    # Create and initialize run.bash
    create_run_bash(project_path)
    os.chmod(project_path / 'run.bash', 0o755)

    # 创建 .gitignore 文件
    gitignore_content = '''# ignore all
*

# except for these files
!README.md
!.gitignore
!*.py
!*.bash'''

    with open(project_path / '.gitignore', 'w') as f:
        f.write(gitignore_content)

def main():
    parser = argparse.ArgumentParser(description='Create a new project structure')
    parser.add_argument('project_name', help='Name of the project')
    parser.add_argument('--path', default='.', help='Base path for project creation')
    
    args = parser.parse_args()
    create_project(args.project_name, Path(args.path).resolve())
    
    print(f"\nProject {args.project_name} created successfully!")
    print(f"cd {args.project_name}")

if __name__ == '__main__':
    main()