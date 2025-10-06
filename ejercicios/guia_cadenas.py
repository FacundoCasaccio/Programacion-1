from operation_tools.arrays_generales import *
from operation_tools.string_utils import *

"""
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). 
La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ejemplo, si la cadena ingresada es “murcielaguito”, la salada por pantalla deberá ser: (“a”: 1; “e”: 1; “i”: 2; “o”: 1; “u”:2)
"""
cadena = "murcielaguito"

listar_elementos(contar_vocales_individuales(cadena))


"""
Crear una función que reciba una cadena y un caracter. 
La función deberá devolver el índice en el que se encuentre la primera 
ocurrencia de dicho caracter, o -1 en caso de que no esté.
"""
cadena_2 = "catamplimba"

print(devolver_indice_caracter("b", cadena_2))
print(devolver_indice_caracter("z", cadena_2))


"""
Crear una función que reciba como parámetro una cadena y determine 
si la misma es o no un palíndromo. 
Deberá retornar un valor booleano indicando lo sucedido.
"""
cadena_caracter = "facu"

print(invertir_cadena(cadena_caracter))

no_palindromo = "facu"
palindromo = "anilina"

print(verificar_palindromo(no_palindromo))
print(verificar_palindromo(palindromo))


"""
Crear una función que reciba como parámetro una cadena 
y suprima los caracteres repetidos consecutivos.
"""
cadena_repetida = "Hoooolaa"
print(eliminar_repetidos_consecutivos(cadena_repetida))

"""
Crear una función que reciba una cadena por parámetro 
y suprima las vocales de la misma.
"""   
print(suprimir_vocales(cadena_repetida))


"""
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
"""
cadena_analizar = "El pan del panadero"

print(str(contar_subcadena(cadena_analizar, "pan")))