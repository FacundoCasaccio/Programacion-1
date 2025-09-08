# Ejercicio 12
"""
Crear una función que imprima la tabla de multiplicar 
de un número recibido como parámetro. La función debe aceptar 
parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
Por defecto es del 1 al 10.
"""

def solicitar_numero_tabla():
    return int(input("Ingrese un numero para ver su tabla de multiplicar: "))

def tabla_de_multiplicar(numero, inicio = 1, fin = 10):
    for i in range(inicio, fin + 1):
        print(f"{numero} * {i} = {numero * i}")

tabla_de_multiplicar(solicitar_numero_tabla())
tabla_de_multiplicar(solicitar_numero_tabla(), 1, 20)