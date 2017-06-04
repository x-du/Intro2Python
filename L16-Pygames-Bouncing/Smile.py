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
    if ypos > 500:
        yspeed = random.randint(-10, -1)
    if ypos < 0:
        yspeed = random.randint(1,10)
    if xpos > 500 or xpos < 0:
        xspeed = -xspeed
    pygame.display.update()

pygame.quit()
