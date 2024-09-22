
### 2. `docs/chsheet_format.md`

Este archivo explica en detalle la estructura y los campos de un archivo `.chsheet`.

**Contenido sugerido:**

```markdown
# Formato de Archivos `.chsheet`

Los archivos `.chsheet` son archivos JSON que siguen una estructura específica para almacenar información sobre temas, fórmulas y conceptos. A continuación se detalla cada campo que puede aparecer en un archivo `.chsheet`.

## Estructura General

```json
{
    "title": "Título del tema",
    "description": "Descripción breve del tema",
    "detail": "<markup>Descripción detallada que puede incluir HTML o markup</markup>",
    "img": "Una imagen",
    "forms": "Fórmula en LaTeX",
    "var_table": [
        {"var": "nombre_variable", "desc": "Descripción de la variable usada en la imagen"}
    ],
    "cons_table": [
        {"constante": "nombre_constante", "valor": "valor", "descripcion": "tablas grandes solo de datos"}
    ],
    "c_date": "Fecha de creación del archivo",
    "m_date": "Fecha de última modificación",
    "author": "Nombre del autor",
    "email": "Correo del autor",
    "web": "Sitio web del autor",
    "ref_webs": [
        "URL de referencia 1",
        "URL de referencia 2"
    ],
    "rel_forms": [
       "Nombre de archivo .chsheet relacionado"
    ]
    
}
