# Jeremy's scaffold to initialize a new project

A collection of Python scripts to quickly generate well-structured project templates, saving you time and ensuring consistency across your projects. Specially designed for pipeline-style workflows, these scaffolds help organize sequential data processing and analysis tasks.

## 🚀 Features

- **Project Scaffold** - Generate a basic project structure with directories for data, logs, and outputs, optimized for pipeline workflows
- **Package Scaffold** - Create a proper Python package structure with src layout, tests, and examples
- **Pipeline Management** - Built-in run.bash script to handle sequential script execution and logging
- **Workflow Oriented** - Directory structure and helpers designed specifically for data processing pipelines

## 🔄 Pipeline Workflow

The project scaffold is specifically designed for pipeline-style workflows where:

1. Data flows through a series of sequential processing steps
2. Each step is encapsulated in individual Python scripts
3. Scripts are executed in a defined order with proper logging
4. Progress and errors are tracked throughout the pipeline

The included `run.bash` script handles:
- Sequential execution of scripts in predefined order
- Comprehensive logging of execution times and results
- Error handling with the option to continue or abort the pipeline
- Timestamps and duration tracking for each pipeline step

This makes it perfect for data science workflows, ETL processes, or any project requiring sequential script execution with proper tracking.

## 📦 What's Included

### 1. Project Scaffold (`scaffold.py`)

Generates a simple project structure with:

- Organized directories (`data`, `output`, `logs`, `bash`)
- Helper utilities for path management
- Pre-configured bash script runner with pipeline execution and logging
- Sequential script execution with error handling
- Basic project configuration files

Perfect for data processing pipelines, ETL workflows, analysis projects, and any sequential processing tasks.

### 2. Package Scaffold (`scaffold_package.py`)

Creates a proper Python package structure with:

- `src` layout (PEP 517/518 compliant)
- Test directory with pytest setup
- Example usage scripts
- Properly initialized package files
- Configuration files (pyproject.toml)
- Documentation setup

Ideal for libraries, tools, and packages you plan to distribute.

## 🛠️ Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/Jeremy-scaffold.git
cd Jeremy-scaffold
```

Make the scripts executable:

```bash
chmod +x scaffold.py scaffold_package.py
```

You can also add them to your PATH for easier access.

## 🔧 Usage

### Creating a Simple Project

```bash
./scaffold.py my_project
# Or with custom path
./scaffold.py my_project --path /path/to/destination
```

### Creating a Python Package

```bash
./scaffold_package.py my_package
# Or with custom path
./scaffold_package.py my_package --path /path/to/destination
```

## 📚 Scaffolded Project Structure Examples

### Project Structure (from `scaffold.py`)

```
my_project/
├── bash/              # For bash execution logs
├── data/              # Raw data files
├── logs/              # Application logs
├── output/            # Generated outputs
├── .gitignore         # Pre-configured for Python
├── LICENSE            # MIT License
├── README.md          # Basic readme
├── config.py          # Project configuration
├── helpers.py         # Common helper functions
└── run.bash           # Script execution pipeline
```

### Package Structure (from `scaffold_package.py`)

```
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── base.py    # Abstract base classes
│       └── inner.py   # Path utilities
├── tests/
│   ├── test_data/
│   └── test_module1.py
├── examples/
│   └── basic_usage.py
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml     # Project configuration with build settings
```

## ⚖️ License

This project is licensed under the MIT License - see the `LICENSE` file for details.

