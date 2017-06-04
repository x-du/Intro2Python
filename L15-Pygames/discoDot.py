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
#GREEN = (0,255,0)    # RGB color triplet for GREEN
radius = 50
while keep_going:
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # draw on the screen
    # ADD CODE HERE: 1. create a random color
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    xpos = random.randint(0,800)
    ypos = random.randint(0,600)
    #time.sleep(0.3)
    pygame.draw.circle(screen, color , (xpos,ypos), radius)
    pygame.display.update()

'''
3. Exit the game
'''
pygame.quit()
