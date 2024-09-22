#Codigo de sergio

import flet as ft
from components.global_cfg import GlobalCfg
from buffer_manager import BufferManager

import subprocess
import sys

class MenuFindNav(ft.Row):
    def __init__(self,back_link):
        super().__init__()
        self.back_link = back_link
        buffer_manager = BufferManager()
        self.all_list = buffer_manager.get_buffer()
        self.search_results = []

    def build(self):
        # self.back_link = back_link
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Settings", on_click=self.on_settings_click),
                ft.PopupMenuItem(text="New (soon)", on_click=self.on_new_click),
                ft.PopupMenuItem(text="Help", on_click=self.on_help_click),
                ft.PopupMenuItem(text="About", on_click=self.on_about_click)
            ]
        )

        find_button = ft.IconButton(icon=ft.icons.SEARCH, on_click=self.on_search_click)
        # search_box = ft.TextField(hint_text="Search...", expand=True,on_change=self.on_search_change)
        search_box = ft.TextField(hint_text="Search...(soon)", expand=True)
        back_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.on_back_click)
        dropdown = ft.Dropdown()

        return ft.Row(
            [
                menu,
                search_box,
                find_button,
                back_button,
                # dropdown
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    
    def on_settings_click(self, e): #----------------ACA------------
       
        # self.page.go("/settings") 
        # print("Settings------------")

        subprocess.Popen([sys.executable, 'settings_manager.py'])
        #sys.exit()
        # self.page.window.visible = False
        self.page.window.close()
        self.page.update()  
        
    def on_new_click(self, e):        
        print("NEW----------(SOON)")
    
    def on_help_click(self, e):   #Anda pero probar.
        g_c = GlobalCfg()            
        self.page.launch_url(g_c.get_help_url())
    
    def on_about_click(self, e):                
        self.page.go("/about") 

    def on_back_click(self, e):        
        g_c = GlobalCfg()
        link=g_c.go_back()        
        if link: self.page.go(link)         

    def on_search_click(self, e):
        print("SEARCH------------")
        if self.search_results:
            first_result = self.search_results[0]
            self.page.go(f"sheet?s={first_result}")

    def on_search_change(self,e):
        # print(e.data)
        # print(self.all_paths)
        query = e.data
        if len(query) > 1:
            self.search_results = [item for item in self.all_list if query.lower() in item.lower()][:10]
            self.update_dropdown()
    
    def update_dropdown(self):
        self.dropdown.items = [ft.DropdownItem(text=result, on_click=self.on_dropdown_click) for result in self.search_results]
        self.dropdown.update()

    def on_dropdown_click(self, e):
        selected_result = e.control.text
        self.page.go(f"sheet?s={selected_result}")