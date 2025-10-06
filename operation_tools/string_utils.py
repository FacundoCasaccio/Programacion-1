from validation_tools.validate import *

def normalizar_cadena(cadena, minuscula = True):
    cadena_normalizada = ""
    
    if minuscula:
        for i in range(len(cadena)):
            caracter = cadena[i]
            codigo_caracter = ord(caracter)
            
            if verificar_mayuscula(caracter):
                cadena_normalizada += chr(codigo_caracter + 32)
            else:
                cadena_normalizada += caracter
                
    else:
        for i in range(len(cadena)):
            caracter = cadena[i]
            codigo_caracter = ord(caracter)
            
            if verificar_minuscula(caracter):
                cadena_normalizada += chr(codigo_caracter - 32)
            else:
                cadena_normalizada += caracter
                
    return cadena_normalizada

def contar_vocales_individuales(cadena_a_contar):
    matriz_vocales = [
        ["a", 0],
        ["e", 0],
        ["i", 0],
        ["o", 0],
        ["u", 0],
    ]
    
    for i in range(len(cadena_a_contar)):
        caracter = cadena_a_contar[i]
        
        if caracter == "A" or caracter == "a":
            matriz_vocales[0][1] += 1
            
        if caracter == "E" or caracter == "e":
            matriz_vocales[1][1] += 1
            
        if caracter == "I" or caracter == "i":
            matriz_vocales[2][1] += 1
            
        if caracter == "O" or caracter == "o":
            matriz_vocales[3][1] += 1
        
        if caracter == "U" or caracter == "u":
            matriz_vocales[4][1] += 1
            
    return matriz_vocales

def devolver_indice_caracter(caracter_objetivo, cadena):
    indice_caracter = -1
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if caracter_objetivo == caracter:
            indice_caracter = i
            break
        
    return indice_caracter

def invertir_cadena(cadena):
    cadena_nueva = ""
    
    for i in range(len(cadena) - 1, -1, -1):
        caracter = cadena[i]
        
        cadena_nueva += caracter
        
    return cadena_nueva

def verificar_palindromo(cadena):
    es_palindromo = False
    cadena_invertida = invertir_cadena(cadena)
    
    if cadena == cadena_invertida:
        es_palindromo = True
        
    return es_palindromo

def eliminar_repetidos_consecutivos(cadena):
    nueva_cadena = ""
    ultimo_caracter = None
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if caracter != ultimo_caracter:
            nueva_cadena += caracter
            
        ultimo_caracter = caracter
        
    return nueva_cadena

def verificar_vocal(caracter):
    es_vocal = False
    
    if caracter == "A" or caracter == "a":
        es_vocal = True
        
    if caracter == "E" or caracter == "e":
        es_vocal = True
        
    if caracter == "I" or caracter == "i":
        es_vocal = True
        
    if caracter == "O" or caracter == "o":
        es_vocal = True
    
    if caracter == "U" or caracter == "u":
        es_vocal = True
        
    return es_vocal

def suprimir_vocales(cadena):
    nueva_cadena = ""
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if verificar_vocal(caracter) == False:
            nueva_cadena += caracter
            
    return nueva_cadena

def contar_subcadena(cadena, subcadena):
    apariciones = 0
    
    for i in range(len(cadena)):
        
        if i + len(subcadena) < len(cadena):
            subcadena_comparar = cadena[slice(i, i + len(subcadena))]
            
            if subcadena == subcadena_comparar:
                apariciones += 1
                
    return apariciones