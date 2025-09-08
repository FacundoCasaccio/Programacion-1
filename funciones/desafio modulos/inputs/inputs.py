from validations.validate import validate_number, validate_length

def get_int(mensage: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int):
    print(mensage)
    input_usuario = input("Ingrese un numero entero: ")
    bandera_dato_valido = validate_number(input_usuario, minimo, maximo, int)


    while reintentos > 0 and bandera_dato_valido == False:
        print(mensaje_error)
        input_usuario = input("Ingrese un numero entero: ")
        bandera_dato_valido = validate_number(input_usuario, minimo, maximo, int)
        reintentos -= 1
        
    if bandera_dato_valido == False:
        return None
    else:
        return int(input_usuario)
    
        
def get_float(mensage: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int):
    print(mensage)
    input_usuario = input("Ingrese un numero decimal: ")
    bandera_dato_valido = validate_number(input_usuario, minimo, maximo, float)


    while reintentos > 0 and bandera_dato_valido == False:
        print(mensaje_error)
        input_usuario = input("Ingrese un numero decimal: ")
        bandera_dato_valido = validate_number(input_usuario, minimo, maximo, float)
        reintentos -= 1
        
    if bandera_dato_valido == False:
        return None
    else:
        return float(input_usuario)
    
def get_string(mensage: str, mensaje_error: str, reintentos: int, longitud = int):
    print(mensage)
    input_usuario = input(f"Ingrese un una cadena de caracteres de longitud {longitud}:\n ")
    bandera_dato_valido = validate_length(input_usuario, longitud)


    while reintentos > 0 and bandera_dato_valido == False:
        print(mensaje_error)
        input_usuario = input(f"Ingrese un una cadena de caracteres de longitud {longitud}:\n ")
        bandera_dato_valido = validate_length(input_usuario, longitud)
        reintentos -= 1
        
    if bandera_dato_valido == False:
        return None
    else:
        return input_usuario