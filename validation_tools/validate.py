def validate_number(input, minimo, maximo, type):
    bandera_int = False
    contador_puntos = 0
    contador_simbolo_menos = 0

    # Recorrer caracteres de la cadena del input
    for caracter in input:
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
        if contador_puntos == 0 and contador_simbolo_menos < 2 and type == int:
            numero = int(input)
            if (numero < minimo or numero > maximo):
                return False
            else:
                return True
        # Caso float
        elif contador_puntos == 1 and contador_simbolo_menos < 2 and type == float:
            numero = float(input)
            if (numero < minimo or numero > maximo):
                return False
            else:
                return True
        # Caso string
        else:
            return False

        
def validate_length(input, expected_length):
    if len(input) != expected_length:
        return False
    else:
        return True

def verificar_no_pertenece_array(elemento, array):
    pertenece = False
    
    if len(array) != 0:
        for i in range(len(array)):
            elemento_array = array[i]
            
            if elemento == elemento_array:
                pertenece = True
            
    return pertenece

def verificar_cadena_alfabetica(cadena):
    alfabetica = True
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        
        if verifificar_caracter_alfabetico(caracter) == False:
            alfabetica = False
            break
    
    return alfabetica
        
def verifificar_caracter_alfabetico(caracter):
    alfabetico = True
    codigo_caracter = ord(caracter)
    
    if codigo_caracter < 32 or (codigo_caracter > 32 and codigo_caracter < 65) or (codigo_caracter > 90 and codigo_caracter < 97) or codigo_caracter > 122:
        alfabetico = False
        
    return alfabetico

def verificar_caracter_numerico(caracter):
    numerico = True
    codigo_caracter = ord(caracter)
    
    if codigo_caracter < 48 or codigo_caracter > 57:
        numerico = False
        
    return numerico

def verificar_numero_entero(cadena):
    numerica_entera = True
    contador_menos = 0
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        codigo_caracter = ord(caracter)
        
        if codigo_caracter == 45:
            
            if contador_menos == 0:
                contador_menos += 1
            else:
                numerica_entera = False
                break
        elif verificar_caracter_numerico(caracter) == False :
            numerica_entera = False
            break
    
    return numerica_entera

def verificar_numero_decimal(cadena):
    numerica_decimal = True
    contador_puntos = 0
    contador_menos = 0
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        codigo_caracter = ord(caracter)
        
        if verificar_caracter_numerico(caracter) == False and codigo_caracter != 46:
            numerica_decimal = False
            break
        elif codigo_caracter == 46:
            if contador_puntos == 0:
                contador_puntos += 1
            else:
                numerica_decimal = False
                break
        elif codigo_caracter == 45:
            if contador_menos == 0:
                contador_menos += 1
            else:
                numerica_decimal = False
                break
            
    if contador_puntos == 0: # Si no hay piuntos, no es un decimal
        numerica_decimal = False
    
    return numerica_decimal

def validar_seguridad_clave(clave):
    clave_segura = False
    
    contiene_mayuscula = False
    contiene_minuscula = False
    contiene_numero = False
    
    if len(clave) >= 8:
        for i in range(len(clave)):
            caracter = clave[i]
            
            if contiene_mayuscula and contiene_minuscula and contiene_numero:
                clave_segura = True
                break
            
            if contiene_mayuscula == False:
                contiene_mayuscula = verificar_mayuscula(caracter)
                
            if contiene_minuscula == False:
                contiene_minuscula = verificar_minuscula(caracter)
                
            if contiene_numero == False:
                contiene_numero = verificar_caracter_numerico(caracter)
                
    return clave_segura
    
def verificar_minuscula(caracter):
    
    es_minuscula = False
    codigo_caracter = ord(caracter)
    
    if (codigo_caracter >= 97 and codigo_caracter <= 122):
        es_minuscula = True
        
    return es_minuscula

def verificar_mayuscula(caracter):
    es_mayuscula = False
    codigo_caracter = ord(caracter)
    
    if (codigo_caracter >= 65 and codigo_caracter <= 90):
        es_mayuscula = True
        
    return es_mayuscula