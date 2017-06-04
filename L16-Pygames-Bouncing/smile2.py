import pygame
import sys
import random

screen = pygame.display.set_mode([600, 600])
pic = pygame.image.load("CrazySmile.bmp")
xpos = 0
ypos = 0
xspeed = 2
yspeed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill((0,0,0))
    screen.blit(pic, (xpos,ypos))

    if xpos > 500 or xpos < 0:
        xspeed = -xspeed
        # xspeed = xspeed * 0.9
    if ypos > 500 or ypos < 0:
        yspeed = -yspeed
        # yspeed = yspeed * 0.9

    xpos += xspeed
    ypos += yspeed
    pygame.display.update()
