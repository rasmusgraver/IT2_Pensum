import pygame as pg
from constants import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = link_r
        self.rect = self.image.get_rect()
        self.rect.width -= 10
        self.rect.center = (x, y)
        self.x_adj = 0
        self.y_adj = 0


    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
            self.image = link_l
            self.x_adj = -10
            self.y_adj = 0
        if keys_pressed[K_RIGHT] and self.rect.x < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
            self.image = link_r
            self.x_adj = 0
            self.y_adj = 0
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= PLAYER_SPEED
            self.image = link_u
            self.x_adj = -5
            self.y_adj = 0
        if keys_pressed[K_DOWN] and self.rect.y < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED
            self.image = link_d
            self.x_adj = -5
            self.y_adj = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x + self.x_adj, self.rect.y + self.y_adj))
        pg.draw.rect(screen, BLACK, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)

        
