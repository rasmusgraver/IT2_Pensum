import pygame as pg
from constants import *
from bilder import *

class Character:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.dy = 0
        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.dead = False

    def move(self):
        # Fart i y-retning endrer seg med gravitasjonen:
        self.dy += GRAVITY

        # Og posisjon i y-retning endrer seg med y-farten:
        self.y += self.dy

        # Når truffet gulvet, så stopper fallet: (med mindre man er død)
        # Hvis du er død, så fortsetter du å falle (ut av skjermen)
        if not self.dead and self.y > FLOOR - self.height:
            self.dy = 0
            self.y = FLOOR - self.height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

