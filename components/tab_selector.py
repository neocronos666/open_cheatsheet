import flet as ft

class TabSelector(ft):
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
