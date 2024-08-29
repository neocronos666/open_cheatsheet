import flet as ft
import os

class MainContent(ft):
    def __init__(self, base_dir):
        super().__init__()
        self.base_dir = base_dir
        self.file_list_view = ft.Column(expand=True)

    def build(self):
        # Carga la navegación de directorios
        directory_navigation = self.load_directory(self.base_dir)
        
        return ft.Column(
            [
                directory_navigation,
                self.file_list_view
            ],
            expand=True,
            spacing=5
        )

    def load_directory(self, path, level=0):
        items = []
        # Recorre los directorios y archivos
        for item in sorted(os.listdir(path)):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                # Añade un botón para cada directorio
                items.append(
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.FOLDER, color=ft.colors.GREY),
                                ft.Text(item),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10
                        ),
                        # padding=ft.EdgeInsets.symmetric(horizontal=10 * level, vertical=5),
                        on_click=lambda e, p=full_path: self.show_files(p)
                    )
                )
                
                # Carga los subdirectorios recursivamente
                items.append(self.load_directory(full_path, level + 1))

        return ft.Column(items, expand=True)

    def show_files(self, directory):
        files = []
        # Filtra los archivos con la extensión .chsheet
        for item in sorted(os.listdir(directory)):
            if item.endswith('.chsheet'):
                # Elimina la extensión .chsheet y agrega el nombre del archivo a la lista
                file_name = os.path.splitext(item)[0]
                files.append(
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.DESCRIPTION, color=ft.colors.BLUE_GREY),
                                ft.Text(file_name),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10
                        ),
                        padding=ft.EdgeInsets.symmetric(vertical=5)
                    )
                )
        
        self.file_list_view.controls.clear()
        self.file_list_view.controls.extend(files)
        self.update()

