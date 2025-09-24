from input_tools.inputs import get_int_matrix, get_int, get_unique_int_matrix
from operation_tools.arrays_generales import imprimir_matriz, generar_matriz_int_aleatoria, verificar_cuadrado_magico
from menu_tools.menu_utils import print_menu
import random

matriz = []
opciones_menu = [
    "1- Ingresar matriz",
    "2- Generar matriz aleatoria",
    "3- Salir"
]

print_menu(opciones_menu)

seleccion_usuario = get_int(mensaje = "Ingrese una opcion: ",
                            mensaje_error = "Opcion incorrecta, intente nuevamente. ",
                            minimo = 1,
                            maximo = 3,
                            reintentos = 100)


if seleccion_usuario != 3:
    
    if seleccion_usuario == 1:
        dimension_matriz = get_int(mensaje = "Ingrese dimension de la matriz ",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente",
                                minimo = 1,
                                maximo = 100,
                                reintentos = 99)
        
        matriz = get_unique_int_matrix(dimension_matriz, dimension_matriz, minimo = 1, maximo = (dimension_matriz ** 2))
    
    elif seleccion_usuario == 2:
        dimension_matriz = random.randint(1, 10)
        matriz = generar_matriz_int_aleatoria(filas = dimension_matriz,
                                    columnas = dimension_matriz,
                                    minimo = 1,
                                    maximo = (dimension_matriz ** 2))
        
    cuadrado_magico = verificar_cuadrado_magico(matriz)
    
    print("La matriz:")
    imprimir_matriz(matriz)
    
    if cuadrado_magico:
        print("Es un cuadrado magico")
    else:
        print("No es cuadrado magico")
    
    
else: 
    print("Adios!")

