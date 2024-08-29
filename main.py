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
        self.directory_structure = self.load_directory_structure()
        self.controls = [
            self.build_directory_view(),
            self.build_file_view()
        ]

    def load_directory_structure(self):
        directory_structure = {}
        with open(self.buffer_file, "r") as f:
            for line in f:
                parts = line.strip().split('/')
                current_level = directory_structure
                for part in parts:
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
        return directory_structure

    def build_directory_view(self, structure=None, level=0):
        if structure is None:
            structure = self.directory_structure

        directory_view = ft.Column()
        for directory, subdirectories in structure.items():
            directory_view.controls.append(
                ft.Container(
                    padding=ft.Padding(left=10 * level, top=5, right=0, bottom=5),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FOLDER),
                            ft.Text(directory)
                        ],
                    )
                )
            )
            directory_view.controls.append(
                self.build_directory_view(subdirectories, level + 1)
            )
        return directory_view

    def build_file_view(self):
        file_view = ft.Column()
        with open(self.buffer_file, "r") as f:
            for line in f:
                parts = line.strip().split('/')
                file_name = parts[-1]
                if len(parts) > 2:  # Exclude root-level directories
                    file_view.controls.append(
                        ft.Container(
                            padding=ft.Padding(left=10, top=5, right=0, bottom=5),
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.INSERT_DRIVE_FILE),
                                    ft.Text(file_name)
                                ],
                                #on_click=self.on_file_click
                                
                            )
                        )
                    )
        return file_view

    def on_file_click(self, e):
        # Aquí puedes añadir el código para manejar el evento cuando se hace click en un archivo
        print(f"Archivo seleccionado: {e.control.content.controls[1].value}")


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
    page.title = "My App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Create app and add to page
    page.add(MyApp())


ft.app(target=main)
