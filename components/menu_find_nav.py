import flet as ft
from components.global_cfg import GlobalCfg
from buffer_manager import BufferManager

import subprocess
import sys

'''
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
'''
class MenuFindNav(ft.Row):
    def __init__(self, back_link):
        super().__init__()
        self.back_link = back_link
        buffer_manager = BufferManager()
        self.all_list = buffer_manager.get_buffer()
        self.search_results = []

    def build(self):
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Settings", on_click=self.on_settings_click),
                ft.PopupMenuItem(text="New (soon)", on_click=self.on_new_click),
                ft.PopupMenuItem(text="Help", on_click=self.on_help_click),
                ft.PopupMenuItem(text="About", on_click=self.on_about_click)
            ]
        )

        # self.search_box = ft.TextField(hint_text="Search...", expand=True, on_change=self.on_search_change)
        self.find_button = ft.IconButton(icon=ft.icons.SEARCH, on_click=self.on_search_click)
        self.back_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.on_back_click)
        self.search_bar = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Search colors...",
            view_hint_text="Type a subject",
            on_change=self.on_search_change,
            on_submit=self.on_search_click,
            on_tap=self.on_search_click
            )

        return ft.Row(
            [
                menu,
                # self.search_box,
                self.search_bar,
                self.find_button,
                self.back_button
                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    

    def on_settings_click(self, e):        
        subprocess.Popen([sys.executable, 'settings_manager.py'])        
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
    '''
    def on_search_click(self, e):
        print("SEARCH------------")
        if self.search_results:
            first_result = self.search_results[0]
            self.page.go(f"sheet?s={first_result}")
    '''
    def on_search_click(self, e):
        if self.search_results:
            print("---------------RESULTADO:")
            print(self.search_results[0])




    '''
    def on_search_change(self,e):        
        query = e.data
        if len(query) > 1:
            self.search_results = [item for item in self.all_list if query.lower() in item.lower()][:10]
            self.update_dropdown()
    -----
    def on_search_change(self, e):
        query = self.search_bar.value
        if len(query) >= 1: #Poner a 3 para ahorrar recursos
            self.search_results = [item for item in self.all_list if query.lower() in item.lower()][:10]
            #self.search_bar.controls = [ft.SearchBar(value=result) for result in self.search_results]
            if len (self.search_results) >= 1 :
                # self.search_bar.controls = self.get_results(self.search_results)
                self.search_bar.controls.clear
                self.search_bar.controls.append([         
                        ft.ListTile(title=ft.Text(self.search_results), on_click=self.on_search_click, data=i)
                        for i in range(len(self.search_results))
                        ]
                    )
                self.search_bar.update()
    '''
    def on_search_change(self, e):
        query = self.search_bar.value
        if len(query) >= 3:  # Cambiado a 3 para ahorrar recursos
            self.search_results = [item for item in self.all_list if query.lower() in item.lower()][:10]
            if len(self.search_results) >= 1:
                self.search_bar.controls.clear()  # Asegúrate de llamar al método clear() correctamente
                self.search_bar.controls = [
                        ft.ListTile(title=ft.Text(result), on_click=self.on_search_click, data=result)
                        for result in self.search_results
                    ]
                
                self.search_bar.update()
  


    def get_results(self,e,search_results):
        controls = [
            #ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            #for i in range(10)
            ft.ListTile(title=ft.Text(search_results), on_click=self.on_search_click, data=i)
                for i in len(search_results)
        ]
        return controls
    '''
    def update_dropdown(self):
        self.dropdown.items = [ft.DropdownItem(text=result, on_click=self.on_dropdown_click) for result in self.search_results]
        self.dropdown.update()

    def on_dropdown_click(self, e):
        selected_result = e.control.text
        self.page.go(f"sheet?s={selected_result}")
    '''