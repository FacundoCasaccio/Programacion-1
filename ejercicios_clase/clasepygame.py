import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    pantalla.fill((0, 250, 0))
    pygame.display.update()