# screens/favs.py
import flet as ft
from utils import read_lists

class Favs(ft.Column):
    def __init__(self):
        super().__init__()
        self.fav_file = "./lists/.favs.chlist"
        self.fav_items = read_lists(self.fav_file)
        self.controls = [
            self.build_all()
        ]
            
    def build_all(self):
        file_view = ft.Column()
        fav_items = read_lists(self.fav_file)
        
        for line in fav_items:
            parts = line.strip().split('/')
            file_name = parts[-1]
            if len(parts) > 2:  # Exclude root-level directories
                file_view.controls.append(
                    ft.Container(
                        padding=ft.Padding(left=10, top=5, right=0, bottom=5),
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.BOOKMARK),
                                ft.Text(file_name)
                            ],                                                            
                        ),
                        on_click=self.on_file_click
                    )
                )
        return file_view
    def on_file_click(self, e):
                   
        print("VALOR CONTROL:" + self.find_full_path(e.control.content.controls[1].value))

        self.page.go("/sheet?s=" + self.find_full_path(e.control.content.controls[1].value))

    def find_full_path(self, filename):
        for path in self.fav_items:
            if path.endswith(filename):
                return path
        return None
