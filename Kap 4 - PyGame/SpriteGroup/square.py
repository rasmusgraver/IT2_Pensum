import pygame as pg
import random
from constants import *

class Square(pg.sprite.Sprite):
    def __init__(self, x, y, color = None):
        super().__init__()
        self.image = pg.Surface((100, 100))
        if color:
            self.image.fill(color)
        else:
            r,g,b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.image.fill( (r,g,b) )
        self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            # self.rect.y = 0
            self.kill()

