# Ejercicio 10
# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def numero_primo(numero_objetivo):
    acumulador_divisores = 0

    for numero in range(1, numero_objetivo + 1):
        if numero_objetivo % numero == 0:
            acumulador_divisores += 1

    if(acumulador_divisores > 2):
        return False
    else:
        return True
    
print(numero_primo(3))
print(numero_primo(10))
print(numero_primo(23))
print(numero_primo(24))