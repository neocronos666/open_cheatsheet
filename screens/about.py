import flet as ft
import subprocess

class AboutScreen:
    def __init__(self, back_link):
        self.back_link = back_link
        self.version = self.get_latest_git_tag()
        # Definir los colores y estilos que podrán cambiarse fácilmente en el futuro
        self.styles = {
            "background_color": ft.colors.WHITE,
            "text_color": ft.colors.BLACK,
            "title_color": ft.colors.BLUE_GREY_900,
            "button_color": ft.colors.BLUE_GREY_700,
            "version_text_color": ft.colors.GREEN_500,
        }
        # Crear la vista
        self.view = self.create_view()

    def get_latest_git_tag(self):
        try:            
            # Obtener el commit más reciente asociado a un tag
            latest_commit = subprocess.check_output(["git", "rev-list", "--tags", "--max-count=1"], universal_newlines=True).strip()

            # Usar el commit para obtener el tag asociado
            latest_tag = subprocess.check_output(["git", "describe", "--tags", latest_commit], universal_newlines=True).strip()
            return latest_tag
        except subprocess.CalledProcessError:
            return "Unknown or Git Error"

    def create_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    # Título del cuadro de diálogo
                    ft.Text(
                        "About Open Cheatsheet",
                        style="headline4",
                        color=self.styles["title_color"],
                        weight="bold",
                    ),
                    # Descripción del proyecto
                    ft.Text(
                        "Open Cheatsheet is an open-source application designed to provide quick and easy access to various programming cheatsheets. It is licensed under the GPL.",
                        color=self.styles["text_color"],
                        size=16,
                    ),
                    # Versión obtenida de Git o manual
                    ft.Text(
                        f"Version: {self.version}",
                        color=self.styles["version_text_color"],
                        size=14,
                    ),
                    # Información de licencia
                    ft.Text(
                        "License: GPL",
                        color=self.styles["text_color"],
                        size=14,
                    ),
                    # Información del desarrollador
                    ft.Text(
                        "Developed by: Sergio Silvestri",
                        color=self.styles["text_color"],
                        size=14,
                    ),
                    # Botón "OK" centrado
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="OK",
                            on_click=lambda e: e.page.go(self.back_link),
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                                bgcolor=self.styles["button_color"],
                                # padding=ft.EdgeInsets(10, 15),
                                padding = ft.padding.all(10)                                
                            ),
                        ),
                        alignment=ft.alignment.center,                        
                        # padding=ft.EdgeInsets(top=20),
                        padding = ft.padding.only(top=20)
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=10,  # Espaciado entre los elementos
            ),
            padding=20,
            bgcolor=self.styles["background_color"],  # Color de fondo del cuadro de diálogo
            border_radius=ft.border_radius.all(10),   # Bordes redondeados para un diseño más moderno
            width=500,  # Tamaño del cuadro de diálogo
        )





'''
import flet as ft
import subprocess

class AboutScreen:
    def __init__(self, back_link):
        self.back_link = back_link
        self.version = self.get_latest_git_tag()
        # self.version = "1.00"
        self.view = self.create_view()

    def get_latest_git_tag(self):
        try:            
            # Obtener el commit más reciente asociado a un tag
            latest_commit = subprocess.check_output(["git", "rev-list", "--tags", "--max-count=1"], universal_newlines=True).strip()

            # Usar el commit para obtener el tag asociado
            latest_tag = subprocess.check_output(["git", "describe", "--tags", latest_commit], universal_newlines=True).strip()
            return latest_tag
        except subprocess.CalledProcessError:
            return "Unknown or Git Error"

    def create_view(self):
        return ft.Column(
            controls=[
                ft.Text("About Open Cheatsheet", style="headline4"),
                ft.Text("Open Cheatsheet is an open-source application designed to provide quick and easy access to various programming cheatsheets. It is licensed under the GPL."),
                ft.Text(f"Version: {self.version}"),
                ft.Text("License: GPL"),
                ft.Text("Developed by: Sergio Silvestri"),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="OK",
                        on_click=lambda e: e.page.go(self.back_link)
                    ),
                    alignment=ft.alignment.center
                )
            ]
        )

# Example usage:
# about_screen = AboutScreen("/home")
# print(about_screen.view)


'''