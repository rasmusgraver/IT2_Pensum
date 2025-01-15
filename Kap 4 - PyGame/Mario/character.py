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
        self.dead = False

    def move(self):
        # TODO: Fart i y-retning endrer seg med gravitasjonen:

        # TODO: Og posisjon i y-retning endrer seg med y-farten:

        # TODO: Når truffet gulvet, så stopper fallet: (med mindre man er død)

        return

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

