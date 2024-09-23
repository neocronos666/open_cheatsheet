import flet as ft
import json
import os
import matplotlib.pyplot as plt
import io
# from components.menu_find_nav import MenuFindNav as bar

class CheatSheetViewer(ft.Column):
    def __init__(self, chsheet_file):
        super().__init__()
        self.chsheet_file = chsheet_file
        self.cheatsheet_data = self.load_cheatsheet()
        self.controls = self.render_cheatsheet()

    def load_cheatsheet(self):
        # Cargar el archivo .chsheet en memoria
        file_path = f"./cheatsheets/{self.chsheet_file}.chsheet"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print(f"Error: El archivo {file_path} no existe.")
            return None
    
    def render_latex_as_image(self, latex_string):
        # Crear un gráfico vacío y agregar el texto LaTeX
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${latex_string}$", fontsize=20, ha='center', va='center')
        ax.axis('off')

        # Guardar la imagen en un archivo temporal
        img_path = "./cfg/.latex_buffer.png"
        # ACA PODRIA ACTIVAR O DESACTIVAR LA CHACHE

        plt.savefig(img_path, format='png', bbox_inches='tight', pad_inches=0.1)
        # plt.savefig("output.svg", format="svg") Probar!!!!!
        plt.close(fig)

        return img_path  # Devolver la ruta del archivo de imagen
   
    def render_cheatsheet(self):
        if not self.cheatsheet_data:
            return []

        controls = []
        #---------Aca agrego a la paginacion
        # controls.append (bar.build)

        # Iterar directamente sobre las claves y valores de self.cheatsheet_data
        for key, value in self.cheatsheet_data.items():
            # print(f"Key: {key}, value: {value}")
            if key == "title":
                controls.append(ft.Text(value, size=24, weight="bold"))
            elif key == "description":
                controls.append(ft.Text(value, size=18))
            elif key == "detail":
                controls.append(ft.Markdown(value))
            elif key == "img":
                img_path = f"./images/{value}"                
                if os.path.exists(img_path):
                    controls.append(ft.Image(src=img_path))
                else:
                    print(f"Error: La imagen {img_path} no existe.")
            elif key == "forms":
                # controls.append(ft.Markdown(f"$$ {value} $$"))
                img_buffer = self.render_latex_as_image(value)
                controls.append(ft.Image(src=img_buffer, width=300))  # Puedes ajustar el tamaño


            elif key == "var_table":
                table = ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(" "))],
                    rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(item['var'] + ": " + item['desc']))]) for item in value]
                )
                controls.append(table)
            elif key == "cons_table":
                headers = value.get("headers", [])
                rows = value.get("rows", [])
                table = ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(header)) for header in headers],
                    rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row.values()]) for row in rows]
                )
                controls.append(table)

        return controls

# Ejemplo de uso:
# viewer = CheatSheetViewer("nombre_del_archivo")
# page.add(viewer)
