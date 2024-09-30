
import flet as ft
from functools import partial  # Para manejar eventos con parámetros específicos

class MainContent(ft.Column):
    def __init__(self, buffer_file=None):
        super().__init__()       
        
        self.buffer_file = buffer_file
        self.all_paths = []  # Lista para almacenar las rutas completas
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

                # Guardar la línea completa en la variable de la clase
                self.all_paths.append(line.strip())

                # Recorrer todos los directorios excepto el último (que es el archivo)
                for part in parts[:-1]:  
                    if part not in current_level:
                        current_level[part] = {"__file_count__": 0}  # Inicializamos contador de archivos en 0
                    current_level = current_level[part]
                
                # Aquí manejamos el archivo .chsheet
                file_name = parts[-1]
                # if file_name.endswith(".chsheet"):
                if file_name:
                    # Incrementamos el contador de archivos en el directorio actual
                    current_level["__file_count__"] += 1

        return directory_structure        
    def find_full_path(self, filename):
        for path in self.all_paths:
            if path.endswith(filename):
                return path
        return None   
    def build_directory_view(self, structure=None, level=0):
        if structure is None:
            structure = self.directory_structure

        directory_view = ft.Column()
        if isinstance(structure, dict):  # Verificamos si structure es un diccionario
            for directory, subdirectories in structure.items():               
                if directory == "__file_count__":
                    continue  # Omitimos el directorio __file_count__                
                file_count = 0  # Inicializamos file_count en 0
                if isinstance(subdirectories, dict):
                    # Cuenta la cantidad de archivos en la subcategoría
                    file_count = int(subdirectories.get("__file_count__", 0))

                directory_view.controls.append(
                    ft.Container(
                        padding=ft.Padding(left=10 * level, top=5, right=0, bottom=5),
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.FOLDER),
                                ft.Text(directory),
                                # Agregar el número de archivos en gris o en una burbuja
                                # ft.Text(f"({file_count})", color=ft.colors.GREY)
                                # O si prefieres la burbuja:
                                ft.Container(
                                    content=ft.Text(f"{file_count}"),
                                    bgcolor=ft.colors.GREY_200,
                                    padding=ft.Padding(5, 2, 5, 2),
                                    border_radius=ft.BorderRadius(10,10,10,10),
                                )
                            ],
                        ),
                        on_click=partial(self.on_category_click, directory=directory)
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
                            # Usa partial para los eventos de click
                            on_click=partial(self.on_file_click, file_name=file_name)
                        )
                    )
        return file_view

    def on_file_click(self, e, file_name):
        # Usar el nombre de archivo pasado como parámetro
        self.selected = self.find_full_path(file_name)
        self.page.go("/sheet?s=" + self.selected)

    def on_category_click(self, e, directory):        
        selected_category = directory  # Obtener el valor de directory pasado por partial        
        filtered_files = []        
        # Filtrar los archivos según la categoría seleccionada
        with open(self.buffer_file, "r") as f:
            for line in f:
                parts = line.strip().split('/')
                if directory in parts[:-1]:
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
                    on_click=partial(self.on_file_click, file_name=file_name)
                )
            )
        
        # Actualiza los controles en la interfaz
        self.controls[1] = file_view
        self.update()

    # Función para contar los archivos en una categoría
    def count_files_in_directory(self, subdirectories):
        count = 0
        if len(subdirectories):            
            for subdir, contents in subdirectories.items():
                if not isinstance(contents, dict):        
                    count += 1
        return count
