# Codigo de sergio

import flet as ft



class MainContent(ft.Column):
    def __init__(self, buffer_file):
        super().__init__()
        self.buffer_file = buffer_file
        self.directory_structure = self.load_directory_structure()
        self.controls = [
            self.build_directory_view(),
            self.build_file_view()
        ]
        
    def load_directory_structure(self):
        directory_structure = {}
        with open(self.buffer_file, "r") as f:
            for line in f:
                parts = line.strip().split('/')
                current_level = directory_structure
                
                # Ignorar el último elemento ya que es el nombre del archivo
                for part in parts[:-1]:  
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
                    
        return directory_structure
    
    def build_directory_view(self, structure=None, level=0):
        if structure is None:
            structure = self.directory_structure

        directory_view = ft.Column()
        for directory, subdirectories in structure.items():
            directory_view.controls.append(
                ft.Container(
                    padding=ft.Padding(left=10 * level, top=5, right=0, bottom=5),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FOLDER),
                            ft.Text(directory)
                        ],
                    ),                    
                    on_click=self.on_category_click
                )
            )
            directory_view.controls.append(
                self.build_directory_view(subdirectories, level + 1)
            )
        return directory_view

    def build_file_view(self):
        file_view = ft.Column()
        with open(self.buffer_file, "r") as f:
            for line in f:
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
         #
         # Aca deberia abrir una ventana con la formula
         #
         print(f"Archivo seleccionado: {e.control.content.controls[1].value}")       
    
    #def on_category_click(self,e):
        # evento cuando se hace click en el directorios
    #    print(f"Categoria seleccionada: {e.control.content.controls[1].value}")       

    def on_category_click(self, e):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ROTO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        # Obtiene la categoría seleccionada
        selected_category = e.control.content.controls[1].value
        
        # Inicializa una lista para almacenar los archivos correspondientes a la categoría seleccionada
        filtered_files = []
        
        # Recorre el archivo buffer y filtra los archivos que pertenecen a la categoría seleccionada
        with open(self.buffer_file, "r") as f:
            for line in f:
                parts = line.strip().split('/')
                
                # Verifica si la ruta comienza con la categoría seleccionada
                if selected_category in parts:
                    # Si la categoría seleccionada es la raíz, muestra todos los archivos bajo ella
                    if parts[:-1] == selected_category.split('/'):
                        filtered_files.append(parts[-1])
                    # Si la categoría seleccionada está en una subcarpeta, muestra solo los archivos correspondientes
                    elif selected_category == parts[len(parts) - len(parts):len(parts)]:
                        filtered_files.append(parts[-1])
        
        # Actualiza el file_view con los archivos filtrados
        file_view = ft.Column()
        for file_name in filtered_files:
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
        
        # Actualiza los controles en la interfaz
        self.controls[1] = file_view
        self.update()

