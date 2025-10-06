# Ejercicio 1
# Mostrar los números ascendentes desde el 1 al 10
for numero in range(0, 10):
    print(numero + 1)
    
# Ejercicio 2
# Mostrar los números descendentes desde el 10 al 1
for numero in range(10, 0, -1):
    print(numero)


# Ejercicio 3
# Ingresar un número. Mostrar los números desde 0 hasta el n0úmero ingresado.
numero_objetivo = int(input("Ingrese un numero:\n"))
print("\n")
if numero_objetivo >= 0:
    paso = 1
else:
    paso = -1

for numero in range(0, numero_objetivo, paso):
    print(numero)
print(numero_objetivo)

# Ejercicio 4
# Ingresar un número y mostrar la tabla de multiplicar de ese número.
numero_objetivo = int(input("Ingrese un numero para saber su tabla de multiplicar:\n"))

for numero in range(0, 11):
    print(f"{numero_objetivo} * {numero} = {numero_objetivo * numero}")

# Ejercicio 5
# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
acumulador_suma_numeros = 0
numeros_ingresados = 0

for ciclo in range(10):
    numero = int(input("Ingrese un numero (0 para finalizar): "))

    if numero == 0: break

    acumulador_suma_numeros += numero
    numeros_ingresados = ciclo + 1

print(f"El promedio de los numeros ingresados es: {acumulador_suma_numeros / numeros_ingresados}")

# Ejercicio 6
# Imprimir los números múltiplos de 3 entre el 1 y el 10.
for numero in range(1, 11):
    if numero % 3 == 0:
        print(numero)

# Ejercicio 7
# Mostrar los números pares que hay desde la unidad hasta el número 50.
for numero in range(0, 50):
    if (numero + 1) % 2 == 0:
        print(numero + 1)

# Ejercicio 8
# Realizar un programa que permita mostrar una pirámide de números
# https://onlinegdb.com/NkadN3Zfi GDB con tabulado
base_piramide = int(input("Ingrese un numero para construir su piramide: "))

for i in range(0, base_piramide):
    fila_piramide = ""
    for j in range(0, i + 1):
        fila_piramide += str(j + 1)

    print(fila_piramide)

# Ejercicio 9
# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
acumulador_divisores = 0
numero_objetivo = int(input("Ingrese un numero: "))

for numero in range(1, numero_objetivo + 1):
    if numero_objetivo % numero == 0:
        print(f"{numero} es divisor de {numero_objetivo}")
        acumulador_divisores += 1

print(f"Se encontraron {acumulador_divisores} divisores para {numero_objetivo}")

# Ejercicio 10
# Ingresar un número. Determinar si el número es primo o no.
numero_objetivo = int(input("Ingrese un numero para evaluar si es primo: "))
acumulador_divisores = 0
for numero in range(1, numero_objetivo + 1):
    if numero_objetivo % numero == 0:
        acumulador_divisores += 1

if(acumulador_divisores > 2):
    print(f"El numero {numero_objetivo} NO es un numero primo")
else:
    print(f"El numero {numero_objetivo} SI es un numero primo")

# Ejercicio 11
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero_objetivo = int(input("Ingrese un numero para encontrar todos los primos entre el 1 y el numero ingresado: "))

def primos_hasta_numero(numero_objetivo):
    contador_primos = 0
    for i in range(1, numero_objetivo + 1):
        acumulador_divisores = 0

        for j in range(1, i + 1):
            if i % j == 0:
                acumulador_divisores += 1

        if(acumulador_divisores <= 2):
            print(f"El numero {i} es un numero primo")
            contador_primos += 1
    
    return contador_primos