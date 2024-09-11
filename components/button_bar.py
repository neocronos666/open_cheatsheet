import flet as ft

class IconButtonSelector(ft.Row):
    def build(self):
        # Crear los tres botones con iconos
        all_button = ft.FilledButton(
            icon=ft.icons.ALL_INBOX, 
            on_click=self.onchange_button_0,
            text="All"
            )
        
        lists_button = ft.FilledButton(
            icon=ft.icons.LIST, 
            on_click=self.onchange_button_1,
            text="Lists"
            )
        
        favs_button = ft.FilledButton(
            icon=ft.icons.FAVORITE, 
            on_click=self.onchange_button_2,
            text="Favs"            
            )

        return ft.Row(
            [
                all_button,
                lists_button,
                favs_button
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

    # Funciones de manejo para cada botón
    def onchange_button_0(self, e):
        print("Botón 0 seleccionado: Home")
        # self.main_page.reset_main_content()        
        self.page.go("/")  # Navegar a la página inicial

    def onchange_button_1(self, e):
        print("Botón 1 seleccionado: Lists")
        self.page.go("/lists")  # Navegar a la página de listas

    def onchange_button_2(self, e):
        print("Botón 2 seleccionado: Favs")
        self.page.go("/favs")  # Navegar a la página de favoritos
