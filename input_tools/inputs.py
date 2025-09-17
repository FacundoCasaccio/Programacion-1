from validation_tools.validate import validate_number, validate_length

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int):
    input_usuario = input(mensaje)
    bandera_dato_valido = validate_number(input_usuario, minimo, maximo, int)


    while reintentos > 0 and bandera_dato_valido == False:
        print(mensaje_error)
        input_usuario = input(mensaje)
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
    

def get_fixed_int_list(lenght ,mensaje, mensaje_error, minimo, maximo, reintentos):
    lista_numeros = []
    
    for _ in range(lenght):
        numero = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        lista_numeros.append(numero)
        
    return lista_numeros


# Permite solicitar ingresos al usuario y devuelve una lista de strings
def get_string_list(mensaje, mensaje_repeticion, caracteres_maximos: int = 99):
    lista_strings = []
    
    continuar_ingreso = "S"
    
    while continuar_ingreso == "s" or continuar_ingreso == "S":
        ingreso_usuario = input(mensaje)
        
        if len(ingreso_usuario) > caracteres_maximos:
            print(f"Maxima cantidad de caracteres es {caracteres_maximos}, intente nuevamente...")
            
        else:
            lista_strings.append(ingreso_usuario)
            
        continuar_ingreso = None
        
        while continuar_ingreso != "s" and continuar_ingreso != "S" and continuar_ingreso != "n" and continuar_ingreso != "N":
            continuar_ingreso = input(mensaje_repeticion) #Desea realizar otro ingreso? [S/N]: 
    
    return lista_strings

# Permite solicitar ingresos ilimitados de listas y devolver una lista de listas
def get_list_of_inputs(mensaje, mensaje_repeticion, mensaje_repeticion_individual):
    lista_inputs = []
    
    continuar_ingreso = "S"
    
    while continuar_ingreso == "s" or continuar_ingreso == "S":
        lista_inputs.append(get_string_list(mensaje, mensaje_repeticion_individual))
            
        continuar_ingreso = None
        
        while continuar_ingreso != "s" and continuar_ingreso != "S" and continuar_ingreso != "n" and continuar_ingreso != "N":
            continuar_ingreso = input(mensaje_repeticion) #Desea realizar otro ingreso? [S/N]: 
    
    return lista_inputs 
