import flet as ft

def main(page: ft.Page):
    # Título de la ventana
    page.title = "Flet App Test"
    
    # Definición de un texto
    label = ft.Text(value="Hello, Flet!", size=30)
    
    # Definición de un botón con un callback que se ejecuta al hacer clic
    def button_click(e):
        label.value = "Button Clicked!"
        page.update()

    button = ft.ElevatedButton(text="Click me!", on_click=button_click)
    
    # Agregar el texto y el botón a la página
    page.add(label, button)

# Ejecutar la app
ft.app(target=main)
