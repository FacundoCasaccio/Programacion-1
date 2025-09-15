from operation_tools.especificas import *

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
    