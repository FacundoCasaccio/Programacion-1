# Valida que el input del usuario sea numerico
def validar_numero(input_usuario, minimo : int, maximo : int, tipo : type):
    bandera_int = False
    contador_puntos = 0
    contador_simbolo_menos = 0

    # Recorrer caracteres de la cadena del input
    for i in range(len(input_usuario)):
        caracter = input_usuario[i]
        codigo_ascii_caracter =  ord(caracter)
        
        if codigo_ascii_caracter >= 48 and codigo_ascii_caracter <= 57:
            bandera_int = True
        elif codigo_ascii_caracter == 46:
            contador_puntos += 1
        elif codigo_ascii_caracter == 45:
            contador_simbolo_menos += 1
        else:
            return False

    # Validacion para salida en caso de string
    if contador_simbolo_menos >= 2:
            return False

    if bandera_int == True:
        # Caso int
        if contador_puntos == 0 and contador_simbolo_menos < 2 and tipo == int:
            numero = int(input_usuario)
            if (numero < minimo or numero > maximo):
                return False
            else:
                return True
        # Caso float
        elif contador_puntos == 1 and contador_simbolo_menos < 2 and tipo == float:
            numero = float(input_usuario)
            if (numero < minimo or numero > maximo):
                return False
            else:
                return True
        # Caso string
        else:
            return False

# Verifica si una cadena es alfabetica y devuelve verdadero o falso
def verificar_cadena_alfabetica(cadena : str):
    alfabetica = True
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if verifificar_caracter_alfabetico(caracter) == False:
            alfabetica = False
            break
    
    return alfabetica
        
# Verifica si un caracter es alfabetica y devuelve verdadero o falso     
def verifificar_caracter_alfabetico(caracter : str):
    alfabetico = True
    codigo_caracter = ord(caracter)
    
    if codigo_caracter < 32 or (codigo_caracter > 32 and codigo_caracter < 65) or (codigo_caracter > 90 and codigo_caracter < 97) or codigo_caracter > 122:
        alfabetico = False
        
    return alfabetico

# Verifica si la longitud de la cadena es la longitud objetivo y retorna verdadero o falso
def verificar_longitud(cadena : str, longitud_objetivo : int):
    longitud_valida = True
    
    if len(cadena) != longitud_objetivo:
        longitud_valida =  False
    
    return longitud_valida

# Verifica que el ingreso del usuario este dentro de los ingresos validos pasados en la lista
def verificar_input_valido(input_usuario : str, inputs_esperados : list):
    input_valido = False
    
    for i in range(len(inputs_esperados)):
        input_objetivo = inputs_esperados[i]
        
        if input_usuario == input_objetivo:
            input_valido = True
            break
        
    return input_valido

# Verifica que el caracter objetivo sea numerico y devuelve un booleano
def verificar_caracter_numerico(caracter : str):
    numerico = True
    codigo_caracter = ord(caracter)
    
    if codigo_caracter < 48 or codigo_caracter > 57:
        numerico = False
        
    return numerico

# Verifica que la cadena sea un numero entero positivo
def verificar_cadena_numerica_positiva(cadena):
    numerica_entera = True
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if verificar_caracter_numerico(caracter) == False :
            numerica_entera = False
            break
    
    return numerica_entera

# Valida que el legajo tenga longitud deseada y sea un numero entero
def validar_legajo(legajo):
    LONGITUD_LEGAJO = 6
    
    legajo_valido = verificar_longitud(legajo, LONGITUD_LEGAJO)
    if legajo_valido:
        legajo_valido = verificar_cadena_numerica_positiva(legajo)
        
    return legajo_valido

# Valida que el ingreso sea uno de los generos objetivos
def validar_genero(genero_estudiante):
    GENEROS = ["F", "M", "X"]
    
    genero_valido = verificar_longitud(genero_estudiante, 1) # tiene que ser de longitud 1 el ingreso
    if genero_valido:
        genero_valido = verificar_input_valido(genero_estudiante, GENEROS)
        
    return genero_valido