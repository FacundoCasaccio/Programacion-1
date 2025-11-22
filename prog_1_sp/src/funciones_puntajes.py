import json
import os

# Carga el archivo de puntajes para escribirlo sin pisar lo ya existente
# Luego, agrega los nuevos datos a l JSON siendo una lista de diccionarios
def escribir_json(datos: dict, nombre_archivo: str) -> None:
    lista_datos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo_json:
            try:
                lista_datos = json.load(archivo_json)
            except json.JSONDecodeError:
                lista_datos = []

    lista_datos.append(datos)

    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(lista_datos, archivo_json, indent=4)

# Lee el archivo de puntajes y devuelve una lista de diccionarios con estos
def leer_json(nombre_archivo: str) -> list:
    datos_leidos = []
    
    try:
        with open(nombre_archivo, 'r') as archivo_json:
            datos_leidos = json.load(archivo_json)
            return datos_leidos
    
    except FileNotFoundError:
        return datos_leidos