# Ejercicio 11
""" 
Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
"""

def solicitar_numero():
    return int(input("Ingrese un numero para encontrar todos los primos entre el 1 y el numero ingresado: "))

def calcular_divisores(numero_objetivo):
    acumulador_divisores = 0

    for j in range(1, numero_objetivo + 1):
        if numero_objetivo % j == 0:
            acumulador_divisores += 1
    
    return acumulador_divisores

def determinar_par(numero, divisores):
    if(divisores <= 2):
        print(f"El numero {numero} es un numero primo")
        
def numeros_primos_hasta():

    numero_objetivo = solicitar_numero()
    acumulador_divisores = 0

    for i in range(1, numero_objetivo + 1):
        acumulador_divisores = calcular_divisores(i)

        determinar_par(i, acumulador_divisores)

    return acumulador_divisores

print(f"La cantidad de divisores es: {numeros_primos_hasta()}")