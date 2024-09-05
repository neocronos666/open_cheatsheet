"""
    Setting Manager
    
    
    Use Logging:
    lg.info("Logging configurado correctamente.")







"""
import logging as lg
import json
import flet as ft

class SettingsManager:
    def __init__(self, settings_file='cfg/settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings()
        self.setup_logging()
        self.new_key_input = ""
        self.new_value_input = ""
        self.temp_settings = ""

    def load_settings(self):
        """Cargar configuraciones desde el archivo settings.json."""
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)
        return settings

    def setup_logging(self):
        """Configurar el sistema de logging según las opciones de configuración."""
        logging_level = self.settings.get("logging_level", "INFO")
        logging_file = self.settings.get("logging_file", "log/app.log")
        logging_format = self.settings.get("logging_format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        lg.basicConfig(level=logging_level,
                            format=logging_format,
                            handlers=[lg.FileHandler(logging_file), lg.StreamHandler()])

        lg.info("Logging configurado correctamente.")

    def update_setting(self, key, value):
        """Actualizar o agregar una configuración y guardarla en el archivo."""
        self.settings[key] = value
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def delete_setting(self, key):
        """Eliminar una configuración y guardarla en el archivo."""
        if key in self.settings:
            del self.settings[key]
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)

    def save_settings(self):
        """Guardar las configuraciones actuales en el archivo."""
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)
#-------------------------------------------------------------------------------------------
    def run_gui(self):
        """Ejecutar la interfaz gráfica para editar configuraciones."""
        self.new_key_input = ""
        self.new_value_input = ""
        self.temp_settings = ""
        
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
            temp_settings[key] = value

        
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
        def add_setting(self, e):
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
            if key in temp_settings:
                del temp_settings[key]
                update_list_view()

        def update_list_view():
            """Actualizar la vista de la lista de configuraciones."""
            list_view.controls = build_controls() #------------
            list_view.update()                    #------------

        def save_settings_and_close(e):
            """Guardar las configuraciones y cerrar la aplicación."""
            self.settings.update(temp_settings)
            self.save_settings()            
            # page.window_close() #--------------funcion deprecada

        temp_settings = self.settings.copy()

        # Crear la ventana de Flet
        def main(page: ft.Page):
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
        ft.app(target=main)

# Código para ejecutar la ventana si este archivo se ejecuta directamente
if __name__ == "__main__":
    sm = SettingsManager()
    sm.run_gui()



# ----------------------------------------------------------------------------
'''
import logging
import json
import flet as ft

class SettingsManager:
    def __init__(self, settings_file='cfg/settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings()
        self.setup_logging()

    def load_settings(self):
        """Cargar configuraciones desde el archivo settings.json."""
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)
        return settings

    def setup_logging(self):
        """Configurar el sistema de logging según las opciones de configuración."""
        logging_level = self.settings.get("logging_level", "INFO")
        logging_file = self.settings.get("logging_file", "log/app.log")
        logging_format = self.settings.get("logging_format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        logging.basicConfig(level=logging_level,
                            format=logging_format,
                            handlers=[logging.FileHandler(logging_file), logging.StreamHandler()])

        logging.info("Logging configurado correctamente.")

    def update_setting(self, key, value):
        """Actualizar o agregar una configuración y guardarla en el archivo."""
        self.settings[key] = value
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def delete_setting(self, key):
        """Eliminar una configuración y guardarla en el archivo."""
        if key in self.settings:
            del self.settings[key]
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)

    def save_settings(self):
        """Guardar las configuraciones actuales en el archivo."""
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def run_gui(self):
        """Ejecutar la interfaz gráfica para editar configuraciones."""
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
            temp_settings[key] = value

        def add_setting(e):
            """Agregar una nueva configuración a la lista."""
            new_key = new_key_input.value
            new_value = new_value_input.value
            if new_key and new_value:
                temp_settings[new_key] = new_value
                update_list_view()
                new_key_input.value = ""
                new_value_input.value = ""

        def delete_setting(key):
            """Eliminar una configuración."""
            if key in temp_settings:
                del temp_settings[key]
                update_list_view()

        def update_list_view():
            """Actualizar la vista de la lista de configuraciones."""
            list_view.controls = build_controls()
            list_view.update()

        def save_settings_and_close(e):
            """Guardar las configuraciones y cerrar la aplicación."""
            self.settings.update(temp_settings)
            self.save_settings()
            page.window_close()

        temp_settings = self.settings.copy()

        # Crear la ventana de Flet
        def main(page: ft.Page):
            page.title = "Settings Manager"
            page.horizontal_alignment = "center"
            page.vertical_alignment = "start"

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

        # Ejecutar la aplicación de Flet
        ft.app(target=main)

# Código para ejecutar la ventana si este archivo se ejecuta directamente
if __name__ == "__main__":
    sm = SettingsManager()
    sm.run_gui()
'''
# -------------------------------------------------

'''
import logging
import json

class SettingsManager:
    def __init__(self, settings_file):
        if settings_file == '':
            self.settings_file = 'cfg/settings.json'
        else:            
            self.settings_file = settings_file

        self.settings = self.load_settings()
        self.setup_logging()

    def load_settings(self):
        """Cargar configuraciones desde el archivo settings.cfg."""
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)
        return settings

    def setup_logging(self):
        """Configurar el sistema de logging según las opciones de configuración."""
        logging_level = self.settings.get("logging_level", "INFO")
        logging_file = self.settings.get("logging_file", "log/app.log")
        logging_format = self.settings.get("logging_format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        logging.basicConfig(level=logging_level,
                            format=logging_format,
                            handlers=[logging.FileHandler(logging_file), logging.StreamHandler()])

        logging.info("Logging configurado correctamente.")

    def update_setting(self, key, value):
        # Cargar las configuraciones actuales
        with open(self.settings_file, 'r') as f:
            settings = json.load(f)

        # Actualizar o agregar el nuevo valor
        settings[key] = value

        # Guardar las configuraciones actualizadas
        with open(self.settings_file, 'w') as f:
            json.dump(settings, f, indent=4)
'''

'''
# Ejemplo de uso
if __name__ == "__main__":
    #Si se inicia sin parametro toma por defecto el archivo cfg/settings.json
    ##settings_manager = SettingsManager('cfg/settings.json')

    #Ver todas las Settings
    ##print(settings_manager.settings)
   
    #Ver una setting
    ##print(settings_manager.settings.get('logging_file'))

    # Actualizar el autor por defecto
    ##settings_manager.update_setting('default_author', 'Neocronos666')

    # Verificar el cambio (opcional)
    # #print(settings_manager.load_settings())
    
#
#   Aca deberia cargar la app de manipulacion de opciones
#


    pass
'''