from utilidades_csv import *
from utilidades_json import *

# archivo = open("datos.txt", "r+")

# lineas_archivo = archivo.readlines()

# for linea in lineas_archivo:
#     print(linea, end="")
    
# archivo.close()

# leer_imprimir_csv(nombre_archivo = "estudiantes.csv")

# nombres_columnas = ["Nombre", "Edad", "Ciudad"]
# matriz = [["Pedro", 24, "París"], ["José", 25, "Toronto"]]

# escribir_csv(nombre_archivo = "datos_personas", nombres_columnas = nombres_columnas, matriz_datos = matriz)

datos = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Madrid"
}

nombre_archivo = "datos.json"

escribir_json(datos, nombre_archivo)
leer_json(nombre_archivo)