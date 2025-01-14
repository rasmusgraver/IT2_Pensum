import pygame as pg
from constants import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = link_r


    def move(self):
        keys_pressed = pg.key.get_pressed()
        # TODO

    def draw(self, screen):
        pass

