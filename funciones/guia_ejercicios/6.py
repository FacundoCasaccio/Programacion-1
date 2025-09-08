# Ejercicio 6
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par(numero):
    if numero % 2 == 0: print(f"El numero {numero} es par")
    else: print(f"El numero {numero} es impar")

es_par(2)
es_par(3)