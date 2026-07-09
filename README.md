# File Organizer CLI

A Command Line Interface (CLI) tool for automatically organizing your files into categorized folders and bulk renaming them. 
Built using Python's `click` library.

## Installation

You can install this tool directly from the source code. From the project directory, run:

```bash
pip install -e .
```

This will make the `file-mgr` command available in your terminal.

## Usage

### Organize Files

Sorts files in a specific directory into subfolders based on their extension.

```bash
file-mgr organize /path/to/directory
```

### Rename Files

Bulk renames files in a directory by replacing a specific pattern with a replacement string.

```bash
file-mgr rename /path/to/directory "old_pattern" "new_pattern"
```
