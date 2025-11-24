from operation_tools.arrays_generales import *
import random
from prog_1_sp.config.sudoku_config import *
from prog_1_sp.src.validaciones import *
from prog_1_sp.sound.sounds import *
import pygame


pygame.mixer.init()


# Inicializa una grilla de 9 x 9 con 0 en cada posicion
def inicializar_grilla() -> list:
    grilla = []
    for _ in range(9):
        fila = [0] * 9
        grilla.append(fila)
        
    return grilla

# Devuelve una lista de numeros del 1 al 9 desordenada para generar mas aleatorieidad
def obtener_numeros() -> list:
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(lista)
    
    return lista

# Itera la grilla, busca un vacio ("0") y devuleve las coordenadas
def encontrar_vacio(grilla: list) -> tuple|None:
    coordenadas = None
    
    for i in range(len(grilla)):
        for j in range(len(grilla[0])):
            
            if grilla[i][j] == 0:
                coordenadas = (i, j)
                break
                
    return coordenadas
    
# Completar la grilla utilizando algoritmo con "bactracking"
# El backtarcking hace que, mediante recursividad, vuelva pasos atras si se encontro con una solucion imposible
def obtener_grilla_solucion(grilla: list) -> bool:
    
    vacio = encontrar_vacio(grilla) # buscar un vacio y obtener las coordenadas

    if not vacio: # Si no hay vacios, la grilla solucion esta completa
        return True
    
    else:
        fila, columna = vacio # Si hay vacios, la grilla queda por llenar

    numeros = obtener_numeros() # obtener los numeros desordenados para que de soluciones mas aleatorias siempre
    
    for numero in numeros:
        if validar_posicionamiento_numero(numero, (fila, columna), grilla):
            grilla[fila][columna] = numero # Si el posicionamiento es valido, lo pone en la grilla
            
            if obtener_grilla_solucion(grilla): # Llama recursivamente hasta que encuetra la solucion
                return True
            
            grilla[fila][columna] = 0 # Si no tuvo solucion posible, resetea esa posicion a 0
            
    return False # Cuando el retorno cae en false, es cuando no pudo posicionar, entonces, con backtracking vuelve para seguir la solucion posible

# Obtiene matriz usada como tablero de partida en su punto inicial.
# Se genera a partir de la solucion, ocultando numeros aleatorios por cuadrante
def obtener_grilla_inicial_partida(grilla_solucion: list, numeros_por_ocultar: int) -> list:
    grilla_partida = copiar_grilla(grilla_solucion)
    
    for i in range(3):
        for j in range(3):
            
            cuadrante = (i, j)
            numeros_ocultos = obtener_numeros_a_ocultar(numeros_por_ocultar)
            
            ocultar_numeros_cuadrante(cuadrante, numeros_ocultos, grilla_partida)
            
    return grilla_partida
                               
# Recibe como parametro la cantidad de numeros para ocultar por cuadrante
# Devuelve valores dentro de los permitidos, aleatorios, para ocultar en un cuadrante
def obtener_numeros_a_ocultar(numeros_por_ocultar: int) -> list:
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(lista_numeros)
    
    for _ in range(numeros_por_ocultar + 1):
        lista_numeros.pop()
        
    return lista_numeros

# Recibe el cuadrante y los numeros que debe ocultar, y en base a la soluciond el tablero, recorre cada uno y oculta dichos valores
def ocultar_numeros_cuadrante(cuadrante: tuple, numeros_ocultos: list, grilla_partida: list) -> None:
    for i in range(3):
        fila = i + 3 * cuadrante[0]
        
        for j in range(3):
            columna = j + 3  * cuadrante[1]
            
            if grilla_partida[fila][columna] in numeros_ocultos:
                grilla_partida[fila][columna] = 0

# Recibe un tablero y devuelve una copia (no por referencia)
def copiar_grilla(grilla: list) -> list:
    nueva_grilla = []
    
    for fila in grilla:
        copia_fila = fila[:] 
        nueva_grilla.append(copia_fila)
                            
    return nueva_grilla

# Inicializa las matrices que representan al tablero en base a la dificultad y las retorna     
def inicializar_partida(dificultad: int) -> tuple:
    
    tablero_solucion = inicializar_grilla()
    obtener_grilla_solucion(tablero_solucion)

    tablero_estado_inicial = obtener_grilla_inicial_partida(tablero_solucion, dificultad)
    
    tablero_partida = copiar_grilla(tablero_estado_inicial)
    
    return tablero_estado_inicial, tablero_partida
                
# Inicializa el estado base del juego con todas las variables y tableros y lo retorna         
def inicializar_estado_juego() -> dict: 
    game_state = {
        "menu" : True,
        "menu_dificultad" : False,
        "mostrar_puntajes" : False,
        "dificultad" : FACIL,
        "celda_resaltada" : False,
        "coordenadas_seleccion" : (-1, -1),
        "posicion_tablero_seleccion" :(-1, -1),
        "fila_seleccion" : -1,
        "columna_seleccion" : -1,
        "posiciones_invalidas" : [],
        "completado" : False,
        "puntaje" : 0,
        "cuadrantes_correctos_validados" : [],
        "celdas_correctas_validadas" : [],
        "nombre" : "",
        "musica": True
        }

    game_state["tablero_estado_inicial"], game_state["tablero_partida"] = inicializar_partida(game_state["dificultad"])
    
    return game_state

# Obtiene y devuelve el campo "puntaje" del item de la lista de puntajes, que es un archivo JSON, siendo una lista de diccionarios
def obtener_puntaje(item: dict) -> int:
    return item["puntaje"]

# Calcula y devuelve las posiciones del tablero en base a las coordenadas de pantalla
def obtener_posicion_por_coordenadas(coordenadas: tuple) -> tuple:
    x = coordenadas[0]
    y = coordenadas[1]
    
    fila = int((x - BOARD_PADDING) // CELL_WIDTH)
    columna = int((y - BOARD_PADDING) // CELL_HEIGHT) 
    
    return (fila, columna)

# Envuelve la funcionalidad de validar en partida (por boton o atajo)
# Obtiene posiciones invalidas, chequea estado de partida compeltada o no y calcula puntos
def validar(game_state: dict) -> None:
    game_state["posiciones_invalidas"] = obtener_posiciones_invalidas(game_state)
    game_state["completado"] = validar_tablero_completo(game_state)
    validar_puntos(game_state)
    
    if len(game_state["posiciones_invalidas"]) > 0:
        INCORRECT_SOUND.play()
    else:        
        if game_state["completado"]:
            COMPLETE_SOUND.play()
        else:
            CORRECT_SOUND.play()
     
# Funcion que verifica el estado de juego luego de cada accion, sin el riesgo de validar y perder puntos
def verificar_estado_partida(game_state: dict) -> None:
    # Resta de puntos por posiciones invalidas
    posiciones_invalidas = obtener_posiciones_invalidas(game_state)
    
    # Suma de puntos por cuadrantes completos correctos
    for i in range(3):
        for j in range(3):
            
            cuadrante = (i, j)
            cuadrante_completo = validar_cuadrante_completo(game_state, cuadrante)
            
            if cuadrante_completo:
                if cuadrante not in game_state["cuadrantes_correctos_validados"]:
                    game_state["puntaje"] += 9
                    game_state["cuadrantes_correctos_validados"].append(cuadrante)

    game_state["completado"] = validar_tablero_completo(game_state)
    # Puntos extra por tablero completo y sin errores      
    if game_state["completado"] and len(posiciones_invalidas) == 0:
        game_state["puntaje"] += 81
        COMPLETE_SOUND.play()     
        
# Envuelve la funcionalidad de resetear la partida usada por boton o atajo
# Resetea las variables del estado de juego y vuelve el tablero a su estado inicial
def resetear(game_state: dict) -> None:
    game_state["tablero_partida"] = copiar_grilla(game_state["tablero_estado_inicial"])
    game_state["completado"] = False
    game_state["posiciones_invalidas"] = []
    game_state["puntaje"] = 0
    game_state["cuadrantes_correctos_validados"] = []
    
# Reproduce o detiene la musica segun el estado de juego
def reproducir_musica(game_state: dict) -> None:
    if game_state["musica"]:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()