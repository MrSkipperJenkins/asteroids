import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt