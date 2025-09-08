# Ejercicio 11
""" 
Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
"""
from ..for_ejercicios.ejercicios import *

def ejecutar_ejercicio():
    numero = int(input("Ingrese un numero: "))

    print(f"La cantidad de numeros primos encontrados es {primos_hasta_numero(numero)}")


ejecutar_ejercicio()