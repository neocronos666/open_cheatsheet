
import logging as lg
import json
import flet as ft
from components.global_cfg import GlobalCfg

class SettingsManager:



    def __init__(self, settings_file='cfg/settings.json'):
        
        self.settings_file = settings_file

        self.g_c = GlobalCfg()

        # self.settings = self.load_settings()
        self.settings = self.g_c.load_settings()
        
        # self.setup_logging()
        self.g_c.setup_logging()

   
#-------------------------------------------------------------------------------------------
    def run_gui(self):# Deberia llamarse BUILD y extender a column?
        """Ejecutar la interfaz gráfica para editar configuraciones."""
        # self.new_key_input = ""
        # self.new_value_input = ""
        # self.temp_settings = ""
        temp_settings = {}
        temp_settings = self.settings
        new_key_input = None
        new_value_input = None

        def build_controls():
            """Construir controles de la lista de configuraciones."""
            controls = []
            for key, value in self.settings.items():
                controls.append(ft.Row([
                    ft.TextField(value=key, expand=1, read_only=True),
                    ft.TextField(value=str(value), expand=2, on_change=lambda e: update_temp_settings(key, e.control.value)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e: delete_setting(key))
                ]))
            return controls

        def update_temp_settings(key, value):
            """Actualizar la configuración temporalmente antes de guardarla."""
            print("UPDATE KEY: " + key + " VALUE: " + value)
            # print(self.temp_settings)
            self.temp_settings = {}
            temp_settings = self.settings.copy()
            self.temp_settings[key] = value

        
        '''
        def add_setting(e):#----------------------------------------
            """Agregar una nueva configuración a la lista."""
            new_key = self.new_key_input
            new_value = self.new_value_input
            if new_key and new_value:
                temp_settings[new_key] = new_value
                update_list_view()
                self.new_key_input = ""
                self.new_value_input = ""
        '''
        def add_setting(self):
            """Agregar una nueva configuración a la lista."""
            new_key = self.new_key_input
            new_value = self.new_value_input
            
            if new_key and new_value:
                # Agregar la nueva configuración al diccionario temporal
                self.temp_settings[new_key] = new_value

                # Guardar la configuración actualizada en el archivo settings.json
                self.save_settings()

                # Refrescar la lista en pantalla
                self.update_list_view()

                # Limpiar los campos de entrada
                self.new_key_input.value = ""
                self.new_value_input.value = ""

                # Actualizar la página
                self.page.update()



        def delete_setting(key):
            """Eliminar una configuración."""
            if key in self.temp_settings:
                del temp_settings[key]
                # update_list_view()
            print("KEY: " + key)
            print("SELF.temp_settings: ")
            print[self.temp_settings]

        def update_list_view():
            """Actualizar la vista de la lista de configuraciones."""
            list_view.controls = build_controls() #------------
            list_view.update()                    #------------

        def save_settings_and_close(e):
            """Guardar las configuraciones y cerrar la aplicación."""
            
            # self.settings.update(temp_settings)
            # self.settings.update(temp_settings) #-----------QUEDE ACA-----------

            print(self.temp_settings)
             # self.g_c.save_settings(self.temp_settings)            



            # page.window_close() #--------------funcion deprecada
            #    que save cambie a saved, espere 1 segundo y vuelva
       
        # temp_settings = self.settings.copy()

        # --------------Crear la ventana de Flet------------ESTO SE VA PARA MAIN
        def settings(page: ft.Page):
            page.title = "Settings Manager"
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            #page.vertical_alignment = ft.MainAxisAlignment.START

            # Lista de configuraciones
            list_view = ft.Column(controls=build_controls(), expand=1)

            # Entradas para nuevas configuraciones
            new_key_input = ft.TextField(label="New Key", expand=1)
            new_value_input = ft.TextField(label="New Value", expand=2)

            # Botón para agregar una nueva configuración
            add_button = ft.FilledButton(text="Add Setting", on_click=add_setting)

            # Botón para guardar las configuraciones y cerrar la ventana
            save_button = ft.FilledButton(text="Save Settings", on_click=save_settings_and_close)

            # Layout principal
            page.add(
                list_view,
                ft.Row([new_key_input, new_value_input, add_button], expand=0),
                save_button
            )

        # Mostrar la ventana
        ft.app(target=settings)

# Código para ejecutar la ventana si este archivo se ejecuta directamente
if __name__ == "__main__":
    sm = SettingsManager()
    sm.run_gui()

