# Valida que el numero no se repita en el cuadrante
def validar_numero_cuadrante(numero: int, posicion: tuple, tablero: list) -> bool:
    numero_valido = True
    
    cuadrante = obtener_cuadrante(posicion)
    
    for i in range(3):
        for j in range(3):
            posicion_actual = (i + 3 * cuadrante[0], j + 3 * cuadrante[1])
            
            # valida los que no esten ni en mima fila ni columna (validados en otra funcion)
            if posicion_actual[0] != posicion[0] and posicion_actual[1] != posicion[1]:
                if tablero[posicion_actual[0]][posicion_actual[1]] == numero:
                    numero_valido = False
                    break
    
    return numero_valido
                
# Devuelve coordenadas de cuadrante segun la posicion
# Coordenadas de cuadrante van en fila y columna de 0 al 2, usado para posteriores calculos
def obtener_cuadrante(posicion: tuple) -> tuple:
    fila_cuadrante = 0
    columna_cuadrante = 0
    
    if posicion[0] > 5:
        fila_cuadrante = 2
    elif posicion[0] > 2:
        fila_cuadrante = 1
        
    if posicion[1] > 5:
        columna_cuadrante = 2
    elif posicion[1] > 2:
        columna_cuadrante = 1
        
    cuadrante = (fila_cuadrante, columna_cuadrante)
    
    return cuadrante
    
# Valida que el numero no se repita en la fila del tablero
def validar_numero_fila(numero: int, posicion: tuple, tablero: list) -> bool:
    numero_valido = True
    
    for j in range(9):
        if tablero[posicion[0]][j] == numero and j != posicion[1]:
            numero_valido = False
            break
        
    return numero_valido
    
# Valida que el numero no se repita en la columna del tabklero
def validar_numero_columna(numero: int, posicion: tuple, tablero: list) -> bool:
    numero_valido = True
    
    for i in range(9):
        if tablero[i][posicion[1]] == numero and i != posicion[0]:
            numero_valido = False
            break
        
    return numero_valido
    
# Envoltorio de las tres validaciones para determinar si el posicionamiento del numero en el tablero es valido
def validar_posicionamiento_numero(numero: int, posicion: tuple, tablero: list) -> bool:
    posicionamiento_valido = False
    
    cuadrante_valido = validar_numero_cuadrante(numero, posicion, tablero)
    fila_valida = validar_numero_fila(numero, posicion, tablero)
    columna_valida = validar_numero_columna(numero, posicion, tablero)
    
    if cuadrante_valido and fila_valida and columna_valida:
        posicionamiento_valido = True
        
    return posicionamiento_valido

# Recorre el tablero y verifica que no haya 
def validar_tablero_completo(game_state: dict) -> bool:
    completo = True
    
    if len(game_state["posiciones_invalidas"]) == 0:
    
        for i in range(9):
            for j in range(9):
                
                numero = game_state["tablero_partida"][i][j]
                
                if numero == 0:
                    completo = False
                    break
    
    else:
        completo = False
            
    return completo

# Valida que el cuadrante objetivo este completo y sin errores para el calculo de puntos
def validar_cuadrante_completo(game_state: dict, cuadrante: tuple) -> bool:
    cuadrante_completo = True
    
    for i in range(3):
        for j in range(3):
            
            posicion_actual = (i + 3 * cuadrante[0], j + 3 * cuadrante[1])
            numero = game_state["tablero_partida"][posicion_actual[0]][posicion_actual[1]]
            estado_inicial_celda = game_state["tablero_estado_inicial"][posicion_actual[0]][posicion_actual[1]]
            valido = validar_posicionamiento_numero(numero, (posicion_actual), game_state["tablero_partida"])
            
            # print(f"Cuadrante {cuadrante} | Celda {posicion_actual} | Numero {numero} | Estado inicial {estado_inicial_celda} | Valido {valido}")
            
            if numero == 0:
                cuadrante_completo = False
                break
            elif numero != 0 and estado_inicial_celda == 0 and valido == False:
                cuadrante_completo = False
                break
          
    return cuadrante_completo
    

# Realiza el calculo de puntossegun el estado de la partida tras validar
def validar_puntos(game_state: dict) -> None:
    # Resta de puntos por posiciones invalidas
    game_state["posiciones_invalidas"] = obtener_posiciones_invalidas(game_state)
    game_state["puntaje"] -= len(game_state["posiciones_invalidas"])
    
    # Suma de puntos por cuadrantes completos correctos
    for i in range(3):
        for j in range(3):
            
            cuadrante = (i, j)
            cuadrante_completo = validar_cuadrante_completo(game_state, cuadrante)
            
            if cuadrante_completo:
                if cuadrante not in game_state["cuadrantes_correctos_validados"]:
                    game_state["puntaje"] += 9
                    game_state["cuadrantes_correctos_validados"].append(cuadrante)

           
    # Puntos extra por tablero completo y sin errores      
    if game_state["completado"] and len(game_state["posiciones_invalidas"]) == 0:
        game_state["puntaje"] += 81     
     
# Verifica el tablero y devuelve una lista con las posiciones invalidas encontradas        
def obtener_posiciones_invalidas(game_state: dict) -> list:
    posiciones_invalidas = []
    for i in range(9):
        for j in range(9):
            
            numero = game_state["tablero_partida"][i][j]

            if numero != 0 and game_state["tablero_estado_inicial"][i][j] == 0:
                valido = validar_posicionamiento_numero(numero, (i, j), game_state["tablero_partida"])
                
                if valido == False:
                    posiciones_invalidas.append((i, j))
                
    return posiciones_invalidas