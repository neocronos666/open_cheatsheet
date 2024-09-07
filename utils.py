import os

def get_categories():
    # Suponiendo que tienes un directorio con categorías
    categories_path = './cheatsheets/'  # Cambia esto a la ruta correcta
    categories = [name for name in os.listdir(categories_path)
                  if os.path.isdir(os.path.join(categories_path, name))]
    return categories

def read_lists(file_path):
    lines = []
    try:
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    return lines
