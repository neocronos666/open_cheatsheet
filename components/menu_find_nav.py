#Codigo de sergio

import flet as ft
from components.global_cfg import GlobalCfg

class MenuFindNav(ft.Row):
    def __init__(self,back_link):
        super().__init__()
        self.back_link = back_link

    def build(self):
        # self.back_link = back_link
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Settings", on_click=self.on_settings_click),
                ft.PopupMenuItem(text="New", on_click=self.on_new_click),
                ft.PopupMenuItem(text="Help", on_click=self.on_help_click),
                ft.PopupMenuItem(text="About", on_click=self.on_about_click)
            ]
        )

        find_button = ft.IconButton(icon=ft.icons.SEARCH, on_click=self.on_search_click)
        search_box = ft.TextField(hint_text="Search...", expand=True,on_change=self.on_search_change)
        back_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.on_back_click)

        return ft.Row(
            [
                menu,
                search_box,
                find_button,
                back_button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    
    def on_settings_click(self, e):
        # on_click=self.on_settings_click
        # g_c = GlobalCfg()
        # link=g_c.go_back()
        self.page.go("/settings") 



        print("Settings------------")

    def on_new_click(self, e):        
        print("NEW------------")
    
    def on_help_click(self, e):        
        print("HELP------------")
    
    def on_about_click(self, e):        
        print("ABOUT------------")

    def on_back_click(self, e):        
        g_c = GlobalCfg()
        link=g_c.go_back()
        print("Link: "+link if link else "VACIO")
        # if link:  
        
        # self.page.route = link
        # self.page.go(link) 
        print("----------------BACK-PRESSED----------------")
        print(g_c.get_nav_history())
        if link: self.page.go(link) 
        

        # print("----backlink: " + self.back_link)

    def on_search_click(self, e):
        print("SEARCH------------")
    def on_search_change(self,e):
        print(e.data)
        # print(self.all_paths)