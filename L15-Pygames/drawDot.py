'''
1. Set up the game
'''
import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True

'''
2. The game loop
'''
GREEN = (0,255,0)    # RGB color triplet for GREEN
radius = 50
while keep_going:
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # draw on the screen
    pygame.draw.circle(screen, GREEN, (100,100), radius)
    pygame.display.update()

'''
3. Exit the game
'''
pygame.quit()
