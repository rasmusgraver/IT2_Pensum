import pygame as pg
from constants_5 import *


class Ball:

    def __init__(self, farge, radius, x, y, dx, dy):
        self.farge = farge
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def oppdater(self):
        self.x += self.dx 
        self.y += self.dy

        # Sjekk om vi kolliderer i veggen:
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy

        # Sørg for at vi ikke blir "stuck" i veggen
        self.flytt_ut_fra_veggen() 


    def flytt_ut_fra_veggen(self):
        """ Dytt ballen litt ut fra veggen """
        if self.x < self.radius:
            self.x = self.radius
        if self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT -self.radius



class Pad:

    def __init__(self, farge, x, y, bredde, hoyde, fart):
        self.farge = farge
        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde
        self.fart = fart

    def tegn(self, screen):
        pg.draw.rect(screen, self.farge, (self.x, self.y, self.bredde, self.hoyde))


    def oppdater(self):
        # TODO: Oppdater self.x med self.fart avhengig av piltaster trykket
        pass


