import json
import os
import logging
from datetime import datetime

class Cheatsheet:
    def __init__(self, title, description, detail, forms, var_table, cons_table, author, email, web, ref_webs, rel_forms, template, path):
        self.title = title
        self.description = description
        self.detail = detail
        self.forms = forms
        self.var_table = var_table
        self.cons_table = cons_table
        self.author = author
        self.email = email
        self.web = web
        self.ref_webs = ref_webs
        self.rel_forms = rel_forms
        self.template = template
        self.path = path
        self.c_date = datetime.now().strftime('%Y-%m-%d')
        self.m_date = self.c_date

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "detail": self.detail,
            "forms": self.forms,
            "var_table": self.var_table,
            "cons_table": self.cons_table,
            "c_date": self.c_date,
            "m_date": self.m_date,
            "author": self.author,
            "email": self.email,
            "web": self.web,
            "ref_webs": self.ref_webs,
            "rel_forms": self.rel_forms,
            "template": self.template
        }

    def save(self):
        """Guardar el archivo .chsheet en la ruta especificada."""
        os.makedirs(self.path, exist_ok=True)  # Crear el directorio si no existe
        file_path = os.path.join(self.path, f"{self.title}.chsheet")
        
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
        logging.info(f"Cheatsheet '{file_path}' creada exitosamente.")

# Ejemplo de uso
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Definición de datos para un cheatsheet
    var_table = [
        {"var": "xi", "desc": "Distancia Inicial"},
        {"var": "xf", "desc": "Distancia Final"},
        {"var": "t", "desc": "Tiempo transcurrido"},
        {"var": "v", "desc": "Velocidad"},
        {"var": "a", "desc": "aceleracion"}
    ]
    
    cons_table = {
        "headers": ["Constante", "Valor", "Descripción"],
        "rows": [
            {"constante": "g", "valor": "9.81 \\text{ m/s}^2", "descripcion": "Aceleración de la gravedad"},
            {"constante": "c", "valor": "3.00 \\times 10^8 \\text{ m/s}", "descripcion": "Velocidad de la luz en el vacío"}
        ]
    }
    
    ref_webs = [
        "http://web1.com",
        "http://web2.com"
    ]
    
    rel_forms = [
        "ES_Aceleracion_constante.chsheet",
        "ES_Caida_libre.chsheet"
    ]
    
    template = ["Default", "dark"]
    
    # Crear una nueva instancia de Cheatsheet
    cheatsheet = Cheatsheet(
        title="Movimiento rectilíneo uniformemente variado",
        description="Descripción breve sobre el movimiento rectilíneo uniformementye variado.",
        detail="<markup>Explicación detallada del tema, puede incluir múltiples párrafos, listas, etc.</markup>",
        forms="\\frac{d}{t} = v",
        var_table=var_table,
        cons_table=cons_table,
        author="Nombre del Autor",
        email="autor@example.com",
        web="http://autorwebsite.com",
        ref_webs=ref_webs,
        rel_forms=rel_forms,
        template=template,
        path="cheatsheets/fisica/cinematica/"
    )
    
    # Guardar el cheatsheet en la ruta especificada
    cheatsheet.save()
