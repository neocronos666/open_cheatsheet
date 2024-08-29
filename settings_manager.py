import logging
import json

class SettingsManager:
    def __init__(self, settings_file):
        if settings_file == '':
            self.settings_file = 'cfg/settings.json'
        else:            
            self.settings_file = settings_file

        self.settings = self.load_settings()
        self.setup_logging()

    def load_settings(self):
        """Cargar configuraciones desde el archivo settings.cfg."""
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)
        return settings

    def setup_logging(self):
        """Configurar el sistema de logging según las opciones de configuración."""
        logging_level = self.settings.get("logging_level", "INFO")
        logging_file = self.settings.get("logging_file", "log/app.log")
        logging_format = self.settings.get("logging_format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        logging.basicConfig(level=logging_level,
                            format=logging_format,
                            handlers=[logging.FileHandler(logging_file), logging.StreamHandler()])

        logging.info("Logging configurado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    #Si se inicia sin parametro toma por defecto el archivo cfg/settings.json
    settings_manager = SettingsManager('cfg/settings.json')

    #Ver todas las Settings
    print(settings_manager.settings)
    #Ver una setting
    print(settings_manager.settings.get('logging_file'))