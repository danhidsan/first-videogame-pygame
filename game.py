import sys
import pygame

# Initialize game engine
pygame.init()

# screen size
size = (500, 500)

# set up screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My first game")

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing lines
    pygame.draw.line(screen, RED, (0, 0), (200, 200), 2)
    pygame.draw.line(screen, RED, (500, 0), (300, 200), 2)
    pygame.draw.line(screen, RED, (0, 500), (200, 300), 2)
    pygame.draw.line(screen, RED, (500, 500), (300, 300), 2)

    # drawing rectangle
    pygame.draw.rect(screen, RED, pygame.Rect((200, 200), (100, 100)), 2)

    # drawing circle
    pygame.draw.circle(screen, RED, (250, 250), 50, 0)
    # drawing circle border
    pygame.draw.circle(screen, BLUE, (250, 250), 50, 2)

    # drawing polygon
    pygame.draw.polygon(screen, GREEN, [(200, 200), (250, 100), (300, 200)])

    pygame.display.update()

