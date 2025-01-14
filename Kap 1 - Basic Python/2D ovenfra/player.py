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
        if keys_pressed[K_LEFT] and self.x > 0:
            self.x -= PLAYER_SPEED
            self.image = link_l
        if keys_pressed[K_RIGHT] and self.x < WIDTH:
            self.x += PLAYER_SPEED
            self.image = link_r
        if keys_pressed[K_UP] and self.y > 0:
            self.y -= PLAYER_SPEED
            self.image = link_u
        if keys_pressed[K_DOWN] and self.y < HEIGHT:
            self.y += PLAYER_SPEED
            self.image = link_d

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

