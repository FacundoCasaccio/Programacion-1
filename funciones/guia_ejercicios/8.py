# Ejercicio 8
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def mayor_numero(numero_a, numero_b, numero_c):
    numero_mayor = numero_a

    if (numero_b > numero_mayor): numero_mayor = numero_b
    if (numero_c > numero_mayor): numero_mayor = numero_c

    return numero_mayor

print(mayor_numero(1, 2, 3))
print(mayor_numero(4, 1, 0))
print(mayor_numero(-1, 28, 3))