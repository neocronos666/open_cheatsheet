
import flet as ft
import webbrowser
from deprecated.platform import PlanformUtils

def main(page):
    def open_webpage(e):
        platforms = [
            "ANDROID",
            "IOS",
            "LINUX",
            "MACOS",
            "WINDOWS"
        ]



        # if page.platform == ft.Platform.WEB:
        if page.platform in platforms:
            webbrowser.open("https://www.repuestosimpresos.com")            
        # else:
            # page.eval_js("window.open('https://www.repuestosimpresos.com', '_blank');")


    page.title = "Abrir Página Web"
    page.add(
        ft.Text("Haz clic en el botón para abrir una página web en el navegador predeterminado."),
        ft.ElevatedButton("Abrir Página Web", on_click=open_webpage)
    )
    print(page.platform)
ft.app(target=main)

'''
import flet as ft

def main(page):
    def open_webpage(e):
        page.eval_js("window.open('https://www.example.com', '_blank');")

    page.title = "Abrir Página Web"
    page.add(
        ft.Text("Haz clic en el botón para abrir una página web en el navegador predeterminado."),
        ft.ElevatedButton("Abrir Página Web", on_click=open_webpage)
    )

ft.app(target=main, view=ft.WEB_BROWSER)
'''

