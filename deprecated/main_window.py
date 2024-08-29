import flet as ft
from deprecated.home_screen import HomeScreen

def main(page: ft.Page):
    page.title = "My Flet App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Instancia de la pantalla principal
    home_screen = HomeScreen(page)
    home_screen.build()

    page.update()

# Ejecuta la aplicación
if __name__ == "__main__":
    ft.app(target=main)