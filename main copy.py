import flet as ft
import os

class MenuFindNav(ft.Row):
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


class TabSelector(ft.Row):
    def build(self):
        back_button = ft.IconButton(icon=ft.icons.ARROW_BACK)
        up_button = ft.IconButton(icon=ft.icons.ARROW_UPWARD)
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Favs"),
                ft.Tab(text="Lists"),
                ft.Tab(text="All")
            ],
            expand=True
        )

        return ft.Row(
            [
                tabs,
                back_button,
                up_button                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )


class MainContent(ft.Column):
    def __init__(self, buffer_file):
        super().__init__()
        self.buffer_file = buffer_file
        self.directory_structure = {}
        self.controls = [self.load_directory_structure()]

    def load_directory_structure(self):
        with open(self.buffer_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Construimos un diccionario con la estructura de directorios
        for line in lines:
            path_parts = line.strip().split('/')
            current_level = self.directory_structure

            for part in path_parts:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        return self.build_directory_ui(self.directory_structure)

    def build_directory_ui(self, structure, level=0):
        directory_navigation = ft.Column()

        for key, value in structure.items():
            directory_navigation.controls.append(
                ft.Container(
                    padding=ft.Padding(left=10 * level, top=5, right=0, bottom=5),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FOLDER),
                            ft.Text(key)
                        ],
                    )
                )
            )
            if isinstance(value, dict):
                directory_navigation.controls.append(self.build_directory_ui(value, level + 1))
            else:
                # Para los archivos dentro de un directorio
                for file in value:
                    directory_navigation.controls.append(
                        ft.Container(
                            padding=ft.Padding(left=10 * (level + 1), top=5, right=0, bottom=5),
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.INSERT_DRIVE_FILE),
                                    ft.Text(file)
                                ],
                            )
                        )
                    )

        return directory_navigation


class MyApp(ft.Column):
    def __init__(self, buffer_file):
        super().__init__()
        self.menu_find_nav = MenuFindNav()
        self.tab_selector = TabSelector()
        self.main_content = MainContent(buffer_file=buffer_file)

        self.controls = [
            self.menu_find_nav,
            self.tab_selector,
            self.main_content
        ]


def main(page: ft.Page):
    page.title = "My App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Path al archivo .buffer
    buffer_file = "./cfg/.buffer"

    # Create app and add to page
    page.add(MyApp(buffer_file=buffer_file))


ft.app(target=main)
