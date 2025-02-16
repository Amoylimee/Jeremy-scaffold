#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

def create_init_file(project_path: Path, package_name: str) -> None:
    """Create __init__.py with version and imports."""
    init_content = f'''"""
{package_name} - Python package scaffold
"""

__version__ = "0.1.0"
__author__ = "Jeremy"
'''
    with open(project_path / 'src' / package_name / '__init__.py', 'w') as f:
        f.write(init_content)

def create_base_file(project_path: Path, package_name: str) -> None:
    """Create base.py with basic class structure."""
    base_content = '''from abc import ABC, abstractmethod

class BaseClass(ABC):
    """Abstract base class template."""
    
    def __init__(self):
        """Initialize base class."""
        pass
        
    @abstractmethod
    def process(self):
        """Template method to be implemented by subclasses."""
        pass
'''
    with open(project_path / 'src' / package_name / 'base.py', 'w') as f:
        f.write(base_content)

def create_test_file(project_path: Path) -> None:
    """Create basic test file."""
    test_content = '''
'''
    with open(project_path / 'tests' / 'test_module1.py', 'w') as f:
        f.write(test_content)

def create_example_file(project_path: Path, package_name: str) -> None:
    """Create example usage file."""
    example_content = f'''
# Add example usage here
'''
    with open(project_path / 'examples' / 'basic_usage.py', 'w') as f:
        f.write(example_content)

def create_pyproject_toml(project_path: Path, package_name: str) -> None:
    """Create pyproject.toml with minimal configuration."""
    pyproject_content = f'''[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "0.1.0"
requires-python = ">=3.8"

[tool.black]
line-length = 88
target-version = ["py38"]

[tool.isort]
profile = "black"
multi_line_output = 3
'''
    with open(project_path / 'pyproject.toml', 'w') as f:
        f.write(pyproject_content)

def create_readme(project_path: Path, package_name: str) -> None:
    """Create README.md with basic project information."""
    readme_content = f'''# {package_name}
## Installation

```bash
pip install -e .
```

## Usage

```python
from {package_name}.base import BaseClass
```
'''
    with open(project_path / 'README.md', 'w') as f:
        f.write(readme_content)

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

def create_project_structure(project_name: str, base_path: Path) -> None:
    """Create a new Python package project with standard structure."""
    project_path = base_path / project_name
    
    # Create directory structure
    directories = [
        Path('src') / project_name,
        Path('tests') / 'test_data',
        Path('examples'),
    ]
    
    for dir_path in directories:
        (project_path / dir_path).mkdir(parents=True, exist_ok=True)

    # Create package files
    create_init_file(project_path, project_name)
    create_base_file(project_path, project_name)
    create_test_file(project_path)
    create_example_file(project_path, project_name)
    
    # Create configuration files
    create_pyproject_toml(project_path, project_name)
    create_readme(project_path, project_name)
    create_license(project_path)
    create_gitignore(project_path)

def main():
    parser = argparse.ArgumentParser(description='Create a new Python package project structure')
    parser.add_argument('project_name', help='Name of the project/package')
    parser.add_argument('--path', default='.', help='Base path for project creation')
    
    args = parser.parse_args()
    create_project_structure(args.project_name, Path(args.path).resolve())
    
    print(f"\nPackage project {args.project_name} created successfully!")
    print(f"Next steps:")
    print(f"1. cd {args.project_name}")
    print(f"2. pip install -e .")

if __name__ == '__main__':
    main()