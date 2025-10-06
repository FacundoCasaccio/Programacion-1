from prog_1_pp.utilidades_input import *
from prog_1_pp.utilidades_listas import *
from prog_1_pp.estudiantes_hardcodeados import *

def pedir_y_cargar_datos_estudiante(calificaciones, nombres, generos, legajos, estados):
    continuar_carga = True

    while continuar_carga:
        indice_carga_estudiante = obtener_indice_estado_vacio(estados)
        
        if indice_carga_estudiante != None: # Hay espacio en la matriz
        
            nombre_estudiante = obtener_nombre_apellido(mensaje = "Ingrese nombre y apellido del estudiante: ",
                                                        mensaje_error = "Ingreso incorrecto, intente nuevamente\n")
            
            legajo_estudiante = obtener_legajo(mensaje = "Ingrese legajo del estudiante [6 digitos numericos]: ",
                                            mensaje_error = "Ingreso incorrecto, intente nuevamente")
            
            genero_estudiante = obtener_genero(mensaje = "Ingrese genero del estudiante [F | M | X]: ",
                                            mensaje_error = "Ingreso incorrecto, intente nuevamente")
            
            calificaciones_estudiante = obtener_calificaciones()

            # Evitar carga de datos incorrectos
            if nombre_estudiante == None or legajo_estudiante == None or genero_estudiante == None or calificaciones_estudiante == None:
                print("Alguno de los datos ingresados no fue correcto, vuelva a intentarlo")
                continuar_carga = obtener_continuar_carga(mensaje = "Desea intentarlo nuevamente? [S | N]: ")
                
            else:
                nombres[indice_carga_estudiante] = nombre_estudiante
                legajos[indice_carga_estudiante] = legajo_estudiante
                generos[indice_carga_estudiante] = genero_estudiante
                calificaciones[indice_carga_estudiante] = calificaciones_estudiante
                estados[indice_carga_estudiante] = 1
                print("Datos de estudiante cargados satisfactoriamente\n")
                continuar_carga = obtener_continuar_carga(mensaje = "Desea cargar datos de otro estudiante? [S | N]: ")
                
        else:
            print("No hay espacio disponible en el sistema")
            continuar_carga = False
        

"""
Muestra los datos de todos los estudiantes, incluyendo nombre, apellido, legajo y genero
"""
def mostrar_datos_estudiantes(calificaciones, nombres, generos, legajos, estados, promedios):
    for i in range(len(estados)): 
        if estados[i] == 1:
            print(f"Alumno: {nombres[i]} | Legajo: {legajos[i]} | Genero: {generos[i]}")
            print("Calificaciones: ")
            
            for j in range(len(calificaciones[i])):
                print(f"MATERIA_{j + 1}: {calificaciones[i][j]}")
                
            if promedios[i] != None:
                print(f"Promedio: {promedios[i]}")
                
            print() # Solamente para separar entre estudiantes y sea mas legible
            

"""
Recorre las calificaciones y calcula promedios, devolviendo una nueva lista con estos
"""
def calcular_promedios_estudiantes(calificaciones, estados):
    promedios = [0.0] * len(calificaciones)
    
    for i in range(len(calificaciones)):
        estado = estados[i]
        
        if estado == 1:
            total_calificaciones_estudiante = 0
            
            for j in range(len(calificaciones[i])):
                calificacion = calificaciones[i][j]
                
                total_calificaciones_estudiante += calificacion
                
            promedio_estudiante = total_calificaciones_estudiante / len(calificaciones[i])
            promedios[i] = promedio_estudiante
            
    print("Promedios calculados exitosamente\n")
    
    return promedios

"""
Copia y ordena las listas de estudiantes para mostrarlas en pantalla de manera ordenada ASC o DESC
"""
def mostrar_datos_por_promedio(calificaciones, nombres, generos, legajos, estados, promedios, ascendente : bool = False):
        calificaciones_ordenadas, nombres_ordenados, legajos_ordenados, generos_ordenados, estados_ordenados, promedios_ordenados = ordenar_estudiantes_por_promedio(calificaciones, nombres, legajos, generos, estados, promedios, ascendente = ascendente)
        
        mostrar_datos_estudiantes(calificaciones_ordenadas, nombres_ordenados, legajos_ordenados, generos_ordenados, estados_ordenados, promedios_ordenados)
        
        
# Compara el promedio mas alto con los promedios de las materias y muestra lo/s mas altas
def mostrar_materias_mas_promedio(calificaiones, estados):
    promedios_materias = calcular_promedios_materias(calificaiones, estados)
    promedio_mas_alto = obtener_promedio_materia_mas_alto(calificaiones, estados)
            
    for i in range(len(promedios_materias)):
        promedio = promedios_materias[i]
        
        if promedio == promedio_mas_alto:
            print(f"MATERIA_{i + 1} | Promedio general: {promedio_mas_alto}")
            
"""
Pide y valida legajo. Busca indice de ese legajo y meustra los datos correspondientes si los encuentra
"""
def mostrar_datos_por_legajo(calificaciones, nombres, generos, legajos, estados, promedios):
    legajo_estudiante = obtener_legajo(mensaje = "Ingrese legajo del estudiante [6 digitos numericos]: ",
                                        mensaje_error = "Ingreso incorrecto, intente nuevamente")
    
    indice_legajo = obtener_indice_legajo(legajo_estudiante, legajos, estados)
    
    if indice_legajo != None:
        print(f"Alumno: {nombres[indice_legajo]} | Legajo: {legajos[indice_legajo]} | Genero: {generos[indice_legajo]}")
        print("Calificaciones: ")
        
        for j in range(len(calificaciones[indice_legajo])):
            print(f"MATERIA_{j + 1}: {calificaciones[indice_legajo][j]}")
            
        if promedios[indice_legajo] != None:
            print(f"Promedio: {promedios[indice_legajo]}")
            
        print() # Solamente para separar entre estudiantes y sea mas legible
           
# Muestra la cantidad de apariciones por nota individual por cada una de las materias
def mostrar_notas_repetidas_materias(calificaciones, estados):
    
    for i in range(len(calificaciones[0])):
        repeticiones_por_calificacion = obtener_repeticiones_notas_materia(i, calificaciones, estados)
        
        print(f"Cantidad de repeticiones por calificacion en MATERIA_{i + 1}:")
        print("Calificacion | Repeticiones")
        
        for i in range(len(repeticiones_por_calificacion)):
            print(f"{i + 1} | {repeticiones_por_calificacion[i]}")
        
        print()
        
def mostrar_mensajes_error(seleccion_usuario, estudiantes_cargados, promedios_calculados):
    if seleccion_usuario == 4 and promedios_calculados == False and estudiantes_cargados == True:
        print("Debe calcular los promedios primero para ingresar a esta opcion")
        
    else:
        print("Debe cargar datos de estudiantes antes de realizar otras acciones...\n")

