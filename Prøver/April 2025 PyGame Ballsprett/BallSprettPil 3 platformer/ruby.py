import pygame as pg
from constants import *

class Ruby:
    RUBY_BOTTOM = SCREEN_HEIGHT - GRASS_HEIGHT - RUBY_RADIUS

    def __init__(self):
        self.farge = PURPLE
        self.x = SCREEN_WIDTH // 2
        self.y = Ruby.RUBY_BOTTOM
        self.dy = -RUBY_JUMP_HEIGHT
        self.rect = pg.Rect(self.x - RUBY_RADIUS, self.y - RUBY_RADIUS, RUBY_RADIUS * 2, RUBY_RADIUS * 2)

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), RUBY_RADIUS)

    def hopp(self, keys):
        if keys[pg.K_UP]:
            # Hvis vi trykker opp, så hopp dobbelt høyde:
            self.dy = -RUBY_JUMP_HEIGHT*1.5
        else:
            self.dy = -RUBY_JUMP_HEIGHT

    def oppdater(self, platforms):

        # Bevegelse i y-retning:
        self.dy += GRAVITY
        self.y += self.dy

        # Bevegelse i x-retning med tastatur:
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > RUBY_RADIUS:
            self.x -= RUBY_MOVE_SPEED
        if keys[pg.K_RIGHT] and self.x < SCREEN_WIDTH - RUBY_RADIUS:
            self.x += RUBY_MOVE_SPEED

        # Sjekk om vi treffer bakken:
        if self.y > Ruby.RUBY_BOTTOM:
            self.y = Ruby.RUBY_BOTTOM
            self.hopp(keys)


        # Sjekk om vi treffer plattformene:
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Hvis vi treffer plattformen, så sett y-posisjonen til plattformens topp:
                self.y = platform.rect.top - RUBY_RADIUS
                self.hopp(keys)
                platform.mist_liv()
        
        # Oppdater rektangelet til Ruby
        self.rect.x = self.x - RUBY_RADIUS
        self.rect.y = self.y - RUBY_RADIUS

