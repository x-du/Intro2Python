import pygame
import random


pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.MOUSEMOTION:
            spot = event.pos
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pygame.draw.circle(screen, color, spot, 10)
    pygame.display.update()

pygame.quit()
