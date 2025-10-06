# Ejercicio 1
# Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero):
    if numero == 9:
        return numero
    suma = numero + sumar_naturales(numero + 1)
    return suma
    
    
print(str(sumar_naturales(1)))

# Ejercicio 2
# Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base, exponente):
    if exponente == 1:
        return base

    resultado = base * calcular_potencia(base, exponente - 1)
    return resultado

print(calcular_potencia(2, 2))

print(calcular_potencia(2, 3))

print(calcular_potencia(3, 3))

# Ejercicio 3
# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero):
    numero_string = str(numero)
    cantidad_digitos = len(numero_string)
    if cantidad_digitos == 1:
        return numero
    
    numero_recortado = int(numero_string[0 : cantidad_digitos - 1])
    
    suma_digitos = int(numero_string[cantidad_digitos - 1]) + sumar_digitos(numero_recortado)
    
    return suma_digitos

print(sumar_digitos(45))
print(sumar_digitos(128))
print(sumar_digitos(902))

# Ejercicio 4
# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero):
    resultado_fibonacci = None
    if numero < 1:
        resultado_fibonacci = 0
    elif numero == 1:
        resultado_fibonacci = 1
    else:
        resultado_fibonacci = calcular_fibonacci(numero - 2) + calcular_fibonacci(numero - 1)
        
    return resultado_fibonacci

print(calcular_fibonacci(4))
# print(calcular_fibonacci(5))
# print(calcular_fibonacci(6))
# print(calcular_fibonacci(7))
# print(calcular_fibonacci(8))
# print(calcular_fibonacci(9))
        