import pygame
from config.sudoku_config import * 
from src.game_utils import *
from src.funciones_puntajes import *
from ui.ui_utils import *

pygame.display.set_caption("Sudoku UTN - Facundo Casaccio") 

def draw(game_state: dict) -> None:
        
    if game_state["menu"]:
        dibujar_menu(game_state)
    
    else:
        dibujar_partida(game_state)
             
    pygame.display.update()

def main() -> None:
    game_state = inicializar_estado_juego() # Inicializar estado de juego
    run = True
    pygame.mixer.music.play(-1) # Emepezar con musica 
    
    # Bucle principal
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            # Eventos de menu
            if game_state["menu"]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Eventos menu principal
                    if game_state["menu_dificultad"] == False and game_state["mostrar_puntajes"] == False:
                        
                        # Click en Jugar
                        if RECT_BOTON_1.collidepoint(event.pos):
                            game_state["tablero_estado_inicial"], game_state["tablero_partida"] = inicializar_partida(game_state["dificultad"])
                            game_state["puntaje"] = 0
                            game_state["cuadrantes_correctos_validados"] = []
                            game_state["menu"] = False
                            SELECCIONAR.play()
                                          
                        # Click en Dificultad
                        if RECT_BOTON_2.collidepoint(event.pos):
                            game_state["menu_dificultad"] = True
                            SELECCIONAR.play()
                            
                        # Click en Top Puntajes
                        if RECT_BOTON_3.collidepoint(event.pos):
                            SELECCIONAR.play()
                            
                            # Mostrar puntajes
                            if game_state["mostrar_puntajes"] == False:
                                game_state["mostrar_puntajes"] = True
                            else:
                                # Volver al menu principal
                                game_state["mostrar_puntajes"] = False
                            
                        # Click en Salir
                        if RECT_BOTON_4.collidepoint(event.pos):
                            pygame.quit()
                            
                        # Click en musica para parar o reproducir
                        if RECT_MUSICA.collidepoint(event.pos):
                            if game_state["musica"]:
                                game_state["musica"] = False
                            else:
                                game_state["musica"] = True
                                
                            reproducir_musica(game_state)
                    
                    # Evento menu puntaje
                    elif game_state["mostrar_puntajes"] == True:
                        # Volver al menu principal
                        if RECT_BOTON_4.collidepoint(event.pos):
                            game_state["mostrar_puntajes"] = False
                            SELECCIONAR.play()
                    
                    # Eventos menu de seleccion de dificultad
                    else:
                        # Seleccionar Facil
                        if RECT_BOTON_1.collidepoint(event.pos):
                            game_state["dificultad"] = FACIL
                            SELECCIONAR.play()
                           
                        # Seleccionar Medio 
                        if RECT_BOTON_2.collidepoint(event.pos):
                            game_state["dificultad"] = MEDIO
                            SELECCIONAR.play()
                          
                        # Seleccionar Dificil 
                        if RECT_BOTON_3.collidepoint(event.pos):
                            game_state["dificultad"] = DIFICIL
                            SELECCIONAR.play()
                            
                        # Volver al menu principal
                        if RECT_BOTON_4.collidepoint(event.pos):
                            game_state["menu_dificultad"] = False
                            SELECCIONAR.play()
                        
            # Eventos de partida    
            else:
                
                # Eventos de mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Click en boton Validar
                    if RECT_BOTON_VALIDAR.collidepoint(event.pos):
                        validar(game_state)
                        
                    # Click en boton Resetear
                    if RECT_BOTON_RESETEAR.collidepoint(event.pos):
                        resetear(game_state)
                        
                    # Click en boton volver
                    if RECT_BOTON_VOLVER.collidepoint(event.pos):
                        # resetear(game_state)
                        game_state["menu"] = True
                        SELECCIONAR.play()
                        
                    # Click en una celda (seleccionarla)
                    if game_state["celda_resaltada"] and (game_state["fila_seleccion"] < 0 and game_state["fila_seleccion"] > 8) and (game_state["columna_seleccion"] < 0 and game_state["columna_seleccion"] > 8):
                        game_state["celda_resaltada"] = False
                        
                    else:
                        coordenadas_seleccion = event.pos
                        
                        game_state["posicion_tablero_seleccion"] = obtener_posicion_por_coordenadas(coordenadas_seleccion)
                        game_state["fila_seleccion"], game_state["columna_seleccion"] = game_state["posicion_tablero_seleccion"]
                        game_state["celda_resaltada"] = True                       
                 
                # Eventos de teclado       
                if event.type == pygame.KEYDOWN:
                    
                    # Ingreso de nombre/nick
                    if game_state["completado"]:
                        
                        # Borrar input
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            game_state["nombre"] = game_state["nombre"][:-1]
                            
                        # Guardado de input de usuario
                        elif event.key == pygame.K_RETURN and len(game_state["nombre"]) > 0:
                            datos_partida = {"nombre" : game_state["nombre"],
                                       "puntaje" : game_state["puntaje"]
                                       }
                            
                            escribir_json(datos_partida, "puntajes.json")
                            resetear(game_state)
                            game_state["menu"] = True
                            game_state["nombre"] = ""
                        
                        # Agregar input a la cadena
                        else:    
                            game_state["nombre"] += event.unicode
                    
                    # Atajos y ingreso de numeros 
                    else:
                        
                        # Atajo de teclado para validar
                        if event.key == pygame.K_RETURN:
                            validar(game_state)
                        
                        # Atajo de teclado para resetear1
                        elif event.key == pygame.K_r:
                            resetear(game_state)
                        
                        # Ingreso de numeros para celda seleccionada
                        elif game_state["celda_resaltada"] and (game_state["fila_seleccion"] >= 0 and game_state["fila_seleccion"] < 9) and (game_state["columna_seleccion"] >= 0 and game_state["columna_seleccion"] < 9):
                            
                            if game_state["tablero_estado_inicial"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] == 0:
                                if event.key == pygame.K_1:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 1
                                    
                                if event.key == pygame.K_2:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 2
                                    
                                if event.key == pygame.K_3:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 3
                                    
                                if event.key == pygame.K_4:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 4
                                    
                                if event.key == pygame.K_5:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 5
                                    
                                if event.key == pygame.K_6:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 6
                                    
                                if event.key == pygame.K_7:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 7
                                    
                                if event.key == pygame.K_8:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 8
                                    
                                if event.key == pygame.K_9:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 9
                                    
                                # Borrar estado de celda
                                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                                    game_state["tablero_partida"][game_state["fila_seleccion"]][game_state["columna_seleccion"]] = 0
                                    
                                    if (game_state["fila_seleccion"], game_state["columna_seleccion"]) in game_state["posiciones_invalidas"]:
                                        game_state["posiciones_invalidas"].remove((game_state["fila_seleccion"], game_state["columna_seleccion"]))
                                        
                        verificar_estado_partida(game_state)
                        
        # Dibujado en pantalla de estado de juego (menus, partida)
        draw(game_state)
                
                
# Para que se inicialice a correr, si el archivo se llama main                
if __name__ == "__main__":
    main()
