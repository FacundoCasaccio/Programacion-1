import json

def escribir_json(datos : dict, nombre_archivo : str):
    
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent = 4)


def leer_json(archivo : str):
    with open(archivo, 'r') as archivo_json:
        datos_leidos = json.load(archivo_json)

    print(f"Contenido de '{archivo}.json':")
    print(datos_leidos)