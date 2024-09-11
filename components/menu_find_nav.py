#Codigo de sergio

import flet as ft


class MenuFindNav(ft.Row):
    def build(self):
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
        print("Settings------------")

    def on_new_click(self, e):        
        print("NEW------------")
    
    def on_help_click(self, e):        
        print("HELP------------")
    
    def on_about_click(self, e):        
        print("ABOUT------------")

    def on_back_click(self, e):
        print("BACK------------")
    
        # self.page.go("/favs")

    def on_search_click(self, e):
        print("SEARCH------------")
    def on_search_change(self,e):
        print(e.data)
        # print(self.all_paths)