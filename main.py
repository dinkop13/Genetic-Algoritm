import pygame
import sys
from tkinter import *

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill(black)
    """ screen.blit(ball, ballrect) """
    pygame.display.flip()
