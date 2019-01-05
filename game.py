import sys
import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

