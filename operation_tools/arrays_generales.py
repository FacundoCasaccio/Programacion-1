from operation_tools.especificas import *
from input_tools.inputs import get_int
import random

def contar_positivos(lista_numeros):
    cantidad_positivos = 0
    
    for i in range(len(lista_numeros)):
        numero = lista_numeros[i]
        if determinar_numero_positivo(numero) == True and numero != 0:
            cantidad_positivos += 1
            
    return cantidad_positivos

def contar_negativos(lista_numeros):
    cantidad_negativos = 0
    
    for i in range(len(lista_numeros)):
        numero = lista_numeros[i]
        if determinar_numero_positivo(numero) == False and numero != 0:
            cantidad_negativos += 1
            
    return cantidad_negativos

def sumar_pares(lista_numeros):
    suma_pares = 0
    
    for i in range(len(lista_numeros)):
        numero = lista_numeros[i]
        
        if determinar_numero_par(numero):
            suma_pares += numero
            
    return suma_pares

def determinar_mayor_impar(lista_numeros):
    mayor_impar = None
    
    for i in range(len(lista_numeros)):
        numero = lista_numeros[i]
        
        if determinar_numero_par(numero) == False:
            if mayor_impar == None or numero > mayor_impar:
                mayor_impar = numero
    
    return mayor_impar

def listar_elementos(lista_elementos):
    string_elementos = ""
    for i in range(len(lista_elementos)):
        elemento_str = str(lista_elementos[i])
        
        string_elementos += elemento_str + ", "
        
    print(string_elementos)
    
def listar_pares(lista_numeros):
    string_numeros = ""
    for i in range(len(lista_numeros)):
        numero = lista_numeros[i]
        
        if numero % 2 == 0:
            string_numeros += str(numero) + ", "
        
    print(string_numeros)
    
def listar_posiciones_impares(lista_elementos):
    string_elementos = ""
    for i in range(len(lista_elementos)):
        elemento = lista_elementos[i]
        
        if i % 2 != 0:
            string_elementos += str(elemento) + ", "
        
    print(string_elementos)
    
def obtener_elementos_en_comun(listas_a_comparar):
    elementos_iguales = []
    
    # Lista base para comparar
    # Si un elemento esta en TODAS, tiene que estar en la primera
    lista_a = listas_a_comparar[0]
    
    # Empieza a partir de la segunda, asumiendo que siempre len >= 1
    for i in range(1, len(listas_a_comparar)):
        lista_b = listas_a_comparar[i]
            
        # Compara de a dos listas y agrego a los elementos encontrados
        for j in range(len(lista_a)):
            for k in range (len(lista_b)):
                # Si son iguales y no esta ya en la lista
                if lista_a[j] == lista_b[k] and elementos_iguales.count(lista_a[j]) == 0:
                    elementos_iguales.append(lista_a[j])
                        
    return elementos_iguales

def obtener_elementos_exclusivos(listas_a_comparar):
    lista_todos_elementos = []
    lista_elemnentos_exclusivos = []
    
    # Juntar todos los elementos en una lista mas grande
    for i in range(len(listas_a_comparar)):
        lista_actual = listas_a_comparar[i]
        for j in range(len(lista_actual)):
            lista_todos_elementos.append(lista_actual[j])
           
    # Comparar entre ellos y contar apariciones 
    for i in range(len(lista_todos_elementos)):
        elemento_a = lista_todos_elementos[i]
        contador_repeticiones = 0
        
        for j in range(len(lista_todos_elementos)):
            elemento_b = lista_todos_elementos[j]
            
            if elemento_a == elemento_b:
                contador_repeticiones += 1
                
        if contador_repeticiones == 1:
            lista_elemnentos_exclusivos.append(elemento_a)
            
    return lista_elemnentos_exclusivos

def juntar_listas_sin_repetidos(listas_a_comparar):
    lista_todos_elementos = []
    
    # Juntar todos los elementos en una lista mas grande
    for i in range(len(listas_a_comparar)):
        lista_actual = listas_a_comparar[i]
        for j in range(len(lista_actual)):
            if lista_todos_elementos.count(lista_actual[j]) == 0:
                lista_todos_elementos.append(lista_actual[j]) # Evitar repetidos
                
    return lista_todos_elementos

def juntar_listas(listas_a_comparar):
    lista_todos_elementos = []
    
    # Juntar todos los elementos en una lista mas grande
    for i in range(len(listas_a_comparar)):
        lista_actual = listas_a_comparar[i]
        for j in range(len(lista_actual)):
            lista_todos_elementos.append(lista_actual[j]) # Evitar repetidos
                
    return lista_todos_elementos

def obtener_elemento_mas_apariciones(lista_elementos):
    elemento_mas_repetido = 0
    repeticiones_maximas = 0
        
    for i in range(len(lista_elementos)):
        elemento = lista_elementos[i]
        
        if lista_elementos.count(elemento) > repeticiones_maximas:
            elemento_mas_repetido = elemento
        elif lista_elementos.count(elemento) == repeticiones_maximas:
            elemento_mas_repetido = list(elemento_mas_repetido).append(elemento)
            
    return elemento_mas_repetido
           
def recomendar_productos(listas_de_compras):
    elementos_en_comun = obtener_elementos_en_comun(listas_de_compras)
    elementos_exclusivos = obtener_elementos_exclusivos(listas_de_compras)
    catalogo_completo = juntar_listas_sin_repetidos(listas_de_compras)
    compras_totales = juntar_listas(listas_de_compras)
    elemento_mas_apariciones = obtener_elemento_mas_apariciones(compras_totales)
    
    print("En base a las listas de compras proporcionadas: \n")
    print("Los productos que se han estado comprando los clientes son")
    listar_elementos(catalogo_completo)
    print()
    print("Los productos que todos los clientes compran")
    listar_elementos(elementos_en_comun)
    print()
    print(f"El/los productos mas comprados: {elemento_mas_apariciones}")
    print()
    print("Los productos que solo algunos llevan son:")
    listar_elementos(elementos_exclusivos)
    
"""
Hacer una funcion que reciba como parametros un vector y un dato a buscar (int), 
y la misma retorne el indice del elemento encontrado.
En caso de no encontrarse, retornar el valor -1
"""    
def retornar_indice_elemento(lista: list, dato_a_buscar: int) -> int :
    indice_elemento = -1 # Inicializado en el caso de no haberlo encontrado
    
    for i in range(len(lista)):
        if lista[i] == dato_a_buscar:
            indice_elemento = i # Cambiar a indice del elemento si se ecneutnra
            break # cortar ejecucion debido a que se encontro
    
    return indice_elemento

"""
Hacer una funcion que carge de manera secuencial diez elementos numericos
Hacer una funcion que cargue de manera aleatoria 10 elementos
int
"""
def cargar_secuencialmente(cant_elementos = 10):
    lista = [None] * cant_elementos
    
    for i in range(len(lista)):
        elemento_a_cargar = input("Ingrese algo: ")
        lista[i] = elemento_a_cargar
    
    return lista

def cargar_aleatoriamente(cant_elementos):
    lista = [None] * cant_elementos
    
    for _ in range(len(lista)):
        elemento_a_cargar = input("Ingrese algo: ")
        cargar_elemento_indice_aleatorio(elemento_a_cargar, lista)
        # print(lista)
        
    return lista
        
def cargar_elemento_indice_aleatorio(elemento, lista):
    indice = random.randint(0, len(lista) - 1)
    
    if lista[indice] == None:
        lista[indice] = elemento
    else:
        cargar_elemento_indice_aleatorio(elemento, lista)
        
def generar_array_ceros(longitud):
    array_ceros = [0] * longitud
    
    return array_ceros

def cargar_datos(estado, datos, mensaje):
    
    for i in range(len(datos)):
        if estado[i] == 0:
            estado[i] = 1
            datos[i] = input(mensaje)
            break
        else:
            continue
        
def cargar_datos_int(estado, datos, mensaje):
    
    for i in range(len(datos)):
        if estado[i] == 0:
            estado[i] = 1
            datos[i] = get_int(mensaje, "Dato incorrecto, ingrese nuevamente", 0, 10, 99)
            break
        else:
            continue
        
"""
Hacer una app utilizando la biblioteca propia de vectores, 
que realice una carga al estilo agenda de contactos del celular. 
Para esto, desarrollar una funcion que reciba dos vectores, 
estados y datos, y que realice la carga en datos, si hay espacio libre.
"""

def cargar_arrays_mixto(longitud, mensaje):
    lista_estado = generar_array_ceros(longitud)
    lista_datos = generar_array_ceros(longitud)
    contador = 0
    respuesta_continuar = "S"
    continuar = True
    

    while continuar:
        if contador > 0 and contador < len(lista_datos):
            respuesta_continuar = input("Desea continuar? [S/N]: ")
            
        if respuesta_continuar == "S" and contador <= len(lista_datos):
            cargar_datos_int(lista_estado, lista_datos, mensaje)
            contador += 1
        elif respuesta_continuar == "N" or contador >= len(lista_datos):
            break
    
    return lista_datos

def cargar_notas(estudiantes, cantidad_notas, mensaje):
    notas = [0] * len(estudiantes)
    
    for i in range(len(estudiantes)):
        print(f"Estudiante: {estudiantes[i]}")
        notas_estudiante = cargar_arrays_mixto(cantidad_notas, mensaje)
        notas[i] = notas_estudiante
        
    return notas

def calcular_promedios(notas):
    promedios = [0] * len(notas)
    
    for i in range(len(notas)):
        notas_estudiante = notas[i]
        suma_notas_estudiante = 0
        for j in range(len(notas_estudiante)):
            suma_notas_estudiante += notas_estudiante[j]
            
        promedio_estudiante = suma_notas_estudiante / len(notas_estudiante)
        promedios[i] = promedio_estudiante
    
    return promedios

def mostrar_datos_academicos_estudiantes(estudiantes, notas, promedios):
    print("Datos academicos de los estudiantes\n")
    
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]}, promedio {promedios[i]}")
        print("Notas: ")
        listar_elementos(notas[i])
        print()
