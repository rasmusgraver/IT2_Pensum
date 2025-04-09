import pygame as pg
from constants import *

class Plateau(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((40, 8))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.liv = 3

    def mist_liv(self):
        self.liv -= 1
        if self.liv <= 0:
            self.kill()
        elif self.liv == 2:
            self.image.fill(ORANGE)
        elif self.liv == 1:
            self.image.fill(RED)

