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