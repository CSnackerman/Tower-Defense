from sys import exit
import pygame
from pygame.locals import *

from tower import Tower

pygame.init()

window = pygame.display.set_mode ((500, 500))


tower = Tower (100, 100, 50, 50)
tower.moveToCenter()

while 1:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()

        if e.type == MOUSEBUTTONDOWN:
            tower.shoot ()

    window.fill ('#000000')

    tower.draw (window)

    pygame.display.update()