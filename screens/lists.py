# screens/lists.py
import flet as ft
from utils import read_lists
import os

class Lists(ft.Column):
    def __init__(self,selected=None):
        super().__init__()
        self.lists_directory = "./lists" #Estos directorios deberian venir del setting manager
        # self.cheatsheets_directory = "./cheatsheets"

        self.selected_list = selected
        # print("----------ACAA------------")
        # print(os.listdir(self.lists_directory))
        self.list_files = [            
            file for file in os.listdir(self.lists_directory) if file.endswith(".chlist") and not file.startswith(".")
        ]
        self.list_content = []
        self.controls = [
            self.build_directory_view(),
             self.build_file_view()
        ]


    def build_directory_view(self):
        # Lista de archivos .chlist
        lists_view = ft.Column()  

        for file in self.list_files:                     
            lists_view.controls.append(
                        ft.Container(
                            padding=ft.Padding(left=10, top=5, right=0, bottom=5),
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.LIST),
                                    ft.Text(file)
                                    # ft.Text(file_name)
                                ],                                                            
                            ),
                            #on_click=self.on_file_click
                             on_click=lambda e: self.on_list_click(file)
                            #on_click=lambda e, line=line: self.on_item_click(self.lists_directory + "/" + line) if self.selected_list else None
                        )
                    )
            return lists_view       
    
    
    def build_file_view(self):
        # Lista de contenido de archivo seleccionado
        # self.content_view = ft.ListView()
        self.content_view = ft.Column()
        
        # if not self.selected_list:
        
        # con = ['Please Select a list'] if not self.selected_list else read_lists( self.lists_directory + self.selected_list) 
        if not self.selected_list:  #-----------------ACA PUEDE HABER LIO; VER QUE PASA CUANDO llega con un link
            con =[]
            con.append('Please Select a list')
        else:
            con = read_lists( self.lists_directory + "/" + self.selected_list) 
            print("DIR:" + self.lists_directory + "/" + self.selected_list)


        #    content = read_lists( self.lists_directory + self.selected_list) if not  self.selected_list
        print("---------------------CON:")
        print(con)

        for line in con:
            
            self.content_view.controls.append(
                ft.Container(

                    padding=ft.Padding(left=10, top=5, right=0, bottom=5),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.INSERT_DRIVE_FILE),
                            ft.Text(line)
                        ]                                                            
                    ),
                    # on_click=lambda e: self.on_file_click
                    # on_click = self.on_item_click(self.lists_directory + line) if self.selected_list
                    # on_click=lambda e, line=line: self.on_item_click(self.lists_directory + "/" + line) if self.selected_list else None
                    # on_click=lambda e, line=line: self.on_item_click(self.cheatsheets_directory + "/" + line) if self.selected_list else None
                    on_click=lambda e, line=line: self.on_item_click(line) if self.selected_list else None
                )
            )      
        return self.content_view


        

    def on_list_click(self, list_file):
        # self.selected_list = os.path.join(self.lists_directory, list_file)
        # self.list_content = read_lists(self.selected_list)
        # self.page.go("/list?s=" + list_file) 
        # self.update()
        print("----------------LIST CONTENT ON LIST CLICK, LIST FILE:")
        print(list_file)
        self.page.go("/lists?s=" + list_file) 
          # ---------------------ACA---------

    def on_item_click(self, path):
        print("----------------------ON ITEM CLICK. RUTA:")
        print(f"Ruta completa: {path}")
        # print(self.list_content)
        # self.page.go("/lists?s="+path)
        self.page.go("/sheet?s=" + path)



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