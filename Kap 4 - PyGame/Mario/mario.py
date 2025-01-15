import pygame as pg
from constants import *
from bilder import *

class Mario:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.image = mario_image

    def move(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_LEFT] and self.x > 0:
            self.x -= MARIO_SPEED
        if keys_pressed[pg.K_RIGHT] and self.x < WIDTH:
            self.x += MARIO_SPEED
        if keys_pressed[pg.K_UP]:
            self.jump()
        # Fart i y-retning endrer seg med gravitasjonen:
        self.dy += GRAVITY
        # Og posisjon i y-retning endrer seg med y-farten:
        self.y += self.dy
        # Når truffet gulvet, så stopper fallet:
        if self.y > FLOOR:
            self.y = FLOOR
            self.dy = 0

    def jump(self):
        self.dy = MARIO_JUMP

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

