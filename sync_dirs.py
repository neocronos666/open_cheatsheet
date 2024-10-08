'''
    ,=================================================.
    |              SYNC DIRS v1.0 BETA                |
    |-------------------------------------------------|
    |  By. Sergio Silvestri  github.com/neocronos666/ |
    |-------------------------------------------------|
    | Create directories structure automatically      |
    | inside a directory from a txt file tabbed       |
    | see documentation on:                           |____________________________
    | https://github.com/neocronos666/open_cheatsheet/tree/main/docs/sync_dirs.md  |
    '------------------------------------------------------------------------------'
'''


import os

# Ruta del archivo de jerarquía y el directorio base donde crear las carpetas
archivo_jerarquia = "./docs/dirs.txt"
directorio_base = "./cheatsheets/"

def crear_directorios_desde_archivo(archivo, base_dir):
    # Verificar si el directorio base existe, si no, crearlo
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Abrir el archivo de jerarquía
    with open(archivo, 'r') as f:
        # Inicializamos una pila para manejar la jerarquía de directorios
        pila_rutas = [base_dir]
        nivel_anterior = 0

        for linea in f:
            # Eliminar espacios en blanco antes y después
            linea_limpia = linea.strip()

            # Calcular la profundidad del directorio basado en los espacios al inicio de la línea
            nivel_actual = (len(linea) - len(linea_limpia)) // 4  # Asumiendo 4 espacios por nivel

            # Si la línea está vacía o es inválida, la saltamos
            if not linea_limpia:
                continue

            # Si el nivel actual es más profundo que el anterior, añadimos a la pila
            if nivel_actual > nivel_anterior:
                pila_rutas.append(os.path.join(pila_rutas[-1], linea_limpia))

            # Si el nivel actual es más alto, hacemos 'pop' en la pila
            elif nivel_actual < nivel_anterior:
                diferencia = nivel_anterior - nivel_actual
                for _ in range(diferencia):
                    pila_rutas.pop()

                pila_rutas[-1] = os.path.join(os.path.dirname(pila_rutas[-1]), linea_limpia)

            # Si está en el mismo nivel, reemplazamos el último directorio
            else:
                pila_rutas[-1] = os.path.join(os.path.dirname(pila_rutas[-1]), linea_limpia)

            # Crear el directorio si no existe
            if not os.path.exists(pila_rutas[-1]):
                os.makedirs(pila_rutas[-1])
                print(f"Creado: {pila_rutas[-1]}")

            # Actualizamos el nivel anterior
            nivel_anterior = nivel_actual

# Ejecutar la función con las rutas dadas
crear_directorios_desde_archivo(archivo_jerarquia, directorio_base)
