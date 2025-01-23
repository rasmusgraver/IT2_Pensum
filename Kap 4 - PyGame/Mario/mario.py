import pygame as pg
from constants import *
from bilder import *
from character import Character

class Mario(Character):

    def __init__(self):
        x = 200
        y = FLOOR # Mario starter nede på floor
        super().__init__(x, y, mario_image)
        # Dytt ham opp like mye som han er høy (kan ikke bruke self.height før super_init...)
        y = FLOOR - self.height

    def move(self):
        if not self.dead:
            keys_pressed = pg.key.get_pressed()
            if keys_pressed[pg.K_LEFT] and self.x > 0:
                self.x -= MARIO_SPEED
                self.image = mario_image_left
            if keys_pressed[pg.K_RIGHT] and self.x < WIDTH - self.width:
                self.x += MARIO_SPEED
                self.image = mario_image
            if keys_pressed[pg.K_UP]:
                self.jump()
        super().move()

    def jump(self):
        if self.dy == 0:
            self.dy = MARIO_JUMP

