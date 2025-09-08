# Ejercicio 13
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

def validar_tipo_input(input):
    bandera_int = False
    contador_puntos = 0
    contador_simbolo_menos = 0

    for caracter in input:
        codigo_ascii_caracter =  ord(caracter)
        
        if codigo_ascii_caracter >= 48 and codigo_ascii_caracter <= 57:
            bandera_int = True
        elif codigo_ascii_caracter == 46:
            contador_puntos += 1
        elif codigo_ascii_caracter == 45:
            contador_simbolo_menos += 1
        else:
            return str

    if contador_simbolo_menos >= 2:
            return str

    if bandera_int == True:
        if contador_puntos == 0 and contador_simbolo_menos < 2:
            return int
        elif contador_puntos == 1 and contador_simbolo_menos < 2:
            return float
        else:
            return str
        
# Por si se quiere usar especificamente para int
def input_entero():
    tipo_input_usuario = None
    input_usuario = None

    while tipo_input_usuario != int:
        input_usuario = input("Ingrese un numero entero: ")
        tipo_input_usuario = validar_tipo_input(input_usuario)

        if tipo_input_usuario != int:
            print("Tipo incorrecto, vuelva a intentarlo.")
    return int(input_usuario)

# Por si se quiere usar especificamente para float
def input_float():
    tipo_input_usuario = None
    input_usuario = None

    while tipo_input_usuario != float:
        input_usuario = input("Ingrese un numero decimal: ")
        tipo_input_usuario = validar_tipo_input(input_usuario)

        if tipo_input_usuario != float:
            print("Tipo incorrecto, vuelva a intentarlo.")
    return float(input_usuario)

# Input de usuario generico
def casted_input():
    input_usuario = input("Ingrese algo aqui: ")

    tipo_input = validar_tipo_input(input_usuario)

    if tipo_input == int:
        return int(input_usuario)
    elif tipo_input == float:
        return float(input_usuario)
    else:
        return input_usuario
    
ingreso_usuario = casted_input()

print(ingreso_usuario)
print(type(ingreso_usuario))