import pygame
from pygame import Rect
from config.sudoku_config import * 
from src.game_utils import *
from src.funciones_puntajes import *
from ui.rects import *
from ui.ui_utils import *
import os

pygame.font.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

FONDO = pygame.transform.scale(pygame.image.load(os.path.join("prog_1_sp", "assets", "fondo.png")), (WIDTH, HEIGHT))

MUSIC_ON = pygame.transform.scale(pygame.image.load(os.path.join("prog_1_sp", "assets", "music_on.png")), (DIMENSION_ICONO_MUSICA, DIMENSION_ICONO_MUSICA))
MUSIC_OFF = pygame.transform.scale(pygame.image.load(os.path.join("prog_1_sp", "assets", "music_off.png")), (DIMENSION_ICONO_MUSICA, DIMENSION_ICONO_MUSICA))

FUENTE_TITULO = pygame.font.SysFont("Roboto", NUMERO_FUENTE_TITULO)
FUENTE_NUMEROS = pygame.font.SysFont("Roboto", NUMERO_FUENTE_TABLERO)
FUENTE_BOTON = pygame.font.SysFont("Roboto", NUMERO_FUENTE_TABLERO)

# Dibuja el icono de reproducir musica segun su estado (prendido o apagado)
def dibujar_icono_musica(game_state: dict) -> None:
    if game_state["musica"]:
        WINDOW.blit(MUSIC_ON, (X_BOTON_MUSICA, Y_BOTON_MUSICA))
    else:
        WINDOW.blit(MUSIC_OFF, (X_BOTON_MUSICA, Y_BOTON_MUSICA))
    
# Devuelve el color del boton en base a la dificultad seleccionada actualmente
def obtener_color_boton_dificultad(game_state: dict, dificultad: int) -> tuple:
    color = None
    
    if game_state["dificultad"] == dificultad: 
        color = AZUL
    else:
        color = GRIS_MEDIO 
    
    return color

# Envuelve toda la funcionalidad para dibujar el menu de seleccion de dificultad
def dibujar_botones_dificultad(game_state: dict) -> None:
    posicion_mouse = pygame.mouse.get_pos()
    
    texto_boton_facil = FUENTE_BOTON.render("Facil", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_1))
    texto_boton_medio = FUENTE_BOTON.render("Medio", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_2))
    texto_boton_dificil = FUENTE_BOTON.render("Dificil", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_3))
    texto_boton_volver = FUENTE_BOTON.render("Volver", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_4))
    
    pygame.draw.rect(WINDOW, obtener_color_boton_dificultad(game_state, FACIL), RECT_BOTON_1)
    pygame.draw.rect(WINDOW, obtener_color_boton_dificultad(game_state, MEDIO), RECT_BOTON_2)
    pygame.draw.rect(WINDOW, obtener_color_boton_dificultad(game_state, DIFICIL), RECT_BOTON_3)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_4)
    
    # Renderiza en la ventana, los botones con sus respectivos textos, inicializados arriba
    WINDOW.blit(texto_boton_facil, (RECT_BOTON_1.centerx - texto_boton_facil.get_width() / 2, RECT_BOTON_1.centery - texto_boton_facil.get_height() // 2))
    WINDOW.blit(texto_boton_medio, (RECT_BOTON_2.centerx - texto_boton_medio.get_width() / 2, RECT_BOTON_2.centery - texto_boton_medio.get_height() // 2))
    WINDOW.blit(texto_boton_dificil, (RECT_BOTON_3.centerx - texto_boton_dificil.get_width() / 2, RECT_BOTON_3.centery - texto_boton_dificil.get_height() // 2))
    WINDOW.blit(texto_boton_volver, (RECT_BOTON_4.centerx - texto_boton_volver.get_width() / 2, RECT_BOTON_4.centery - texto_boton_volver.get_height() // 2))
    
# Dibuja el cuadro que contiene los maximos puntajes, mostrando nombre y puntaje y ademas, el boton para volver al menu principal
# Los puntajes los lee del archivo ya guardado
def dibujar_puntajes() -> None:
    puntajes = leer_json("puntajes.json") # Leer puntajes del archivo
    
    top_10_puntajes = sorted(puntajes, key = obtener_puntaje, reverse = True)[:10] # Ordenarlos por puntaje de manere descendente, y agarrar solamente los 10 primeros
                
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_PUNTAJES) # Recuedro para los puntajes
    
    # Iterar la lista de puntajes, y, por cada uno, renderizar nombre y puntaje sobre el recuadro
    for i in range(len(top_10_puntajes)):
        string_nombre_puntaje = top_10_puntajes[i]["nombre"]
        string_puntaje = str(top_10_puntajes[i]["puntaje"])
        
        texto_nombre_puntaje = FUENTE_NUMEROS.render(string_nombre_puntaje, 1, GRIS_CLARO)
        texto_puntaje = FUENTE_NUMEROS.render(string_puntaje, 1, GRIS_CLARO)
        
        WINDOW.blit(texto_nombre_puntaje, (RECT_PUNTAJES.left + 40, RECT_PUNTAJES.top + (texto_nombre_puntaje.get_height() + 10) * i + 30))
        WINDOW.blit(texto_puntaje, (RECT_PUNTAJES.right - 40 - texto_puntaje.get_width(), RECT_PUNTAJES.top + (texto_puntaje.get_height() + 10) * i + 30))
        
    # Dibujar boton de volver para el menu principal
    posicion_mouse = pygame.mouse.get_pos()
    
    texto_boton_volver = FUENTE_BOTON.render("Volver", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_4))
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_4)
    WINDOW.blit(texto_boton_volver, (RECT_BOTON_4.centerx - texto_boton_volver.get_width() / 2, RECT_BOTON_4.centery - texto_boton_volver.get_height() // 2))
   
# Calcula y devuelve el color del texto del boton segun la posicion del mouse (efecto hover)
def obtener_color_texto(posicion_mouse: tuple, rect_boton: Rect) -> tuple:
    color = GRIS_CLARO
    if rect_boton.collidepoint(posicion_mouse):
        color = NARANJA
        
    return color

# Dibuja el titulo segun la patalla del menu que se encuentre el estado de juego
def dibujar_titulo(game_state: dict) -> None:
    titulo = "Sudoku!"
    
    if game_state["mostrar_puntajes"]:
        titulo = "Top 10 Puntajes"
    if game_state["menu_dificultad"]:
        titulo = "Elegir Dificultad"
    
    texto_titulo = FUENTE_TITULO.render(titulo, 1, GRIS_CLARO)
    WINDOW.blit(texto_titulo, ((WIDTH - texto_titulo.get_width()) // 2, 100))
    

# Dibuja todos los botones que componen al menu principal y el titulo
def dibujar_menu_principal() -> None:
    posicion_mouse = pygame.mouse.get_pos()
    
    texto_boton_jugar = FUENTE_BOTON.render("Jugar", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_1))
    texto_boton_dificultad = FUENTE_BOTON.render("Dificultad", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_2))
    texto_boton_puntajes = FUENTE_BOTON.render("Top Puntajes", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_3))
    texto_boton_salir = FUENTE_BOTON.render("Salir", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_4))
    
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_1)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_2)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_3)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_4)
    
    WINDOW.blit(texto_boton_jugar, (RECT_BOTON_1.centerx - texto_boton_jugar.get_width() / 2, RECT_BOTON_1.centery - texto_boton_jugar.get_height() // 2))
    WINDOW.blit(texto_boton_dificultad, (RECT_BOTON_2.centerx - texto_boton_dificultad.get_width() / 2, RECT_BOTON_2.centery - texto_boton_dificultad.get_height() // 2))
    WINDOW.blit(texto_boton_puntajes, (RECT_BOTON_3.centerx - texto_boton_puntajes.get_width() / 2, RECT_BOTON_3.centery - texto_boton_puntajes.get_height() // 2))
    WINDOW.blit(texto_boton_salir, (RECT_BOTON_4.centerx - texto_boton_salir.get_width() / 2, RECT_BOTON_4.centery - texto_boton_salir.get_height() // 2))
    
# Dibuja fondo y envuelve la funciones de dibujado de todos los menu
def dibujar_menu(game_state: dict) -> None:
    
    WINDOW.blit(FONDO, (0, 0))
    
    dibujar_titulo(game_state)
    
    if game_state["menu_dificultad"]:
        dibujar_botones_dificultad(game_state)
        
    elif game_state["mostrar_puntajes"]:
        dibujar_puntajes()
            
    else:
        dibujar_menu_principal()
        
    dibujar_icono_musica(game_state)
        
# Dibuja el recuadro para solicitar nombre al usuario una vez terminada la partida para guardar el puntaje
def dibujar_pedir_nombre(game_state: dict) -> None:
    texto_boton_pedir_nombre = FUENTE_NUMEROS.render("Ingrese nombre:", 1, GRIS_CLARO)
    texto_boton_nombre = FUENTE_NUMEROS.render(game_state["nombre"], 1, GRIS_CLARO)

    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_PEDIR_NOMBRE)

    WINDOW.blit(texto_boton_pedir_nombre, (RECT_PEDIR_NOMBRE.left + 10, RECT_PEDIR_NOMBRE.top + 10))
    WINDOW.blit(texto_boton_nombre, (RECT_PEDIR_NOMBRE.centerx - texto_boton_nombre.get_width() / 2, RECT_PEDIR_NOMBRE.centery - texto_boton_nombre.get_height() // 2))

"""
Dibuja el tablero de la partida
Muestra los numeros en color segun estado (inicial, incorrecto, posicionado, completado)
Dibuja la grilla del tablero y los separadores por cuadrante
Colorea celdas segun celda seleccionada, mostrando fila, columna y cuadrante con las que compara la celda seleccionada actualmente
"""
def dibujar_tablero(game_state: dict) -> None:
    fila_seleccionada, columna_seleccionada = game_state["posicion_tablero_seleccion"]
    
    for i in range(9):
        
        for j in range(9):
            x_celda = i * CELL_WIDTH + BOARD_PADDING
            y_celda = j * CELL_HEIGHT + BOARD_PADDING
            
            cuadrante = obtener_cuadrante((i, j))
            cuadrante_seleccionado = obtener_cuadrante(game_state["posicion_tablero_seleccion"])
            
            rect_celda = pygame.Rect(x_celda, y_celda, CELL_WIDTH, CELL_WIDTH)
            
            color_celda = GRIS_OSCURO
            color_borde = GRIS_CLARO
            grosor_borde = 1
            
            # Pintar las celdas contra las que compara la seleccionada
            if game_state["celda_resaltada"] and (fila_seleccionada >= 0 and fila_seleccionada < 9) and (columna_seleccionada >= 0 and columna_seleccionada < 9):
                if fila_seleccionada == i or columna_seleccionada == j or cuadrante == cuadrante_seleccionado:
                    color_celda = GRIS
                    
                    # Recuadrar en rojo la celda celeccionada
                    if fila_seleccionada == i and columna_seleccionada == j:
                        color_celda = AZUL
                                                
            # Celda
            pygame.draw.rect(WINDOW, color_celda, rect_celda)
            # Borde celda
            pygame.draw.rect(WINDOW, color_borde, rect_celda, grosor_borde)
            
            # Colorea el numero de la celda segun su estado
            valor_celda = game_state["tablero_partida"][i][j]
            if valor_celda != 0:
                if game_state["tablero_estado_inicial"][i][j] != 0:
                    color_texto = GRIS_CLARO # Estado inicial
                    
                elif (i, j) in game_state["posiciones_invalidas"]:
                    color_texto = ROJO # Estado incorrecto
                else:
                    color_texto = NARANJA # Estado posicionado correcto/no validaddo
                    
                if game_state["completado"]:
                    color_texto = VERDE # Estado partida completada
                    
                texto_celda = FUENTE_NUMEROS.render(str(valor_celda), 1, color_texto)
                WINDOW.blit(texto_celda, (rect_celda.centerx - texto_celda.get_width() / 2, rect_celda.centery - texto_celda.get_height() // 2))
                
        # Dibuja separadores de cuadrantes, dando mejor claridad visual sobre el tablero de la partida
        for k in range(3, 9, 3):
            RECT_SEPARADOR_VERTICAL = pygame.Rect(k * CELL_WIDTH + BOARD_PADDING - 2, BOARD_PADDING, 4, 9 * CELL_HEIGHT)
            RECT_SEPARADOR_HORIZONTAL = pygame.Rect(BOARD_PADDING, k * CELL_WIDTH + BOARD_PADDING - 2, 9 * CELL_HEIGHT, 4)
            
            
            pygame.draw.rect(WINDOW, BLANCO, RECT_SEPARADOR_VERTICAL)
            pygame.draw.rect(WINDOW, BLANCO, RECT_SEPARADOR_HORIZONTAL)
                    
# Dibuja los botones utilizados en la partida (Validar, Resetear y Volver)
def dibujar_botones_partida() -> None:
    posicion_mouse = pygame.mouse.get_pos()
    
    texto_boton_validar = FUENTE_BOTON.render("Validar", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_VALIDAR))
    texto_boton_resetear = FUENTE_BOTON.render("Resetear", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_RESETEAR))
    texto_boton_volver = FUENTE_BOTON.render("Volver", 1, obtener_color_texto(posicion_mouse, RECT_BOTON_VOLVER))
    
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_VALIDAR)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_RESETEAR)
    pygame.draw.rect(WINDOW, GRIS_MEDIO, RECT_BOTON_VOLVER)
    
    WINDOW.blit(texto_boton_validar, (RECT_BOTON_VALIDAR.centerx - texto_boton_validar.get_width() / 2, RECT_BOTON_VALIDAR.centery - texto_boton_validar.get_height() // 2))
    WINDOW.blit(texto_boton_resetear, (RECT_BOTON_RESETEAR.centerx - texto_boton_resetear.get_width() / 2, RECT_BOTON_RESETEAR.centery - texto_boton_resetear.get_height() // 2))
    WINDOW.blit(texto_boton_volver, (RECT_BOTON_VOLVER.centerx - texto_boton_volver.get_width() / 2, RECT_BOTON_VOLVER.centery - texto_boton_volver.get_height() // 2))
    
# Dibuja el puntaje actual de la partida
def dibujar_puntaje(game_state: dict) -> None:
    puntaje_formateado = formatear_puntaje(game_state)
    
    texto_puntaje = FUENTE_BOTON.render(f"Puntaje: {puntaje_formateado}", 1, GRIS_CLARO)
    WINDOW.blit(texto_puntaje, (850, BOARD_PADDING))
    
# Envuelve todos las funciones de dibujado para mostrar la partida
def dibujar_partida(game_state: dict) -> None:
    WINDOW.fill(GRIS_OSCURO)
    
    dibujar_tablero(game_state)
    dibujar_botones_partida()
    dibujar_puntaje(game_state)

    if game_state["completado"]:
        dibujar_pedir_nombre(game_state)

# Da formato al puntaje, completando con ceros para tener 4 cifras
def formatear_puntaje(game_state: dict) -> str:
    puntaje_string = str(game_state["puntaje"])
    puntaje_string_formateado = ""
    
    for _ in range(4 - len(puntaje_string)):
        puntaje_string_formateado += "0"
        
    puntaje_string_formateado += puntaje_string

    
    return puntaje_string_formateado