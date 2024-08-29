import flet as ft

class SettingsScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.Column(
            [
                ft.Text("Settings", size=30),
                ft.ElevatedButton(text="Back to Home", on_click=lambda e: self.page.go("/")),
            ]
        )
