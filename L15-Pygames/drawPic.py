'''
1. Set up the game
'''
import pygame
import time

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
timer = pygame.time.Clock()


'''
2. The game loop
'''
x=100
y=100
while keep_going:
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # draw on the screen
    x+=1
    y+=1
    screen.blit(pic, (x,y))
    pygame.display.update()
    timer.tick()
'''
3. Exit the game
'''
pygame.quit()
