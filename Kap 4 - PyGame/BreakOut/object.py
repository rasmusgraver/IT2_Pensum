import pygame as pg
from constants import *


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
        # MERK: Har fjernet sjekk med "spretting" i bunn (y == HEIGHT)
        if self.y < self.radius:
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

    def kollisjon_med_pad(self, pad):
        """ Detekter om vi "kolliderer" med padden """
        if (self.y + self.radius > pad.y 
            and self.y + self.radius < pad.y + pad.hoyde
            and self.x > pad.x and self.x < pad.x + pad.bredde):
            # Sprett oppover:
            self.dy = -self.dy
            # "Dytt ballen over padden" (unngå at ballen "fanges i padden")
            self.y = pad.y - self.radius

    def game_over(self):
        if self.y > HEIGHT:
            # Stop ballen for å vise game over:
            self.dy = 0
            self.dx = 0


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
        # Henter en liste med status for alle tastatur-taster
        trykkede_taster = pg.key.get_pressed()
        if trykkede_taster[pg.K_LEFT] and self.x > 0:
            self.x -= self.fart
        if trykkede_taster[pg.K_RIGHT] and self.x < WIDTH - self.bredde:
            self.x += self.fart


