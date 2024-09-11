# screens/lists.py
import flet as ft
from utils import read_lists
import os

class Lists(ft.Column):
    def __init__(self,selected):
        super().__init__()
        self.lists_directory = "./lists"
        self.selected_list = None
        print("----------ACAA------------")
        print(os.listdir(self.lists_directory))
        self.list_files = [            
            file for file in os.listdir(self.lists_directory)if file.endswith(".chlist")
        ]
        self.list_content = []

    def build(self):
        # Lista de archivos .chlist
        lists_view = ft.Column(
            items=[
                ft.TextButton(
                    text=list_file,
                    on_click=lambda e, file=list_file: self.on_list_click(file)
                )
                for list_file in self.list_files
            ]
        )

        # Lista de contenido de archivo seleccionado
        self.content_view = ft.ListView(
            items=[
                ft.TextButton(
                    text=item.split('/')[-1],  # Mostrar solo el nombre
                    on_click=lambda e, path=item: self.on_item_click(path)
                )
                for item in self.list_content
            ]
        )

        return ft.Column([lists_view, self.content_view])

    def on_list_click(self, list_file):
        self.selected_list = os.path.join(self.lists_directory, list_file)
        self.list_content = read_lists(self.selected_list)
        self.update()

    def on_item_click(self, path):
        print(f"Ruta completa: {path}")



'''
# screens/lists.py
import flet as ft
import os
from utils import read_lists

def lists_page(page: ft.Page):
    # Ruta de la carpeta que contiene los archivos de listas
    lists_dir = "/lists/"

    # Obtener la lista de archivos en la carpeta /lists/
    list_files = [f for f in os.listdir(lists_dir) if f.endswith(".chlist")]

    # Variable para almacenar la lista de elementos del archivo seleccionado
    file_items = []

    # Función para manejar el click en los archivos de la lista superior
    def on_list_file_click(e):
        selected_file = e.control.data
        file_path = os.path.join(lists_dir, selected_file)
        global file_items
        file_items = read_lists(file_path)
        
        # Actualizar la segunda lista con el contenido del archivo seleccionado
        second_list.controls.clear()
        second_list.controls.extend([
            ft.Text(item.split("/")[-1], on_click=on_file_click, data=item)
            for item in file_items
        ])
        second_list.update()

    # Función para manejar el click en los elementos de la segunda lista
    def on_file_click(e):
        print(f"Ruta completa: {e.control.data}")

    # Crear la primera lista con los archivos en /lists/
    first_list = ft.ListView(
        items=[
            ft.Text(list_file, on_click=on_list_file_click, data=list_file)
            for list_file in list_files
        ],
        height=200,
    )

    # Crear la segunda lista (inicialmente vacía)
    second_list = ft.ListView(height=200)

    # Mostrar la página
    page.controls.clear()
    page.controls.append(first_list)
    page.controls.append(ft.Divider())
    page.controls.append(second_list)
    page.update()
'''