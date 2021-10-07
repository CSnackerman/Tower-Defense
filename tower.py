import pygame.draw
import pygame.surface
import pygame.mouse
import pygame.display
from pygame.rect import Rect
from math import atan2, cos, sin
from projectile import Projectile

class Tower:

    def __init__(self, x, y, w, h):

        self.rect = Rect (x,y,w,h)
        self.towerColor = '#FF0000'
        self.lineColor = '#FFFFFF'
        self.dir = 0
        self.lineLength = 50
        self.ex = 0
        self.ey = 0
        self.projectiles = []

    def draw (self, surface):
        pygame.draw.rect (surface, self.towerColor, self.rect)

        p1x = self.rect.centerx
        p1y = self.rect.centery


        mpos = pygame.mouse.get_pos()
        p2x = mpos [0]
        p2y = mpos [1]

        self.dir = atan2 (p2y - p1y, p2x - p1x)

        self.ex = p1x + self.lineLength * cos (self.dir)
        self.ey = p1y + self.lineLength * sin (self.dir)
        e = (self.ex, self.ey)

        pygame.draw.line (surface, self.lineColor, self.rect.center, e, 5)

        for p in self.projectiles:
            p.draw (surface)

    def shoot (self):
        self.projectiles.append (Projectile (self.ex, self.ey, self.dir))
        

    def moveToCenter (self):
        self.rect.center = pygame.display.get_surface().get_rect().center

