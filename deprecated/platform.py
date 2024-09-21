import flet as ft
import webbrowser

class PlatformUtils:
    platforms = [
        "ANDROID",
        "IOS",
        "LINUX",
        "MACOS",
        "WINDOWS"
    ]
    def __init__(self, page):
        self.page = page

    def open_web_browser(self, url):
        platform = self.get_platform()

        
        if platform in self.platforms:
            # Abre la URL en el navegador predeterminado del sistema si está en una plataforma admitida
            webbrowser.open(url)
        else:
            # Si la plataforma es web, usa JavaScript para abrir la URL en una nueva pestaña
            self.page.call_js_method("window.open", [url, "_blank"])

    def get_platform(self):
        # Obtiene la plataforma actual de la página
        return self.page.platform if self.page.platform in self.platforms else None






'''
import flet as ft
import webbrowser

class PlanformUtils():
    platforms = [
            "ANDROID",
            "IOS",
            "LINUX",
            "MACOS",
            "WINDOWS"
        ]
    
    def open_web_browser(self,url):
        
        # if page.platform == ft.Platform.WEB:
        if get_platform(self):
            webbrowser.open("url")            
        else:
            self.page.eval_js("window.open(url, '_blank');")
    
        def get_platform(self):
            return None if ft.Page.platform not in self.platforms else self.platforms
'''