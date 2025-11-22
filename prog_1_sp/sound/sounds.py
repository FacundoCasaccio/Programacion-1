import pygame
import os

pygame.mixer.init()

# Carga de sonidos de partida
CORRECT_SOUND = pygame.mixer.Sound(os.path.join("prog_1_sp", "assets", "correct.mp3"))
COMPLETE_SOUND = pygame.mixer.Sound(os.path.join("prog_1_sp", "assets", "complete.mp3"))
INCORRECT_SOUND = pygame.mixer.Sound(os.path.join("prog_1_sp", "assets", "incorrect.mp3"))
# Carga de sonidos de menu
SELECCIONAR = pygame.mixer.Sound(os.path.join("prog_1_sp", "assets", "seleccionar.mp3"))

# Carga de musica y volumen
MUSICA = pygame.mixer.music.load(os.path.join("prog_1_sp", "assets", "musica.mp3"))
pygame.mixer.music.set_volume(0.5)
