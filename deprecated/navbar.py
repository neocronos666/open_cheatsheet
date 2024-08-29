import flet as ft

class NavBar(ft.UserControl):
    def build(self):
        return ft.Row(
            [
                ft.TextButton(text="Home", on_click=lambda e: self.page.go("/")),
                ft.TextButton(text="Settings", on_click=lambda e: self.page.go("/settings")),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
