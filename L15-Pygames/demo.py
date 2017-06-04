'''
1. Setup
'''
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
radius = 20
'''
2. Display loop
'''
colors = []
for i in range(10):
    colors.append((random.randint(0,255) ,random.randint(0,255) ,random.randint(0,255) ))
xy = []
for i in range(10):
    x = random.randint(0,800)
    y = random.randint(0,600)
    xy.append((x,y))


while keep_going:
    # handle event
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # draw on the screen
    for i in range(10):
        pygame.draw.circle(screen, colors[i], xy[i], radius)


    pygame.display.update()

'''
3. Exit
'''
pygame.quit()
