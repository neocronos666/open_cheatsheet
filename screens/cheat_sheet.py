import flet as ft
import json
import os
import matplotlib.pyplot as plt
import io


from matplotlib import transforms
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
    

    def render_latex_as_image(self, latex_string, font_size=20, font_family="serif", color="#7134eb", img_path = "./cfg/.latex_buffer.svg"):
        # Configurar la familia de fuentes y el color de la fuente en Matplotlib
        plt.rcParams['mathtext.fontset'] = 'custom'
        plt.rcParams['mathtext.rm'] = font_family
        plt.rcParams['mathtext.it'] = font_family
        plt.rcParams['mathtext.bf'] = font_family
        plt.rcParams['text.color'] = color              
        
        # Crear figura y ejes
        fig, ax = plt.subplots()

        # Agregar el texto LaTeX y obtener el objeto de texto
        text_obj = ax.text(0.5, 0.5, f"${latex_string}$", fontsize=font_size, ha='center', va='center', transform=ax.transAxes)

        # Desactivar ejes
        ax.axis('off')

        # Dibujar la figura para calcular el tamaño del texto
        fig.canvas.draw()

        # Obtener el tamaño del texto renderizado en unidades de figura
        bbox = text_obj.get_window_extent(renderer=fig.canvas.get_renderer())
        
        # Convertir las coordenadas del cuadro delimitador a coordenadas de figura
        inv = ax.transData.inverted()
        bbox_data = bbox.transformed(inv)

        # Calcular el tamaño del texto en coordenadas de figura
        width, height = bbox_data.width, bbox_data.height

        # Calcular el factor de escala necesario para que el texto quepa en la figura con un margen del 5%
        scale_x = 0.9 / width
        scale_y = 0.9 / height
        scale = min(scale_x, scale_y)

        # Escalar el tamaño de la fuente
        new_fontsize = text_obj.get_fontsize() * scale
        text_obj.set_fontsize(new_fontsize)

        # Establecer los márgenes para centrar el contenido
        # ax.margins(x=(1-scale_x)/2, y=(1-scale_y)/2)
        ax.margins(x= 0.05 / width, y= 0.05/height)

        # Ruta de la imagen SVG
        # img_path = "./cfg/.latex_buffer.svg"

        # Guardar la imagen en formato SVG con ajustes de tamaño
        plt.savefig(img_path, format="svg", bbox_inches='tight', pad_inches=0.1, transparent=True)
        plt.close(fig)

        return img_path


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
                img_buffer = self.render_latex_as_image(value,img_path = "./cfg/.latex_buffer2.svg")
                controls.append(ft.Image(src=img_buffer, width=500))  # Puedes ajustar el tamaño

            elif key == "var_table":
                table = ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(" "))],
                    rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(item['var'] + ": " + item['desc']))]) for item in value]
                )
                controls.append(table)
            elif key == "cons_table":
                headers = value.get("headers", [])
                rows = value.get("rows", [])
                if rows[0]:
                    table = ft.DataTable(
                        columns=[ft.DataColumn(ft.Text(header)) for header in headers],
                        rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row.values()]) for row in rows]
                    )
                    controls.append(table)

        return controls

# Ejemplo de uso:
# viewer = CheatSheetViewer("nombre_del_archivo")
# page.add(viewer)
