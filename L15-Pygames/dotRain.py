'''
1. Set up the game
'''
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True

'''
2. The game loop
'''
radius = 20
colors = []
BLACK = (0,0,0)
for i in range(10):
    colors.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
speed = 5
ypos = 20
while keep_going:
    screen.fill(BLACK)
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # draw on the screen
    for i in range(10):
        pygame.draw.circle(screen, colors[i] , (100+i*50,ypos), radius)
    # ADD CODE Here to change ypos
    
    pygame.display.update()

'''
3. Exit the game
'''
pygame.quit()
