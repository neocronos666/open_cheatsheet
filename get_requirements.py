'''
    ,=================================================.
    |           GET REQUIREMENTS v1.0 BETA            |
    |-------------------------------------------------|
    |  By. Sergio Silvestri  github.com/neocronos666/ |
    |-------------------------------------------------|
    | A simple script that crawls in his direcotry and|
    | subdirectories finding dependencies of py files |
    | then filter them and dump to requirements.txt   |
    '-------------------------------------------------'
'''
import os
import pkg_resources
import re

# Pattern to find imports and from-imports
import_pattern = re.compile(r'^\s*(?:import|from)\s+([^\s]+)')

def find_imports(file_path):
    """Find all imported modules in a given Python file."""
    imports = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = import_pattern.match(line)
            if match:
                module = match.group(1).split('.')[0]
                imports.add(module)
    return imports

def get_installed_packages():
    """Returns a dictionary of currently installed packages and their versions."""
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return installed_packages

def scan_directory(directory):
    """Recursively scan the directory for .py files and extract imports."""
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_imports = find_imports(file_path)
                all_imports.update(file_imports)
    return all_imports

def filter_installed(imports):
    """Filter out installed Python packages to avoid unnecessary entries."""
    installed_packages = get_installed_packages()
    return {pkg: installed_packages[pkg] for pkg in imports if pkg in installed_packages}

def write_requirements(requirements, output_file='requirements.txt'):
    """Write the requirements to a file."""
    with open(output_file, 'w') as f:
        for package, version in sorted(requirements.items()):
            f.write(f"{package}>={version}\n")
    print(f"Requirements written to {output_file}")

def main():
    print("Scanning for Python files and extracting requirements...")
    imports = scan_directory(os.getcwd())
    print(f"Found imports: {imports}")
    
    filtered_imports = filter_installed(imports)
    print(f"Filtered external requirements: {filtered_imports}")
    
    write_requirements(filtered_imports)

if __name__ == "__main__":
    main()



'''
import os
import pkg_resources
import re

# Pattern to find imports and from-imports
import_pattern = re.compile(r'^\s*(?:import|from)\s+([^\s]+)')

def find_imports(file_path):
    """Find all imported modules in a given Python file."""
    imports = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = import_pattern.match(line)
            if match:
                module = match.group(1).split('.')[0]
                imports.add(module)
    return imports

def get_installed_packages():
    """Returns a set of currently installed packages."""
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    return installed_packages

def scan_directory(directory):
    """Recursively scan the directory for .py files and extract imports."""
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_imports = find_imports(file_path)
                all_imports.update(file_imports)
    return all_imports

def filter_installed(imports):
    """Filter out installed Python packages to avoid unnecessary entries."""
    installed_packages = get_installed_packages()
    return imports.intersection(installed_packages)

def write_requirements(requirements, output_file='requirements.txt'):
    """Write the requirements to a file."""
    with open(output_file, 'w') as f:
        for package in sorted(requirements):
            f.write(f"{package}\n")
    print(f"Requirements written to {output_file}")

def main():
    print("Scanning for Python files and extracting requirements...")
    imports = scan_directory(os.getcwd())
    print(f"Found imports: {imports}")
    
    filtered_imports = filter_installed(imports)
    print(f"Filtered external requirements: {filtered_imports}")
    
    write_requirements(filtered_imports)

if __name__ == "__main__":
    main()
'''