import pygame as pg
from constants import *
import random


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
        """
        MERK: Returnerer en ny ball når den treffer veggen!
        """
        self.x += self.dx 
        self.y += self.dy

        # Sjekk om vi kolliderer i veggen:
        # Hvis vi gjør det, så snu retning på dx/dy
        # OG! Lag en ny ball!
        ny_dx = 0
        ny_dy = 0
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
            ny_dx = self.dx
            ny_dy = -self.dy # Snu y retningen på den nye ballen
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy
            ny_dy = self.dy
            ny_dx = -self.dx # Snu x retningen på den nye ballen

        self.flytt_ut_fra_veggen()

        if ny_dx or ny_dy:
            # Lag en ny ball, og returner denne
            # Legg inn en liten random, så vi får litt variasjon i sprettingen:
            ny_dx *= (random.random()*0.2 + 0.8)
            ny_dy *= (random.random()*0.2 + 0.8)
            # TODO: Hadde vært gøy å endre fargen litt: Gjør ballene litt lysere hver gang f eks
            return Ball(farge=self.farge, radius=self.radius, x=self.x, y=self.y, dx=ny_dx, dy=ny_dy)
        else:
            return None

    def flytt_ut_fra_veggen(self):
        """ Dytt ballen litt ut fra veggen """
        if self.x < self.radius:
            self.x = self.radius + 1
        if self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius - 1
        if self.y < self.radius:
            self.y = self.radius + 1
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT -self.radius - 1

