import flet as ft
import os

from components.menu_find_nav import *
from components.tab_selector import *
from screens.main_content import *
from screens.cheat_sheet import *

# --------------------------------------------------
class MyApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.menu_find_nav = MenuFindNav()
        self.tab_selector = TabSelector()
        self.main_content = MainContent(buffer_file="./cfg/.buffer")        
        self.controls = [
            self.menu_find_nav,
            self.tab_selector,
            self.main_content
        ]
  


def main(page: ft.Page):
    page.title = "open CHEATSHEET Alpha"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Create app and add to page
    page.add(MyApp())

def sheet(page: ft.Page,selected):
    page.title = " - open CHEATSHEET Alpha"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE    
    
    
    # Create app and add to page    
    #page.add(CheatSheetViewer("fisica/cinematica/Movimiento rectilíneo uniforme"))
    page.add(CheatSheetViewer(selected))
    

ft.app(target=main)
#ft.app(target=sheet)
