# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing
- Run tests: `pytest`
- Run specific test file: `pytest fluent-python/p13/randompick_test.py`
- Run tests with verbose output: `pytest -v`

### Python Execution
- Run main application: `python app.py`
- Run specific Python file: `python <file_path>`

### Virtual Environment
**IMPORTANT**: Always activate the virtual environment before running any prototype scripts or installing dependencies.

- The project uses a virtual environment located at `.venv/`
- Activate environment: `source .venv/bin/activate` (Unix/macOS) or `.venv\Scripts\activate` (Windows)
- Deactivate environment: `deactivate`
- All dependency installations and package downloads must be performed within the activated virtual environment

### Dependencies
**PREREQUISITE**: Ensure virtual environment is activated before running any of these commands.

- Install dependencies: `pip install -r python-crash-course/p20/requirements.txt`
- Update dependencies: `pip install -r python-crash-course/p20/requirements.txt --upgrade`
- Export current dependencies: `pip freeze > requirements.txt`

## Code Architecture

### Repository Structure
This repository is a Python learning project with two main educational tracks:

1. **`fluent-python/`** - Advanced Python concepts organized by chapters (p1-p15)
   - Each chapter contains multiple code examples (4-1-1.py, 4-2-1.py, etc.)
   - Focuses on Python idioms, design patterns, and advanced features
   - Includes test files for validating implementations

2. **`python-crash-course/`** - Beginner-friendly Python tutorials (p2-p20)
   - Progressive learning path from basics to advanced topics
   - Chapter p20 contains Django web development examples
   - Includes requirements.txt with Django and data science libraries

### Key Components

#### Main Application (`app.py`)
- Contains commented Python basics and examples
- Covers variables, strings, numbers, lists, tuples, functions, conditionals, dictionaries
- Serves as a quick reference for fundamental Python concepts

#### Documentation (`doc/`)
- All documentation-related files must be placed in this directory.
- Comprehensive Python concept explanations in Chinese
- Key topics include:
  - `python_multiple_inheritance.md` - Multiple inheritance patterns
  - `python_type_hints_summary.md` - Type hints comprehensive guide
  - `python_protocol_explained.md` - Protocol interface patterns
  - `python_args_kwargs.md` - Function arguments and keyword arguments
  - `python_private_attributes.md` - Private attribute conventions
  - `matrix_algorithms_intro.md` - Matrix algorithms introduction

#### Testing Patterns

- Tests use `pytest` framework
- Test files follow naming pattern `test_*.py`
- Tests focus on type checking and protocol validation
- Example: `fluent-python/p13/randompick_test.py` tests protocol implementation

### Code Style and Conventions

- Uses type hints extensively (`typing` module)
- Follows Python naming conventions (snake_case for variables/functions)
- Uses `TYPE_CHECKING` for import-time type validation
- Implements Protocol interfaces for structural typing

### Key Dependencies (from p20/requirements.txt)

- **Web Framework**: Django 5.2.1 with django-bootstrap5
- **Data Science**: pandas, numpy, matplotlib, plotly
- **Testing**: pytest
- **Game Development**: pygame
- **Utilities**: requests, urllib3, certifi

### VS Code Configuration

- Python language server disabled (`"python.languageServer": "None"`)
- Custom indentation settings for Python files
- Located in `.vscode/settings.json`

### Educational Focus

- Repository serves as a comprehensive Python learning resource
- Combines theoretical concepts (doc/) with practical examples (fluent-python/, python-crash-course/)
- Progressive difficulty from basic syntax to advanced design patterns
- Emphasis on Pythonic code and type safety
