
### 3. `docs/chsheet_examples.md`

Este archivo proporciona ejemplos de archivos `.chsheet` completos.

**Contenido sugerido:**

```markdown
# Ejemplos de Archivos `.chsheet`

A continuación se muestran algunos ejemplos de archivos `.chsheet` para que puedas ver cómo se estructuran en la práctica.

## Ejemplo 1: Movimiento Rectilíneo Uniforme

```json
{
    "title": "Movimiento rectilíneo uniforme",
    "description": "Descripción breve sobre el movimiento rectilíneo uniforme.",
    "detail": "<markup>Explicación detallada del tema, puede incluir múltiples párrafos, listas, etc.</markup>",
    "forms": "\\frac{d}{t} = v",
    "var_table": [
        {"var": "d", "desc": "Distancia recorrida"},
        {"var": "t", "desc": "Tiempo transcurrido"},
        {"var": "v", "desc": "Velocidad"}
    ],
    "cons_table": [
        {"constante": "g", "valor": "9.81 \\text{ m/s}^2", "descripcion": "Aceleración de la gravedad"}
    ],
    "c_date": "2024-08-27",
    "m_date": "2024-08-27",
    "author": "Nombre del Autor",
    "email": "autor@example.com",
    "web": "http://autorwebsite.com",
    "ref_webs": [
        "http://web1.com", 
        "http://web2.com"
    ],
    "rel_forms": [
        "ES_Aceleracion_constante.chsheet", 
        "ES_Caida_libre.chsheet"
    ],
    "template": [
        "Default", 
        "dark"
    ]
}
