def verificar_ganador_ronda(jugador, maquina):
    resultado_ronda = None
    
    if jugador == 1:
        if maquina == 2:
            resultado_ronda = "Maquina"
        if maquina == 3:
            resultado_ronda = "Jugador"
            
    if jugador == 2:
        if maquina == 3:
            resultado_ronda = "Maquina"
        if maquina == 1:
            resultado_ronda = "Jugador"
            
    if jugador == 3:
        if maquina == 1:
            resultado_ronda = "Maquina"
        if maquina == 2:
            resultado_ronda = "Jugador"
            
    if resultado_ronda == None:
        resultado_ronda = "Empate"
    
    return resultado_ronda

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    estado_partida = None
    
    if ronda_actual == 3: 
        if aciertos_jugador == aciertos_maquina:
            estado_partida = True
        else:
            estado_partida = False
    elif ronda_actual == 2 and (aciertos_jugador == 2 or aciertos_maquina == 2):
        estado_partida = False
        
    elif ronda_actual > 3 and (aciertos_jugador != aciertos_maquina):
        estado_partida = False
    else:
        estado_partida = True
        
    return estado_partida

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    ganador_partida = None
    
    if aciertos_jugador > aciertos_maquina:
        ganador_partida = "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        ganador_partida = "Maquina"
        
    return ganador_partida

def mostrar_elemento(eleccion):
    eleccion_str = None
    
    match eleccion:
        case 1:
            eleccion_str = "Piedra"
        case 2:
            eleccion_str = "Papel"
        case 3:
            eleccion_str = "Tijera"
            
    return eleccion_str