
import logging as lg
import flet as ft
from components.global_cfg import GlobalCfg

class SettingsManager(ft.Column):
    def __init__(self, backlink=None):
        super().__init__()
       
        self.g_c = GlobalCfg()
        self.settings = []
        self.temp_settings = {}        
        self.g_c.setup_logging()
        self.back_link = backlink
        
        #self.run_gui(self.back_link)         
        
        self.controls = [
            self.build_all(self.back_link)
        ]

#-------------------------------BUILD ALL------------------------------------------------------------
    def build_all(self, back_link):     
        
        #---METODOS DE BUILD ALL------------

        def save_settings(e):
            """Guardar las configuraciones y cerrar la aplicación."""            
            if self.temp_settings:
                self.g_c.save_settings(self.temp_settings)            
            update_list_view()          

        def build_param_list():            
            controls = []            
            self.settings = self.temp_settings if self.temp_settings  else self.g_c.load_settings()
            for key, value in self.settings.items():
                controls.append(ft.Row([
                    ft.TextField(value=key, expand=1, read_only=True),
                    ft.TextField(value=str(value), expand=2, on_change=lambda e: update_temp_settings(key, e.control.value)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e: delete_setting(key))
                ]))
            return controls
        
        def update_temp_settings(key, value):
            """Actualizar la configuración temporalmente antes de guardarla."""           
            self.temp_settings = {}
            self.temp_settings = self.settings.copy()
            self.temp_settings[key] = value        
         
        def delete_setting(key):
            """Eliminar una configuración."""
            if not self.temp_settings: self.temp_settings = self.settings.copy()           
            if key in self.temp_settings:
                del self.temp_settings[key]          
            update_list_view()
        
        def update_list_view():  
            """Actualizar la vista de la lista de configuraciones."""            
            self.settings=self.temp_settings
            self.list_view.page.clean()
            settings_page(self.list_view.page)
        
        def add_setting(self):
            """Agregar una nueva configuración a la lista."""
            new_key = self.page.controls[1].controls[0].value
            new_value = self.page.controls[1].controls[1].value            
            if new_key and new_value:
                self.page.controls[1].controls[0].value = ""
                self.page.controls[1].controls[1].value = ""
                update_temp_settings(new_key,new_value)
                update_list_view()

        def build_settings_page():
            # page.title = "Settings Manager - [open CHEATSHEET pre-Alpha]"
            # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            # page.vertical_alignment = ft.MainAxisAlignment.CENTER
            # page.vertical_alignment = ft.MainAxisAlignment.START
            
            # Lista de configuraciones
            self.list_view = ft.Column(controls=build_param_list(), expand=1)

            # Entradas para nuevas configuraciones
            self.new_key_input = ft.TextField(label="New Key", expand=1)
            self.new_value_input = ft.TextField(label="New Value", expand=2)

            # Botón para agregar una nueva configuración
            self.add_button = ft.FilledButton(text="Add Setting", on_click=add_setting)

            # Botón para guardar las configuraciones y cerrar la ventana
            self.save_button = ft.FilledButton(text="Save Settings", on_click=save_settings)
            return [
                self.list_view,
                ft.Row([self.new_key_input, self.new_value_input, self.add_button], expand=0),
                self.save_button
            ]
        
            # Layout principal-------------ESTO DEBE DEVOLVER BUILD ALL
            '''
            page.add(
                self.list_view,
                ft.Row([self.new_key_input, self.new_value_input, self.add_button], expand=0),
                self.save_button
            )
            '''


        
        #---CODIGO DE BUILD ALL----------------

        settings_view = ft.Column()
        # settings_view.controls.append(build_param_list())
        settings_view.controls.append(build_settings_page())



        return settings_view
    
     

#----------------------RUN GUI--------------------------------
    def run_gui(self,nav_link=None):# Deberia llamarse BUILD y extender a column?
        """Ejecutar la interfaz gráfica para editar configuraciones."""        
        temp_settings = {}
        temp_settings = self.settings
        new_key_input = None
        new_value_input = None
        # gui = ft.Column        


        # INDENTACION
        def build_controls():# [FUNCIONANDO] No Tocar!!!
            """Construir controles de la lista de configuraciones."""
            controls = []            
            self.settings = self.temp_settings if self.temp_settings  else self.g_c.load_settings()
            for key, value in self.settings.items():
                controls.append(ft.Row([
                    ft.TextField(value=key, expand=1, read_only=True),
                    ft.TextField(value=str(value), expand=2, on_change=lambda e: update_temp_settings(key, e.control.value)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e: delete_setting(key))
                ]))
            return controls

        def update_temp_settings(key, value):# [FUNCIONANDO] No tocar!
            """Actualizar la configuración temporalmente antes de guardarla."""           
            self.temp_settings = {}
            self.temp_settings = self.settings.copy()
            self.temp_settings[key] = value        
     
        def add_setting(self):# [ANDANDO] NO TOCAR! CUCHA!
            """Agregar una nueva configuración a la lista."""
            new_key = self.page.controls[1].controls[0].value
            new_value = self.page.controls[1].controls[1].value            
            if new_key and new_value:
                self.page.controls[1].controls[0].value = ""
                self.page.controls[1].controls[1].value = ""
                update_temp_settings(new_key,new_value)
                update_list_view()

        def delete_setting(key):# [ANDA] NO TOCAR!!!
            """Eliminar una configuración."""
            if not self.temp_settings: self.temp_settings = self.settings.copy()           
            if key in self.temp_settings:
                del self.temp_settings[key]          
            update_list_view()
           
        def update_list_view():  # [FUNCIONA] No TOCAR!!!!!
            """Actualizar la vista de la lista de configuraciones."""            
            self.settings=self.temp_settings
            self.list_view.page.clean()
            settings_page(self.list_view.page)
            
        def save_settings(e):# [FUNCIONA] queda a la espera de implementacion de boton back
            """Guardar las configuraciones y cerrar la aplicación."""            
            if self.temp_settings:
                self.g_c.save_settings(self.temp_settings)            
            update_list_view()                                  
        
        # --------------Crear la ventana de Flet------------ESTO SE VA PARA MAIN-------------------------------------------
       
       
        def settings_page(page: ft.Page):
            page.title = "Settings Manager - [open CHEATSHEET pre-Alpha]"
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            #page.vertical_alignment = ft.MainAxisAlignment.START
            
            # Lista de configuraciones
            self.list_view = ft.Column(controls=build_controls(), expand=1)

            # Entradas para nuevas configuraciones
            self.new_key_input = ft.TextField(label="New Key", expand=1)
            self.new_value_input = ft.TextField(label="New Value", expand=2)

            # Botón para agregar una nueva configuración
            self.add_button = ft.FilledButton(text="Add Setting", on_click=add_setting)

            # Botón para guardar las configuraciones y cerrar la ventana
            self.save_button = ft.FilledButton(text="Save Settings", on_click=save_settings)

            # Layout principal
            page.add(
                self.list_view,
                ft.Row([self.new_key_input, self.new_value_input, self.add_button], expand=0),
                self.save_button
            )

        # Mostrar la ventana
        # ft.app(target=settings_page)
        # update_list_view()
        # return gui


# Código para ejecutar la ventana si este archivo se ejecuta directamente
if __name__ == "__main__":
    sm = SettingsManager()
    sm.run_gui()
    
