from input_tools.inputs import get_list_of_inputs
from operation_tools.arrays_generales import recomendar_productos

listas_productos_usuarios = get_list_of_inputs(mensaje= "Ingrese un producto: ", 
                                               mensaje_repeticion= "Desea ingresar otro cliente? [S/N]: ", 
                                               mensaje_repeticion_individual= "Desea ingresar otro producto para este cliente? [S/N]: ")


# listas_usuarios = [["pepsi", "coca", "fanta", "manaos", "coca"], ["coca", "7up", "fanta", "coca", "Dr Pepper", "Dr Pepper", "Dr Pepper", "Dr Pepper", "Dr Pepper", "Dr Pepper" ]]

recomendar_productos(listas_productos_usuarios)
