'''
Modify the following program so that, when the smile face bounces, it bounces with a random angle.
'''
import pygame
import random

screen = pygame.display.set_mode([600,600])
pic = pygame.image.load("CrazySmile.bmp")
keep_going = True
xpos = 0
ypos = 0
yspeed = random.randint(0, 10)
xspeed = random.randint(0, 10)
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.fill((0,0,0))
    screen.blit(pic, (xpos,ypos))
    ypos += yspeed
    xpos += xspeed
    if ypos > 500 or ypos < 0:
        yspeed = -yspeed
    if xpos > 500 or xpos < 0:
        xspeed = -xspeed
    pygame.display.update()

pygame.quit()
