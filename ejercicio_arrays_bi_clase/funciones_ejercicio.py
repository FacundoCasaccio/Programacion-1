from operation_tools.arrays_generales import *
from input_tools.inputs import *
from ejercicio_arrays_bi_clase.funciones_ejercicio import *

def inicializar_vectores_matriz(longitud_listas = 100):
    nombres = generar_array_ceros(longitud_listas)
    estado_nombres = generar_array_ceros(longitud_listas)
    
    notas = generar_matriz_ceros(longitud_listas, 3)
    estado_notas = generar_array_ceros(longitud_listas)
    
    promedios = generar_array_ceros(longitud_listas)
    estado_promedios = generar_array_ceros(longitud_listas)
    
    
    return nombres, estado_nombres, notas, estado_notas, promedios, estado_promedios

def cargar_nombres(nombres, estado_nombres):
    continuar_carga = True
    
    while continuar_carga:
        cargar_datos(estado_nombres, nombres, mensaje = "Ingrese nombre y apellido del alumno: ")
        
        respuesta_usuario = input("Desea ingresar otro nombre? (s/n): ")
        
        while respuesta_usuario != "s" and respuesta_usuario != "n":
            respuesta_usuario = input("Respuesta incorrecta, responda nuevamente \nDesea ingresar otro nombre? (s/n): ")
            
        if respuesta_usuario == "n":
            continuar_carga = False
            
            
def cargar_notas_alumnos(notas, estado_notas, nombres, estado_nombres):
    
    for i in range(len(notas)):
        if estado_nombres[i] != 0:
            for j in range(len(notas[i])):
                
                if estado_nombres[i] != 0:
                    nota = get_int(mensaje = f"Ingrese nota del alumno {nombres[i]}",
                                    mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                    minimo = 1,
                                    maximo = 10,
                                    reintentos = 100)
                
                    notas[i][j] = nota
                    
            estado_notas[i] = 1


def calcular_promedios(notas, estado_notas, promedios, estado_promedios):
    
    for i in range(len(notas)):
        if estado_notas[i] != 0:
            notas_estudiante = notas[i]
            suma_notas_estudiante = 0
            for j in range(len(notas_estudiante)):
                suma_notas_estudiante += notas_estudiante[j]
                
            promedio_estudiante = suma_notas_estudiante / len(notas_estudiante)
            promedios[i] = promedio_estudiante
            estado_promedios[i] = 1
            

def listar_promedios(promedios, estado_promedios, nombres):
    piso_promedios = get_float(
        mensage = "Ingrese un piso para los promedios a mostrar: ",
        mensaje_error = "Ingreso incorrecto, intente nuevamente...",
        minimo = 1,
        maximo = 10,
        reintentos = 100
    )
    
    for i in range(len(promedios)):
        if estado_promedios[i] != 0:
            print(f"Alumno {nombres[i]} | promedio: {promedios[i]}")