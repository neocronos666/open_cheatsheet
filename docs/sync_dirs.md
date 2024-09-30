# :file_folder: :ant: Sync Dirs Tool

## Overview

This Python application reads a hierarchical structure from a text file (`dirs.txt`) and automatically creates directories and subdirectories based on the indentation levels specified in the file. It creates all the directories inside a base directory (`/cheatsheets/`), which can be customized. 

This tool is useful for creating complex directory structures quickly based on predefined hierarchies, such as those used for educational purposes or any other organizational needs.

## Features
- Reads a file (`dirs.txt`) that defines directory structures using indentation.
- Creates directories and subdirectories according to the specified hierarchy.
- Supports dynamic creation of directories based on the hierarchy levels in the text file.
- Handles errors like missing base directories by automatically creating them if necessary.
- Easily customizable for different levels of indentation or custom base directories.

## Installation

### Requirements
This script uses only built-in Python modules, so no additional dependencies are required.

### Python Version
Make sure you have Python 3.x installed. You can check your Python version with:
```bash
python --version
```
## Example Directory Structure
If the `dirs.txt` file contains the following:
```css
Secundario
    Bachiller
        Primer Año
            Matemáticas
            Física
        Segundo Año
            Matemáticas
            Física
```
The following directories will be created:
```bash
/cheatsheets/Secundario/Bachiller/Primer Año/Matemáticas
/cheatsheets/Secundario/Bachiller/Primer Año/Física
/cheatsheets/Secundario/Bachiller/Segundo Año/Matemáticas
/cheatsheets/Secundario/Bachiller/Segundo Año/Física
```
