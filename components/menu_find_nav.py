import flet as ft

class MenuFindNav(ft):
    def build(self):
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Settings"),
                ft.PopupMenuItem(text="New"),
                ft.PopupMenuItem(text="Help"),
                ft.PopupMenuItem(text="About")
            ]
        )

        find_button = ft.IconButton(icon=ft.icons.SEARCH)
        search_box = ft.TextField(hint_text="Search...", expand=True)

        return ft.Row(
            [
                menu,
                search_box,
                find_button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
