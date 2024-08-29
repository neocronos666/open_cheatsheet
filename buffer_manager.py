import os

import logging
from settings_manager import *



class BufferManager:
    def __init__(self, cheatsheets_path, buffer_file):
        self.cheatsheets_path = cheatsheets_path
        self.buffer_file = buffer_file

    def create_buffer(self):
        """Crea un buffer con la lista de archivos .chsheet y lo guarda en un archivo.
        cheatsheet_files = [f.replace('.chsheet', '') for f in os.listdir(self.cheatsheets_path) if f.endswith('.chsheet')]
        """

        cheatsheet_files = []
        for root, dirs, files in os.walk(self.cheatsheets_path):
            for file in files:
                if file.endswith('.chsheet'):
                    # Guardar la ruta relativa desde cheatsheets
                    relative_path = os.path.relpath(os.path.join(root, file), self.cheatsheets_path)
                    cheatsheet_files.append(relative_path.replace('.chsheet', ''))


        with open(self.buffer_file, 'w') as f:
            for cheatsheet in cheatsheet_files:
                f.write(f"{cheatsheet}\n")

        logging.info(f"Buffer creado con {len(cheatsheet_files)} archivos .chsheet.")

    def load_buffer(self):
        """Carga y devuelve la lista de nombres de archivos desde el buffer."""
        if os.path.exists(self.buffer_file):
            with open(self.buffer_file, 'r') as f:
                cheatsheet_files = [line.strip() for line in f.readlines()]
            logging.info(f"Buffer cargado con {len(cheatsheet_files)} archivos.")
            return cheatsheet_files
        else:
            logging.error("El archivo de buffer no existe.")
            return []

# Ejemplo de uso
if __name__ == "__main__":
    settings_manager = SettingsManager('cfg/settings.json')
    
    buffer_manager = BufferManager('cheatsheets', 'cfg/.buffer')
    
    # Crear el buffer
    buffer_manager.create_buffer()
    
    # Cargar y consultar el buffer
    cheatsheets = buffer_manager.load_buffer()
    print("Cheatsheets en buffer:", cheatsheets)

    
