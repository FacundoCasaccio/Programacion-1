# Ejercicio 7
# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par_bool(numero):
    if numero % 2 == 0: return True
    else: return False

print(es_par_bool(2))
print(es_par_bool(3))