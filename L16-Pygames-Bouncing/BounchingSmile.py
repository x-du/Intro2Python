import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600,600])
pic = pygame.image.load("CrazySmile.bmp")
xpos = 0 ; xspeed = 2; ypos = 0; yspeed = 3
BLACK = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if xpos > 500 or xpos < 0: xspeed = -xspeed
    if ypos > 500 or ypos < 0: yspeed = -yspeed
    screen.fill(BLACK)
    xpos = xpos + xspeed
    ypos = ypos + yspeed
    screen.blit(pic, (xpos,ypos))
    pygame.display.update()
