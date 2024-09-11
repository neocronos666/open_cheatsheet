import flet as ft
import os

from components.menu_find_nav import *
from components.button_bar import *
from screens.main_content import *
from screens.cheat_sheet import *
from screens.lists import *
from screens.favs import *
from screens.lists import *

# ----Clases de Maquetacion-------------------------------------------
class MainApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.menu_find_nav = MenuFindNav()
        # self.tab_selector = TabSelector()
        self.iconbutton_selector = IconButtonSelector()
        self.main_content = MainContent(buffer_file="./cfg/.buffer")            
        self.controls = [
            self.menu_find_nav,
            self.iconbutton_selector,
            self.main_content
        ]
class FavsApp(ft.Column):
    def __init__(self):
        super().__init__()
        #self.menu_find_nav = self.page.controls.menu_find_nav
        self.menu_find_nav = MenuFindNav()
        self.tab_selector = IconButtonSelector()        
        # self.tab_selector = TabSelector()
        self.favs_content = Favs()            
        self.controls = [
            self.menu_find_nav,
            self.tab_selector,
            self.favs_content
        ]
class ListApp(ft.Column):
    def __init__(self,selected):
        super().__init__()
        #self.menu_find_nav = self.page.controls.menu_find_nav
        self.menu_find_nav = MenuFindNav()
        self.tab_selector = IconButtonSelector()                
        self.lists_content = Lists(selected)            
        self.controls = [
            self.menu_find_nav,
            self.tab_selector,
            self.lists_content
        ]

#---------Metodos propios--------------------

def main(page: ft.Page):
    page.title = "open CHEATSHEET pre-Alpha"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE  
    nav = []
    # Manejar rutas
    def route_change(route):        
        page.controls.clear()
        # param_value = page.route_params.get("s")
        print("--------------Page.route: " + page.route)

        full_route = page.route

        # Separar la ruta del parámetro (si existe)
        route_parts = full_route.split('?')

        # Almacenar la parte izquierda de la ruta
        path = route_parts[0]

        # Almacenar la parte derecha de la ruta (parámetro s)
        params = route_parts[1] if len(route_parts) > 1 else None

        # Extraer el valor de "s"
        s_value = None
        if params:
            selected_value = params.split('=')[1] if '=' in params else None
        
            #print("Ruta:", path)
            #print("Valor de 's':", s_value)
        
        

        #-------RUTAS-------------------------
        if page.route == "/":
            nav.append("/")
            page.add(MainApp())  # Página principal           
        elif path == "/sheet":
            nav.append(full_route)
            page.title = selected_value + " [open CHEATSHEET pre-Alpha]"            
            page.add(CheatSheetViewer(s_value))        
        elif page.route == "/lists":
            nav.append("/lists")
            print("-----LISTS")
            page.add(ListApp(0)) 
        elif page.route == "/favs":
            nav.append("/favs")
            print("-----FAVS")
            page.add(FavsApp())
        else:
            nav.append("/")
            page.route = "/"
            page.add(MainApp())
        print(nav)
        
    
    

    page.on_route_change = route_change
    page.go(page.route)  # Cargar la página principal al inicio
    
    
# ------------APP----------------------------




ft.app(target=main)
#ft.app(target=sheet)
