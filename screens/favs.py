# screens/favs.py
import flet as ft
from utils import read_lists

class Favs(ft.Column):
    def __init__(self):
        super().__init__()
        self.fav_file = "./lists/.favs.chlist"
        self.fav_items = read_lists(self.fav_file)
        self.controls = [
            self.build_all()
        ]
            
    def build_all(self):
        file_view = ft.Column()
        fav_items = read_lists(self.fav_file)
        
        for line in fav_items:
            parts = line.strip().split('/')
            file_name = parts[-1]
            if len(parts) > 2:  # Exclude root-level directories
                file_view.controls.append(
                    ft.Container(
                        padding=ft.Padding(left=10, top=5, right=0, bottom=5),
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.INSERT_DRIVE_FILE),
                                ft.Text(file_name)
                            ],                                                            
                        ),
                        on_click=self.on_file_click
                    )
                )
        return file_view
    def on_file_click(self, e):
                   
        print( e.control.content.controls[1].value)

'''
    def build(self):
        fav_list_view = ft.ListView(
            items=[
                ft.TextButton(
                    text=item.split('/')[-1],  # Solo mostrar el nombre del archivo
                    on_click=lambda e, path=item: self.on_item_click(path)
                )
                for item in self.fav_items
            ]
        )

        return fav_list_view

    def on_item_click(self, path):
        print(f"Ruta completa: {path}")



# screens/favs.py
import flet as ft
from utils import read_lists

def favs_page(page: ft.Page):
    # Ruta del archivo de favoritos
    fav_file_path = "/lists/.fav.chlist"
    
    # Cargar el archivo de favoritos
    fav_items = read_lists(fav_file_path)

    # Función para manejar el click en los elementos de la lista
    def on_fav_click(e):
        print(f"Ruta completa del favorito: {e.control.data}")

    # Crear la lista de favoritos
    fav_list = ft.ListView(
        items=[
            ft.Text(fav_item.split("/")[-1], on_click=on_fav_click, data=fav_item)
            for fav_item in fav_items
        ],
        height=400,
    )

    # Mostrar la página
    page.controls.clear()
    page.controls.append(fav_list)
    page.update()
'''