import sys
import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game")

color = pygame.Color(70, 80, 150)

while True:
    window.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

