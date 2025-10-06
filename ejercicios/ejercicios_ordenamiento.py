# from operation_tools.arrays_generales import *

def ordenar_array(array, ascendente = True):
    
    for i in range(len(array)):
        for j in range(0, len(array) - 1 - i):
            
            if ascendente:
                if array[j] > array[j + 1]:
                    valor_menor = array[j] 
                    
                    array[j] = array[j + 1]
                    array[j + 1] = valor_menor
                    
            else:
                if array[j] < array[j + 1]:
                    valor_menor = array[j] 
                    
                    array[j] = array[j + 1]
                    array[j + 1] = valor_menor

    return array

array = [15, 23213, 9, 10, 1, 231, 1, 2]

print(array)
ordenar_array(array, ascendente = False)
print(array)

# listar_elementos(array)
# ordenar_array(array)
# listar_elementos(array)
# ordenar_array(array, ascendente = False)
# listar_elementos(array)


# def intercalar_vectores(vector_a, vector_b, ascendente = True):
#     nuevo_vector = vector_a + vector_b
#     ordenar_array(nuevo_vector, ascendente)
    
#     listar_elementos(nuevo_vector)    
#     # Forma mas rustica para ir "intercalando"
#     # ordenar_array(vector_a)
#     # ordenar_array(vector_b)

#     # nuevo_vector = [0] * (len(vector_a) + len(vector_b))
    
#     # indice_a, indice_b = 0, 0
    
#     # for i in range(len(nuevo_vector)):
        
#     #     if indice_a < len(vector_a) and indice_b < len(vector_b):
            
#     #         if vector_a[indice_a] <= vector_b[indice_b]:
#     #             nuevo_vector[i] = vector_a[indice_a]
#     #             indice_a += 1
#     #         else:
#     #             nuevo_vector[i] = vector_b[indice_b]
#     #             indice_b += 1
                
#     #     elif indice_a >= len(vector_a):
#     #         for j in range(indice_b, len(vector_b)):
#     #             nuevo_vector[i] = vector_b[j]
                
#     #     elif indice_b >= len(vector_b):
#     #         for j in range(indice_a, len(vector_a)):
#     #             nuevo_vector[i] = vector_a[j]
                
                
#     # if ascendente:
#     #     listar_elementos(nuevo_vector)
#     # else:
#     #     ordenar_array(nuevo_vector, ascendente = False)
#     #     listar_elementos(nuevo_vector)
                    
#     return nuevo_vector
    
    
# # vector_a = [4, 83, 1, 9, 24, 823, 2]
# # vector_b = [99, 1, 2131, 7, 42, 1]

# # intercalar_vectores(vector_a, vector_b, False)

# vector_c = [-231, 7, -1241, -2, 14, 99, -32]

# def ordernar_negativos_positivos(vector_a_ordenar):
    
#     ordenar_array(vector_a_ordenar)
    
#     for i in range(len(vector_a_ordenar)):
#         for j in range(0, len(vector_a_ordenar) - 1 - i):
            
#             if vector_a_ordenar[j] < 0 and vector_a_ordenar[j + 1] < 0:
#                 if vector_a_ordenar[j] < vector_a_ordenar[j + 1]:
#                     valor_menor = vector_a_ordenar[j] 
                    
#                     vector_a_ordenar[j] = vector_a_ordenar[j + 1]
#                     vector_a_ordenar[j + 1] = valor_menor
                    
#             if vector_a_ordenar[j] >= 0 and vector_a_ordenar[j + 1] >= 0:
#                 if vector_a_ordenar[j] > vector_a_ordenar[j + 1]:
#                     valor_mayor = vector_a_ordenar[j] 
                    
#                     vector_a_ordenar[j] = vector_a_ordenar[j + 1]
#                     vector_a_ordenar[j + 1] = valor_mayor
                        
#     return vector_a_ordenar

# listar_elementos(vector_c)

# ordernar_negativos_positivos(vector_c)
# print("##############")
# listar_elementos(vector_c)