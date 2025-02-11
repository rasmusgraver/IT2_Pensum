import pygame as pg
from constants import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = link_r
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
            self.image = link_l
        if keys_pressed[K_RIGHT] and self.rect.x < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
            self.image = link_r
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= PLAYER_SPEED
            self.image = link_u
        if keys_pressed[K_DOWN] and self.rect.y < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED
            self.image = link_d

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
