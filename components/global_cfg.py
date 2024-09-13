from typing import Any
import json
import logging as lg


class GlobalCfg:
    _instance = None    
    nav_hist = []
    settings_file='cfg/settings.json'
    settings = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCfg, cls).__new__(cls)
            # cls._instance.settings = {}            
            # cls._instance.nav_history = []
        return cls._instance
    
    def __init__(self):
        self.settings = self.load_settings()
        self.setup_logging()
    
    #--------NAVIGATION----------------
    def add_nav(self,nav):
        self.nav_hist.append(nav)
        print("----ADDED: "+nav)

    def get_nav_link(self):
        nav = self.nav_hist
        if len(nav) > 2: return str(nav[-2])
        elif len(nav)==1: return str(nav[-1])
        else: return "/"

    def get_nav_history(self):
        return self.nav_hist
    
    def go_back(self):
        if len(self.nav_hist) > 1:
            self.nav_hist.pop(-1) 
            return self.nav_hist[-1]
        else:
            return None
    
    #--------SETTINGS----------------
    def load_settings(self):
        """Cargar configuraciones desde el archivo settings.json."""
        settings = {}
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)
        return settings
    
    def update_setting(self, key, value):
        """Actualizar o agregar una configuración y guardarla en el archivo."""
        self.settings[key] = value
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def delete_setting(self, key):
        """Eliminar una configuración y guardarla en el archivo."""
        if key in self.settings:
            del self.settings[key]
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)

    def save_settings(self,set):
        """Guardar las configuraciones actuales en el archivo."""
        self.settings = set
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)
    


    #--------LOGGING-----------------
    def setup_logging(self):
        """Configurar el sistema de logging según las opciones de configuración."""
        logging_level = self.settings.get("logging_level", "INFO")
        logging_file = self.settings.get("logging_file", "log/app.log")
        logging_format = self.settings.get("logging_format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        lg.basicConfig(level=logging_level,
                            format=logging_format,
                            handlers=[lg.FileHandler(logging_file), lg.StreamHandler()])

        lg.info("Logging configurado correctamente.")