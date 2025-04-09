import pygame as pg
from constants import *

class Ruby:

    def __init__(self):
        self.farge = PURPLE
        self.radius = 20
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.radius - GRASS_HEIGHT
        self.dy = -RUBY_JUMP_HEIGHT

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def oppdater(self):

        # Bevegelse i y-retning:
        self.dy += GRAVITY
        self.y += self.dy

        # Bevegelse i x-retning med tastatur:
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > self.radius:
            self.x -= RUBY_MOVE_SPEED
        if keys[pg.K_RIGHT] and self.x < SCREEN_WIDTH - self.radius:
            self.x += RUBY_MOVE_SPEED

        # Sjekk om vi treffer bakken:
        if self.y > SCREEN_HEIGHT - self.radius - GRASS_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius - GRASS_HEIGHT
            if keys[pg.K_UP]:
                # Hvis vi trykker opp, så hopp dobbelt høyde:
                self.dy = -RUBY_JUMP_HEIGHT*1.5
            else:
                self.dy = -RUBY_JUMP_HEIGHT
