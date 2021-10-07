from pygame import Vector2
import pygame.draw
from math import sin, cos

class Projectile:

    def __init__(self, x, y, angle):

        self.position = Vector2 (x, y)
        self.velocity = Vector2 (0, 0)
        
        self.speed = 0.1
        self.radius = 7
        self.color = '#FF00FF'

        self.setVelocity (angle)

    def draw (self, surface):
        self.position += self.velocity
        pygame.draw.circle (surface, self.color, self.position, self.radius)

    def setVelocity (self, angle):
        vx = self.speed * cos (angle)
        vy = self.speed * sin (angle)
        self.velocity.update ((vx, vy))


