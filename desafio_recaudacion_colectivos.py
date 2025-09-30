from menu_tools.menu_utils import print_menu
from operation_tools.arrays_generales import *
from input_tools.inputs import *
from especificos_ejercicios.funciones_colectivos import *

opciones_menu = [
    "1 - Cargar planilla de recaudación",
    "2 - Mostrar la recaudación de cada coche y línea",
    "3 - Calcular y mostrar la recaudación por línea",
    "4 - Calcular y mostrar la recaudación por coche",
    "5 - Calcular y mostrar la recaudación total",
    "6 - Salir del programa\n\n",
]

choferes = [111, 222, 333, 444, 555, 666, 777, 888, 999, 101010, 111111, 121212, 131313, 141414, 151515]
recaudaciones = inicializar_recaudaciones()
nombre_lineas = ["A", "B", "C"]

seleccion_usuario = 0

while seleccion_usuario != 6:
    
    print_menu(opciones_menu)
    seleccion_usuario = get_int(mensaje = f"Ingrese una opcion: ",
                            mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                            minimo = 1,
                            maximo = 6,
                            reintentos = 100)

    match seleccion_usuario:
        case 1:
            cargar_planilla(recaudaciones, choferes, nombre_lineas)
        
        case 2:
            recaudacion_lineas_coches(recaudaciones, nombre_lineas)
        
        case 3:
            mostrar_recaudacion_lineas(recaudaciones, nombre_lineas)
        
        case 4:
            mostrar_recaudacion_coches(recaudaciones, nombre_lineas)
        
        case 5:
            mostrar_recaudacion_total(recaudaciones)
    
    