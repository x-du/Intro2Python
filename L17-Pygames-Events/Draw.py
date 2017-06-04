import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
clear = False

while keep_going:
    pygame.event.set_grab(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.MOUSEMOTION:
            spot = event.pos
            pygame.draw.circle(screen, (255,0,0), spot, 10)
        elif event.type == pygame.KEYDOWN and event.key == KEY_c:
            screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()
