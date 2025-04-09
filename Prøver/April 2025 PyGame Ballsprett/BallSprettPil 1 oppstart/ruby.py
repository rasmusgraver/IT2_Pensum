import pygame as pg
from constants import *

class Ruby:

    def __init__(self):
        self.farge = PURPLE
        self.radius = 20
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.radius - GRASS_HEIGHT
        self.dx = 0
        self.dy = 0

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def oppdater(self):
        self.x += self.dx 
        self.y += self.dy
        # Sjekk om vi kolliderer i veggen:
        # Hvis vi gjør det, så snu retning på dx/dy
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.dy = -self.dy
