# Ejercicio 1
# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(longitud):
    array = []
    for i in range(longitud):
        array.append(i)
    return array

# print(crear_array(8))

# Ejercicio 2
# Escribir una función que permita ingresar la cantidad 
# de números que reciba como parámetro.  Crear el array con la función del punto 1.
def cargar_array(longitud):
    array = crear_array(longitud)
    
    for i in range(len(array)):
        array[i] = int(input("Ingrese un numero: "))
    
    return array

# lista_numeros_cargados = cargar_array(8)
# print(lista_numeros_cargados)

# Ejercicio 3
# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def promedio_enteros(lista_enteros):
    suma_enteros = 0
    for numero in lista_enteros:
        suma_enteros += numero
    promedio = suma_enteros / len(lista_enteros)
    
    return promedio

# print(promedio_enteros([4, 2, 5, 7]))

# Ejercicio 4
# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def promedio_enteros_positivos(lista_enteros):
    suma_enteros_positivos = 0
    contador_positivos = 0
    for numero in lista_enteros:
        if numero > 0:
            suma_enteros_positivos += numero
            contador_positivos += 1
            
    if contador_positivos > 0:
        promedio_positivos = suma_enteros_positivos / contador_positivos
    else:
        promedio_positivos = 0
    
    return promedio_positivos

# print(promedio_enteros_positivos([4, 2, -2, -7]))

# Ejercicio 5
# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def producto_elementos(lista_elementos):
    producto_elementos = 0
    for i in range(len(lista_elementos)):
        elemento = lista_elementos[i]
        if type(elemento) == float or type(elemento) == int:
            if i == 0:
                producto_elementos = elemento
            else:
                producto_elementos *= elemento
    
    return producto_elementos

# print(producto_elementos([4, 3, 1, -1]))

# Ejercicio 6
# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def retornar_indice_maximo(lista_enteros):
    numero_maximo = None
    indice_maximo = None
    
    for i in range(len(lista_enteros)):
        numero = lista_enteros[i]
        if i == 0:
            numero_maximo = numero
            indice_maximo = i
        else:
            if numero > numero_maximo:
                numero_maximo = numero
                indice_maximo = i
    return indice_maximo
    
lista = [4, 8, 5, -1]
print(retornar_indice_maximo(lista))
print(lista[retornar_indice_maximo(lista)]) # type: ignore

# Ejercicio 7
# Escribir una función que reciba como parámetros una lista de enteros y 
# muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def indices_maximos(lista_enteros):
    numero_maximo = None
    indices_maximos = []
    
    for i in range(len(lista_enteros)):
        numero = lista_enteros[i]
        if i == 0:
            numero_maximo = numero
            indices_maximos = [i]
        else:
            if numero > numero_maximo:
                numero_maximo = numero
                indices_maximos = [i]
            elif numero == numero_maximo:
                indices_maximos.append(i)
    return indices_maximos

# print(indices_maximos([4, 3, 5, -1, 5]))

# Ejercicio 8
"""
Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
Una lista de nombres (lista_nombres).
Un nombre a buscar en la lista (nombre_antiguo).
Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
"""

def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    cantidad_reemplazos = 0
    
    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        if nombre == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            cantidad_reemplazos += 1
    
    return cantidad_reemplazos

# lista_nombres = ["Juan", "Pepe", "Eugenio", "Juan"]
# print(lista_nombres)
# print(reemplazar_nombres(lista_nombres, "Juan", "Ricardo"))
# print(lista_nombres)

# Ejercicio 9
# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

def interseccion_arrays(array_a, array_b):
    interseccion_a_b = []
    
    for i in range(len(array_a)):
        elemento_a = array_a[i]
        
        for j in range(len(array_b)):
            elemento_b = array_b[j]
            
            if elemento_a == elemento_b:
                interseccion_a_b.append(elemento_b)
                
    return interseccion_a_b

# array_a = ["a", "c", "b"]
# array_b = ["g", "l", "b", "e"]

# print(interseccion_arrays(array_a, array_b))

# Ejercicio 10
# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

def union_arrays(array_a, array_b):
    union_a_b = list(array_a)
    
    for i in range(len(array_b)):
        elemento_b = array_b[i]
        repetido_en_a = False
        
        for j in range(len(array_a)):
            elemento_a = array_a[j]
            
            if elemento_a == elemento_b:
                repetido_en_a = True
        
        if repetido_en_a == False:
            union_a_b.append(elemento_b)
    
    return union_a_b

# array_a = ["a", "c", "b"]
# array_b = ["g", "l", "b", "e", "a"]

# print(union_arrays(array_a, array_b))

# Ejercicio 11
# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.

def diferencia_arrays(array_a, array_b):
    diferencia_a_b = list(array_a)
    
    for i in range(len(array_b)):
        elemento_b = array_b[i]
        repetido_en_a = False
        
        for j in range(len(array_a)):
            elemento_a = array_a[j]
            
            if elemento_a == elemento_b:
                repetido_en_a = True
        
        if repetido_en_a == True:
            diferencia_a_b.remove(elemento_b)
    
    return diferencia_a_b

# array_a = ["a", "c", "b"]
# array_b = ["g", "l", "b", "e"]


# print(diferencia_arrays(array_b, array_a))
# print(diferencia_arrays(array_a, array_b))