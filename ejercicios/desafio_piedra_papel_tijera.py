from menu_tools.menu_utils import print_menu
from input_tools.inputs import get_int
from pieda_papel_tijera.piedra_papel_tijera_utils import *
import random


estado_partida = None
opcion_seleccionada = None
ronda_actual = 0
aciertos_jugador = 0
aciertos_maquina = 0
ganador_partida = None

opciones_menu = [
    "1- Piedra",
    "2- Papel",
    "3- Tijera\n"
]

def jugar_piedra_papel_tijera():
    global ronda_actual, aciertos_jugador, aciertos_maquina, ganador_partida
    ronda_actual += 1
    
    eleccion_jugador = get_int("\nElija una opcion: ", "Opcion incorrecta, elija nuevamente", 1, 3, 100)
    eleccion_maquina = random.randint(1, 3)
    
    ganador_ronda = verificar_ganador_ronda(eleccion_jugador, eleccion_maquina)
    
    if ganador_ronda == "Empate":
        print(f"{ganador_ronda}. Jugador {mostrar_elemento(eleccion_jugador)}, Maquina {mostrar_elemento(eleccion_maquina)}")
    else:
        print(f"{ganador_ronda} gano la ronda. Jugador {mostrar_elemento(eleccion_jugador)}, Maquina {mostrar_elemento(eleccion_maquina)}")
    
    if ganador_ronda == "Jugador":
        aciertos_jugador += 1
    elif ganador_ronda == "Maquina":
        aciertos_maquina += 1
        
    if verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
        jugar_piedra_papel_tijera()
    else:
        ganador_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
        print(f"{ganador_partida} ha ganado la partida!")

print_menu(opciones_menu)        
jugar_piedra_papel_tijera()
    
    
    
    
    
