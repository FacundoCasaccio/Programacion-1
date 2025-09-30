from menu_tools.menu_utils import print_menu
from operation_tools.arrays_generales import *
from input_tools.inputs import *
from especificos_ejercicios.funciones_ejercicio import *

"""
matriz de 100 por 3 elementos de números enteros, que van a representar las notas del curso de ingreso
ademas tendremos un vector de 100 elementos donde se cargaran los promedios de las tres notas

Menu de opciones:
1 - generar e inicializar los vectores y la matriz
2 - para cargar los datos: nombre
3 - cargar las notas en la matriz
4 - calcular y poblar los promedios
5 - buscar por promedio mayor o igual que el dato a buscar, y mostrar el listado de estudiantes que cumplen esa condicion
6 - Salir
"""

opciones_menu = [
    "1 - Generar e inicializar los vectores y la matriz",
    "2 - Para cargar los datos: nombre",
    "3 - Cargar las notas en la matriz",
    "4 - Calcular y poblar los promedios",
    "5 - Buscar por promedio mayor o igual que el dato a buscar, y mostrar el listado de estudiantes que cumplen esa condicion",
    "6 - Salir\n\n",
]

LONGITUD_LISTAS = 5 # Para que se lea mejor en consola
        
def programa():
    seleccion_usuario = 0
    nombres, estado_nombres, notas, estado_notas, promedios, estado_promedios = [], [], [], [], [], []
    
    while seleccion_usuario != 6:
        print_menu(opciones_menu)
        seleccion_usuario = get_int(mensaje = f"Ingrese una opcion: ",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                minimo = 1,
                                maximo = 7,
                                reintentos = 100)
    
        match seleccion_usuario:
            case 1:
                nombres, estado_nombres, notas, estado_notas, promedios, estado_promedios = inicializar_vectores_matriz(LONGITUD_LISTAS)
                
            case 2:
                cargar_nombres(nombres, estado_nombres)
                
            case 3:
                cargar_notas_alumnos(notas, estado_notas, nombres, estado_nombres)
                
            case 4:
                calcular_promedios(notas, estado_notas, promedios, estado_promedios)
                
            case 5:
                listar_promedios(promedios, estado_promedios, nombres)
                
            case 7: # Caso para debuggear
                listar_elementos(nombres)
                listar_elementos(estado_nombres)
                imprimir_matriz(notas)
                listar_elementos(estado_notas)
                listar_elementos(promedios)
                listar_elementos(estado_promedios)
    

programa()



