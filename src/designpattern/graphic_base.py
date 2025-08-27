# import pygame
# from time import sleep

# pygame.init()
# screen = pygame.display.set_mode((800,600))
# pygame.draw.rect(screen, (255,0,34), pygame.Rect(42,15,400,32))
# pygame.display.flip()
# sleep(10)

import pygame
from time import sleep

window_dimensions = 800,600
screen = pygame.display.set_mode(window_dimensions)

def draw_square(x,y):
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(x,y,40,40))

x = 100; y = 100
quits = False

while not quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quits = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] : y -= 4
        if pressed[pygame.K_DOWN] : y += 4
        if pressed[pygame.K_LEFT] : x -= 4
        if pressed[pygame.K_RIGHT] : x += 4
        draw_square(x,y)
    pygame.display.flip()