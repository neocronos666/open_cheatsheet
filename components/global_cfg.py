# Clase global solo para guardar valores de navegacion y configuracion


from typing import Any


class GlobalCfg:
    _instance = None    
    nav_hist = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCfg, cls).__new__(cls)
            # cls._instance.settings = {}            
            # cls._instance.nav_history = []
        return cls._instance
    
   
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
