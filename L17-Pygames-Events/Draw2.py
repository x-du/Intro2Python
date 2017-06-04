import pygame
import random


pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
draw_mode = True

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.MOUSEMOTION:
            spot = event.pos
            rect = pygame.Rect(spot, (50,50))
            if not draw_mode:
                color = (0,0,0)
            else:
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            #pygame.draw.circle(screen, color, spot, 10)
            pygame.draw.rect(screen, color,rect)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                draw_mode = False
            elif event.button == 1:
                draw_mode = True
    pygame.display.update()

pygame.quit()
