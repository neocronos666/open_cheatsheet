# get_requirements.py

This script scans a directory for Python files, extracts the imported modules, and generates a `requirements.txt` file with the necessary packages and their minimum versions.

## Usage

To use this script, place it in the root directory of your project and run it. The script will generate a `requirements.txt` file with the required packages.

```bash
python get_requirements.py
```

# Functions
## find_imports(file_path)
Finds all imported modules in a given Python file.

### Parameters:
    file_path (str): The path to the Python file.
### Returns:
    set: A set of imported modules.

## get_installed_packages()
Returns a dictionary of currently installed packages and their versions.
    ### Returns:
        dict: A dictionary where the keys are package names and the values are versions.

## scan_directory(directory)
Recursively scans the directory for .py files and extracts imports.
    ### Parameters:
        directory (str): The path to the directory to scan.
    ### Returns:
        set: A set of all found imported modules.

## filter_installed(imports)
Filters out installed Python packages to avoid unnecessary entries.

    ### Parameters:
        imports (set): A set of imported modules.
    ### Returns:
        dict: A dictionary of installed packages and their versions.

## write_requirements(requirements, output_file='requirements.txt')
Writes the requirements to a file.

    ### Parameters:
        requirements (dict): A dictionary of packages and their versions.

### output_file (str, optional): The name of the output file. Defaults to requirements.txt.
---
## main()
Main function that scans Python files, filters installed packages, and writes the requirements to a file.

