from operation_tools.arrays_generales import *
from menu_tools.menu_utils import print_menu
import random

opciones_menu = [
    "1 - Ingreso de la matriz",
    "2 - Verificar la existencia de secuencias de números consecutivos pares",
    "3 - Determinar la cantidad de ocurrencias",
    "4 - Identificar la secuencia más corta",
    "5 - Identificar la secuencia más larga",
    "6 - Salir del programa\n\n",
]

filas_matriz = random.randint(2, 10)
columnas_matriz = random.randint(2, 10)
matriz = []

def verificar_secuencias_encontradas(secuencias_encontradas):
    existe_secuencia = False
    for i in range(len(secuencias_encontradas)):
        if len(secuencias_encontradas[i]) > 0:
            existe_secuencia = True
            break
    
    if existe_secuencia:
        print("EXISTEN NÚMEROS CONSECUTIVOS PARES")
    else:
        print("NO EXISTEN NÚMEROS CONSECUTIVOS PARES")
        
    return existe_secuencia
            
def contar_secuencias_pares_existentes(secuencias_encontradas):
    existe_secuencia = verificar_secuencias_encontradas(secuencias_encontradas)
    cantidad_secuencias = 0
    
    if existe_secuencia:

        for i in range(len(secuencias_encontradas)):
            if len(secuencias_encontradas[i]) > 0:
                cantidad_secuencias += 1
    
    print(f"Se encontraron {cantidad_secuencias} secuencias de consecutivos pares")
    
def obtener_secuencia_mas_corta(secuencias_encontradas):
    existe_secuencia = verificar_secuencias_encontradas(secuencias_encontradas)
    secuencia_mas_corta = []
    
    if existe_secuencia:

        for i in range(len(secuencias_encontradas)):
            secuencia_actual = secuencias_encontradas[i]
            
            if len(secuencia_actual) < len(secuencia_mas_corta) or len(secuencia_mas_corta) == 0:
                secuencia_mas_corta = secuencia_actual
                
    else:
        print("No hay secuencias pares consecutivas")
        
    
    return secuencia_mas_corta
    

def obtener_secuencia_mas_larga(secuencias_encontradas):
    existe_secuencia = verificar_secuencias_encontradas(secuencias_encontradas)
    secuencia_mas_larga = []
    
    if existe_secuencia:

        for i in range(len(secuencias_encontradas)):
            secuencia_actual = secuencias_encontradas[i]
            
            if len(secuencia_actual) > len(secuencia_mas_larga):
                secuencia_mas_larga = secuencia_actual
                
    else:
        print("No hay secuencias pares consecutivas")
        
    
    return secuencia_mas_larga

def buscar_secuencias_pares_consecutivos(matriz):
    secuencias_encontradas = []
    
    for i in range(len(matriz)):
        secuencia_actual = []
        
        for j in range(len(matriz[i])):
            numero = matriz[i][j]
            
            if numero % 2 == 0:
                secuencia_actual.append(numero)

            elif numero % 2 != 0:
                
                if len(secuencia_actual) > 1:
                    secuencias_encontradas.append(secuencia_actual)
                
                secuencia_actual = []
            
            if j == len(matriz[i]) - 1 and len(secuencia_actual) > 1:
                secuencias_encontradas.append(secuencia_actual)
    
    return secuencias_encontradas


imprimir_matriz(matriz)

longitud_secuencias = filas_matriz * columnas_matriz
print("############")
secuencias_encontradas = []
listar_elementos(secuencias_encontradas)

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
            matriz = generar_matriz_int_aleatoria(filas = filas_matriz,
                            columnas = columnas_matriz,
                            minimo = 1,
                            maximo = 99)
            secuencias_encontradas = buscar_secuencias_pares_consecutivos(matriz)
        
        case 2:
            verificar_secuencias_encontradas(secuencias_encontradas)
        
        case 3:
            contar_secuencias_pares_existentes(secuencias_encontradas)
        
        case 4:
            secuencia_mas_corta = obtener_secuencia_mas_corta(secuencias_encontradas)
            listar_elementos(secuencia_mas_corta)
        
        case 5:
            secuencia_mas_larga = obtener_secuencia_mas_larga(secuencias_encontradas)
            listar_elementos(secuencia_mas_larga)
    