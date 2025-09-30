from validation_tools.validate import validate_number, validate_length, verificar_no_pertenece_array

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
    input_usuario = input(mensage)
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
    
def get_string_with_length(mensage: str, mensaje_error: str, reintentos: int, longitud):
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
    
def get_string(mensaje: str):
    input_usuario = input(mensaje)
    return input_usuario    
    

def get_fixed_int_list(lenght ,mensaje, mensaje_error, minimo, maximo, reintentos):
    lista_numeros = []
    
    for _ in range(lenght):
        numero = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        lista_numeros.append(numero)
        
    return lista_numeros


# Permite solicitar ingresos al usuarionumeros
def get_int_list(mensaje, mensaje_error, mensaje_repeticion, minimo, maximo):
    lista_numeros = []
    
    continuar_ingreso = "S"
    
    while continuar_ingreso == "s" or continuar_ingreso == "S":
        ingreso_usuario = get_int(mensaje, mensaje_error, minimo, maximo, reintentos = 99)
            
        lista_numeros.append(ingreso_usuario)
            
        continuar_ingreso = None
        
        while continuar_ingreso != "s" and continuar_ingreso != "S" and continuar_ingreso != "n" and continuar_ingreso != "N":
            continuar_ingreso = input(mensaje_repeticion) #Desea realizar otro ingreso? [S/N]: 
    
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

# Permite solicitar ingresos ilimitados de listas y devolver una lista de listas
def get_list_of_int_inputs(mensaje, mensaje_error, mensaje_repeticion, mensaje_repeticion_individual):
    lista_inputs = []
    
    continuar_ingreso = "S"
    
    while continuar_ingreso == "s" or continuar_ingreso == "S":
        lista_inputs.append(get_int_list(mensaje, mensaje_error, mensaje_repeticion_individual, minimo = -9999, maximo = 9999))
            
        continuar_ingreso = None
        
        while continuar_ingreso != "s" and continuar_ingreso != "S" and continuar_ingreso != "n" and continuar_ingreso != "N":
            continuar_ingreso = input(mensaje_repeticion) #Desea realizar otro ingreso? [S/N]: 
    
    return lista_inputs 

def get_int_matrix(filas, columnas, minimo = -9999, maximo = 9999):
    inputs_matrix = [0] * filas
    
    for i in range(filas):
        print(f"Fila {i + 1}")
        fila = get_fixed_int_list(lenght = columnas, 
                                  mensaje = "Ingrese un numero: ",
                                  mensaje_error = "Ingreso incorrecto.",
                                  minimo = -9999,
                                  maximo = 9999,
                                  reintentos = 99)
        inputs_matrix[i] = fila
        
    return inputs_matrix

def get_unique_int_matrix(filas, columnas, minimo = -9999, maximo = 9999):
    inputs_matrix = [0] * filas
    numeros_ingresados = []
    
    for i in range(filas):
        print(f"Fila {i + 1}")
        fila = [0] * columnas
        
        for j in range(columnas):
            repetido = True
            numero = 0
            
            while repetido:
                numero = get_int(mensaje = "Ingrese un numero (no repita entre ingresos: ",
                                mensaje_error = "Ingreso incorrecto.",
                                minimo = minimo,
                                maximo = maximo,
                                reintentos = 99)
            
                repetido = verificar_no_pertenece_array(numero, numeros_ingresados)
                
                if repetido:
                    print("Numero repetido, ingrese nuevamente...")
                
            numeros_ingresados.append(numero)
            fila[j] = numero
            
        inputs_matrix[i] = fila
        
    return inputs_matrix

        