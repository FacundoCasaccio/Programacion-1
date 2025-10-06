from operation_tools.string_utils import *

cadena = input("Ingrese una cadena de caracteres: ")
cadena_minuscula = normalizar_cadena(cadena, minuscula = True)
cadena_mayuscula = normalizar_cadena(cadena, minuscula = False)

print()

print("Normalizada a minuscula")
print(cadena_minuscula)

print()

print("Normalizada a mayuscula")
print(cadena_mayuscula)
        
    