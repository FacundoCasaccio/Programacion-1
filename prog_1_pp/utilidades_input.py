from prog_1_pp.utilidades_validacion import *
from prog_1_pp.utilidades_listas import *


"""
Pide entrada al usuario hasta que ingrese una entrada numerica dentro de los parametros maximo y minimo o agote reintentos
En caos de ingresar un flotante, lo convierte a entero
"""
def obtener_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int = 10):
    input_usuario = input(mensaje)
    bandera_dato_valido = validar_numero(input_usuario, minimo, maximo, int)


    while reintentos > 0 and bandera_dato_valido == False:
        print(mensaje_error)
        input_usuario = input(mensaje)
        bandera_dato_valido = validar_numero(input_usuario, minimo, maximo, int)
        reintentos -= 1
        
    if bandera_dato_valido == False:
        return None
    else:
        return int(input_usuario)
    
"""
Pide genero hasta ingresar un dato correcto esperado o agote intentos
Si no hubo intento satisfactorio, devuelve None
"""
def obtener_genero(mensaje: str, mensaje_error: str, reintentos: int = 10):
    genero_estudiante = input(mensaje)
    genero_valido = validar_genero(genero_estudiante)
        
    while reintentos > 0 and genero_valido == False:
        print(mensaje_error)
        genero_estudiante = input(mensaje)
        
        genero_valido = validar_genero(genero_estudiante)
        reintentos -= 1
        
    if genero_valido == False:
        genero_estudiante = None
        
    return genero_estudiante

"""
Pide legajoi hasta ingresar un dato correcto esperado o agote intentos
Si no hubo intento satisfactorio, devuelve None
"""
def obtener_legajo(mensaje: str, mensaje_error: str, reintentos: int = 10):
    legajo_estudiante = input(mensaje)
    
    legajo_valido = validar_legajo(legajo_estudiante)
        
    while reintentos > 0 and legajo_valido == False:
        print(mensaje_error)
        legajo_estudiante = input(mensaje)
        
        legajo_valido = validar_legajo(legajo_estudiante)
        reintentos -= 1
        
    if legajo_valido == False:
        legajo_estudiante = None
        
    return legajo_estudiante

"""
Pide nombre y apellido y valida que sea una cadena alfabetica
"""
def obtener_nombre_apellido(mensaje: str, mensaje_error: str, reintentos: int = 10):
    nombre_estudiante = input(mensaje)
    
    nombre_valido = verificar_cadena_alfabetica(nombre_estudiante)
        
    while reintentos > 0 and nombre_valido == False:
        print(mensaje_error)
        nombre_estudiante = input(mensaje)
        
        nombre_valido = verificar_cadena_alfabetica(nombre_estudiante)
        reintentos -= 1
        
    if nombre_valido == False:
        nombre_estudiante = None
        
    return nombre_estudiante


"""
Pide calificaciones, validando que sean datos validos y devuelve una lista de calificicaiones
"""
def obtener_calificaciones():
    CANTIDAD_ASIGNATURAS = 5
    
    calificaciones = [0] * CANTIDAD_ASIGNATURAS
    
    for i in range(CANTIDAD_ASIGNATURAS):
        calificacion = obtener_entero(mensaje = f"Ingrese nota del alumno para MATERIA_{i + 1} [1 - 10]: ", 
                                      mensaje_error = "Ingreso incorrecto, intente nuevamente",
                                      minimo = 1,
                                      maximo = 10)
        
        if calificacion == None:
            calificaciones = None
            break
        else:
            calificaciones[i] = calificacion
        
    return calificaciones


"""
Pide si desea continuar cargando datos y devuelve booleano 
"""
def obtener_continuar_carga(mensaje : str):
    respuesta_usuario = None
    continuar = None
    
    while respuesta_usuario != "s" and respuesta_usuario != "S" and respuesta_usuario != "n" and respuesta_usuario != "N":
        respuesta_usuario = input(mensaje) #Desea realizar otro ingreso? [S/N]: 
    
    if respuesta_usuario == "s" or respuesta_usuario == "S":
        continuar = True
    elif respuesta_usuario == "n" or respuesta_usuario == "N":
        continuar = False
        
    return continuar
    
    

