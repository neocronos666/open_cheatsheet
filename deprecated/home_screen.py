import flet as ft

class HomeScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        self.page.controls.append(
            ft.Column(
                [
                    ft.Text("Welcome to My Flet App", size=30),
                    ft.ElevatedButton(text="Click Me", on_click=self.on_button_click),
                ]
            )
        )

    def on_button_click(self, e):
        self.page.controls.append(ft.Text("Button clicked!", color=ft.colors.GREEN))
        self.page.update()
