import flet as ft
from components.global_cfg import GlobalCfg
from buffer_manager import BufferManager

import subprocess
import sys



class MenuFindNav(ft.Row):
    def __init__(self, back_link):
        super().__init__()
        self.back_link = back_link
        buffer_manager = BufferManager()
        self.all_list = buffer_manager.get_buffer()
        self.search_results = []

    def build(self):
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Settings", on_click=self.on_settings_click),
                ft.PopupMenuItem(text="New (soon)", on_click=self.on_new_click),
                ft.PopupMenuItem(text="Help", on_click=self.on_help_click),
                ft.PopupMenuItem(text="About", on_click=self.on_about_click)
            ]
        )

        # self.search_box = ft.TextField(hint_text="Search...", expand=True, on_change=self.on_search_change)
        self.find_button = ft.IconButton(icon=ft.icons.SEARCH, on_click=self.on_search_click)
        self.back_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.on_back_click)
        
        self.search_results_view = ft.ListView(expand=True, visible=False)       
        
        self.search_bar = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Search ...",
            view_hint_text="Type a subject",
            on_change=self.on_search_change,
            on_submit=self.on_search_click,
            on_tap=self.on_search_click,
            expand=True
            )
        
        #!!!!!!!!!!!!!!!!!!!!!REVISAR POR ACA, crea el menu y se cae en la searchbar
        
        return ft.Row(
            [
                menu,
                # self.search_box,
                self.search_bar,
                self.find_button,
                self.back_button,
                self.search_results_view
                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
        
        '''
        return ft.Column(  # Cambiado de Row a Column
            [
                ft.Row(
                    [
                        menu,
                        self.search_bar,
                        self.find_button,
                        self.back_button
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                    # expand=True   #!!!!!!!!!!!!!!!POSIBLE ERROR!!!!! deberia estar inicializado
                ),
                self.search_results_view
            ],
            # expand=True
        )
        '''

    def on_settings_click(self, e):        
        subprocess.Popen([sys.executable, 'settings_manager.py'])        
        self.page.window.close()
        self.page.update()  
        
    def on_new_click(self, e):        
        print("NEW----------(SOON)")
    
    def on_help_click(self, e):   #Anda pero probar.
        g_c = GlobalCfg()            
        self.page.launch_url(g_c.get_help_url())
    
    def on_about_click(self, e):                
        self.page.go("/about") 

    def on_back_click(self, e):        
        g_c = GlobalCfg()
        link=g_c.go_back()        
        if link: self.page.go(link)         
   


    def on_search_click(self, e):
        if self.search_results:
            print("---------------RESULTADO:")
            print(self.search_results[0])
            print(e.control.data)
            # self.page.go(self.search_results[0])
            # self.page.go('/sheet?s={}'.format(self.search_results[0]))
            self.page.go('/sheet?s={}'.format(e.control.data))
            
    
    def on_search_tap(self, e):
        if self.search_results:
            print("---------------RESULTADO:")
            print(self.search_results[0])
            # self.page.go(self.search_results[0])
            self.page.go('/sheet?s={}'.format(self.search_results[0]))



   
    def on_search_change(self, e):
        query = self.search_bar.value
        if len(query) >= 3:  # Cambiado a 3 para ahorrar recursos
            self.search_results = [item for item in self.all_list if query.lower() in item.lower()][:10]
            if len(self.search_results) >= 1:


                # self.search_bar.controls.clear()  # Asegúrate de llamar al método clear() correctamente
                self.search_results_view.controls.clear()

                # for result in self.search_results:
                #     self.search_results_view.controls.append(ft.ListTile(title=ft.Text(result), on_click=self.on_search_click, data=result))
                for result in self.search_results:
                    self.search_results_view.controls.append(
                        ft.ListTile(
                            title=ft.Row(  # Cambiamos el título por un Row
                                [
                                    ft.Column([  # Añadimos una columna para el texto y otros detalles
                                        ft.Text(result, weight="bold"),  # Texto principal (el resultado)
                                        ft.Text("Other info", size=12, color=ft.colors.GREY),  # Texto secundario (información adicional, si la hay)
                                    ])
                                ]
                            ),
                            on_click=self.on_search_click,
                            data=result
                        )
                    )


                self.search_results_view.visible = True
                self.search_results_view.update()
                
                self.search_bar.update()
  

        

    def get_results(self,e,search_results):
        controls = [
            #ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            #for i in range(10)
            ft.ListTile(title=ft.Text(search_results), on_click=self.on_search_click, data=i)
                for i in len(search_results)
        ]
        return controls
    '''
    def update_dropdown(self):
        self.dropdown.items = [ft.DropdownItem(text=result, on_click=self.on_dropdown_click) for result in self.search_results]
        self.dropdown.update()

    def on_dropdown_click(self, e):
        selected_result = e.control.text
        self.page.go(f"sheet?s={selected_result}")
    '''