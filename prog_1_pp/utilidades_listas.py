""" 
Devuelve una matriz de las dimensiones objetivo con elemento pasado como base
filas: numero de filas
columnas: numero de columnas
elemento: elemento base para inicializar
"""
def generar_matriz_de_elemento(filas : int, columnas : int, elemento):
    matriz = [elemento] * filas
    
    for i in range(filas):
        matriz[i] = generar_array_de_elemento(columnas, elemento)
        
    return matriz


""" 
Devuelve una lista de la longitud objetivo inicializada con el elemento pedido
longitud: longitud de la lista a devolver
elemento: elemento base para inicializar
"""
def generar_array_de_elemento(longitud : int, elemento):
    array_elemento = [elemento] * longitud
    
    return array_elemento   


# Imprime la lista objetivo en pantalla a modo de menu
def imprimir_menu(opciones_menu):
    for i in range(len(opciones_menu)):
        print(opciones_menu[i])
        
      
# Obtiene indice de registro libre en la lista de estados
def obtener_indice_estado_vacio(estados):
    indice_libre = None
    
    for i in range(len(estados)):
        estado = estados[i]
        
        if estado == 0:
            indice_libre = i
            break
            
    return indice_libre


# Cuenta y devuelve la cantidad de estudiantes registrados (estados en 1)
def obtener_cantidad_estudiantes_registrados(estados):
    contador_estudiantes = 0
    
    for i in range(len(estados)):
        estado = estados[i]
        
        if estado == 1:
            contador_estudiantes += 1
            
    return contador_estudiantes
        
# Copia y ordena una lista usando algoritmo burbuja o bubble sort y la devuelve
def ordenar_estudiantes_por_promedio(calificaciones, nombres, legajos, generos, estados, promedios, ascendente = True):
    calificaciones_ordenadas = list(calificaciones)
    nombres_ordenados = list(nombres)
    legajos_ordenados = list(legajos)
    generos_ordenados= list(generos)
    estados_ordenados = list(estados)
    promedios_ordenados = list(promedios)

    for i in range(len(promedios_ordenados)):
        for j in range(0, len(promedios_ordenados) - 1 - i):
            
            if ascendente:
                if promedios_ordenados[j] > promedios_ordenados[j + 1]:
                    intercambiar_posiciones_lista(promedios_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(nombres_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(legajos_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(generos_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(calificaciones_ordenadas, j, j + 1)
                    intercambiar_posiciones_lista(estados_ordenados, j, j + 1)

            else:
                if promedios_ordenados[j] < promedios_ordenados[j + 1]:
                    intercambiar_posiciones_lista(promedios_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(nombres_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(legajos_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(generos_ordenados, j, j + 1)
                    intercambiar_posiciones_lista(calificaciones_ordenadas, j, j + 1)
                    intercambiar_posiciones_lista(estados_ordenados, j, j + 1)

    return calificaciones_ordenadas, nombres_ordenados, legajos_ordenados, generos_ordenados, estados_ordenados, promedios_ordenados

# Intercambia los elementos del indice_a y el indice_b de la lista objetivo
def intercambiar_posiciones_lista(lista, indice_a, indice_b):
    valor_auxiliar = lista[indice_a] 
                    
    lista[indice_a] = lista[indice_b]
    lista[indice_b] = valor_auxiliar
    
# Recorre columna dada por indice de materia y calcula el promedio
def calcular_promedio_materia(indice_materia, calificaciones, estados):
    total_calificaciones_materia = 0
    cantidad_calificaciones = 0
    promedio_materia = 0
    
    for i in range(len(calificaciones)):
        
        if estados[i] == 1: # hay notas cargadas
            calificacion_materia = calificaciones[i][indice_materia]
            total_calificaciones_materia += calificacion_materia
            cantidad_calificaciones += 1
            
    if cantidad_calificaciones != 0:
        promedio_materia = total_calificaciones_materia / cantidad_calificaciones
    
    return promedio_materia

# Recorre todas las columnas de calificaciones, devolviendo una lista de promedios por cada una de ellas
def calcular_promedios_materias(calificaciones, estados):
    promedios_materias = [0.0] * len(calificaciones[0])
    
    for i in range(len(calificaciones[0])):
        promedio_materia = calcular_promedio_materia(i, calificaciones, estados)
        
        promedios_materias[i] = promedio_materia
        
    return promedios_materias
        
# Compara y obtiene el promedio mas alto entre las materias
def obtener_promedio_materia_mas_alto(calificaciones, estados):
    promedios_materias = calcular_promedios_materias(calificaciones, estados)
    promedio_mas_alto = 0.0
    
    for i in range(len(promedios_materias)):
        promedio = promedios_materias[i]
        
        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            
    return promedio_mas_alto


# Busca en la lista de legajos el legajo objetivo y devuelve su indice
def obtener_indice_legajo(legajo, legajos, estados):
    indice_legajo = None
    
    for i in range(len(estados)):
        estado = estados[i]
        
        if estado == 1:
            if legajo == legajos[i]:
                indice_legajo = i
                break
    
    if indice_legajo == None:
        print("No se encontro legajo en los registros de estudiantes")
        
    return indice_legajo
    
    
# Cuenta y devuelve la cantidad de aparicicones por nota idividual en una materia
def obtener_repeticiones_notas_materia(indice_materia, calificaciones, estados):
    repeticiones_por_calificacion = [0] * 10
    
    for calificacion in range(1, 11):
        cantidad_repeticiones = 0
            
        for i in range(len(calificaciones)):
            
            if estados[i] == 1: # hay notas cargadas
                calificacion_materia = calificaciones[i][indice_materia]
                
                if calificacion_materia == calificacion:
                    cantidad_repeticiones += 1
                    
        repeticiones_por_calificacion[calificacion - 1] = cantidad_repeticiones
    
    return repeticiones_por_calificacion