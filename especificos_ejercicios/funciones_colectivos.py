from menu_tools.menu_utils import print_menu
from operation_tools.arrays_generales import *
from input_tools.inputs import *
from especificos_ejercicios import *

def inicializar_recaudaciones():
    recaudaciones = [[]] * 3
    for i in range(len(recaudaciones)):
        recaudaciones[i] = [0] * 5
        
    return recaudaciones

def validar_chofer(choferes):
    legajo = get_int(mensaje = f"Ingrese numero de legajo: ",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                minimo = 0,
                                maximo = 999999,
                                reintentos = 3)
    
    chofer_valido = False
    
    for i in range(len(choferes)):
        if legajo == choferes[i]:
            chofer_valido = True
            break
        
    return chofer_valido

def obtener_indice_linea_colectivo(linea_seleccionada, nombre_lineas):
    indice_linea = None
    for i in range(len(nombre_lineas)):
        if nombre_lineas[i] == linea_seleccionada:
            indice_linea = i
            
    return indice_linea

def cargar_planilla(recaudaciones, choferes, nombre_lineas):
    chofer_valido = validar_chofer(choferes)
    
    if chofer_valido:
        
        linea_seleccionada = get_string_with_length(mensage = "Ingrese linea a cargar [A, B o C]: ",
                                                    mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                                    reintentos = 3,
                                                    longitud = 1
                                                    )
        
        while linea_seleccionada != "A" and linea_seleccionada != "B" and linea_seleccionada != "C":
            linea_seleccionada = get_string_with_length(mensage = "Ingrese linea a cargar [A, B o C]: ",
                                                    mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                                    reintentos = 99,
                                                    longitud = 1
                                                    )
        
        coche_seleccionado = get_int(mensaje = f"Ingrese un coche (del 1 al 5)",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                minimo = 1,
                                maximo = 5,
                                reintentos = 100)
        
        indice_linea_seleccionada = obtener_indice_linea_colectivo(linea_seleccionada, nombre_lineas)
        
        recaudacion = get_float(mensage = "Ingrese recaudacion para el coche: ",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                minimo = 0,
                                maximo = 999999,
                                reintentos = 99)
        
        recaudaciones[indice_linea_seleccionada][coche_seleccionado - 1] += recaudacion# type: ignore
        
    else: 
        print("Legajo inexistente, intentelo nuevamente...\n\n")
        
        
def recaudacion_lineas_coches(recaudaciones, nombre_lineas):
    for i in range(len(recaudaciones)):
        total_linea = 0
        print(f"Linea {nombre_lineas[i]}:")
        
        for j in range(len(recaudaciones[i])):
            total_linea += recaudaciones[i][j]
            print(f"Coche {j}: ${recaudaciones[i][j]}")
            
        print(f"Total recaudacion de la linea: ${total_linea}\n")
        
        
def mostrar_recaudacion_lineas(recaudaciones, nombre_lineas):
    for i in range(len(recaudaciones)):
        recaudacion_linea = 0
        
        for j in range(len(recaudaciones[i])):
            recaudacion_linea += recaudaciones[i][j]
            
        print(f"Recaudacion de la linea {nombre_lineas[i]}: ${recaudacion_linea}")
        
def mostrar_recaudacion_coches(recaudaciones, nombre_lineas):
    
    for i in range(len(recaudaciones)):
        for j in range(len(recaudaciones[i])):
            print(f"Recaudacion de la linea {nombre_lineas[i]} coche {j + 1}: ${recaudaciones[i][j]}")
            
def mostrar_recaudacion_total(recaudaciones):
    recaudacion_total = 0
    
    for i in range(len(recaudaciones)):
        for j in range(len(recaudaciones[i])):
            recaudacion_total += recaudaciones[i][j]
            
    print(f"Recaudacion total: ${recaudacion_total}")