import os

def get_categories():
    # Suponiendo que tienes un directorio con categorías
    categories_path = 'path/to/your/categories'  # Cambia esto a la ruta correcta
    categories = [name for name in os.listdir(categories_path)
                  if os.path.isdir(os.path.join(categories_path, name))]
    return categories