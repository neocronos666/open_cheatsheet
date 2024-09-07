#Codigo de sergio
import flet as ft
class TabSelector(ft.Row):
    def build(self):
        # back_button = ft.IconButton(icon=ft.icons.ARROW_BACK)
        up_button = ft.IconButton(icon=ft.icons.ARROW_UPWARD)
        tabs = ft.Tabs(
            selected_index=0,
            # animation_duration=300,
            tabs=[               
                ft.Tab(text="All"),
                ft.Tab(text="Lists"),
                ft.Tab(text="Favs")                
            ],
            expand=True,
            on_change=self.onchange_all
        )
        return ft.Row(
            [
                tabs,
                #back_button,
                up_button                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    def onchange_all(self,e):        
        if e.data =="0":            
            self.page.go("/")             
        elif e.data =="1":            
            self.page.go("/lists") 
        elif e.data =="2":            
            self.page.go("/favs") 

   











'''
class TabSelector(ft):
    def build(self):
        back_button = ft.IconButton(icon=ft.icons.ARROW_BACK)
        up_button = ft.IconButton(icon=ft.icons.ARROW_UPWARD)
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Favs"),
                ft.Tab(text="Lists"),
                ft.Tab(text="All")
            ],
            expand=True
        )

        return ft.Row(
            [
                tabs,
                back_button,
                up_button                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
'''