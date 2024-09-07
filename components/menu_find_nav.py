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

        find_button = ft.IconButton(icon=ft.icons.SEARCH)
        search_box = ft.TextField(hint_text="Search...", expand=True)
        back_button = ft.IconButton(icon=ft.icons.ARROW_BACK)

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
