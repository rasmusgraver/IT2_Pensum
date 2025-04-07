import pygame as pg
from constants import *

class Ball(pg.sprite.Sprite):

    def __init__(self, farge, radius, x, y, dx, dy):
        super().__init__()
        self.liv = 5 # Antall liv
        self.farge = farge
        self.radius = radius
        # MERK: Trenger ikke self.x og self.y lenger - bruker rect.x og rect.y i stedet
        # self.x = x
        # self.y = y
        self.dx = dx
        self.dy = dy
        # Lager en "Surface" som vårt bilde, og tegner på denne surfacen
        self.image = pg.Surface((radius*2, radius*2))
        self.image.fill(WHITE) # Fyller med hvit bakgrunn
        self.image.set_colorkey(WHITE) # Gjør hvit transparent
        # Tegner en sirkel med farge og radius:
        # MERK: Vi setter x og y til radius, fordi vi tegner i midten av self.image
        pg.draw.circle(self.image, self.farge, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    """
    MERK: Skal ikke lenger ha en draw funksjon, fordi vi bruker sprite group til å tegne
    og spriteGroup.draw() bare "blitter" self.image på skjermen. 
    def draw(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)
    """

    # Denne blir kalt når man kaller på SpriteGroup.update()
    def update(self):
        # MERK: Flytter med rect.x og rect.y: (DVS: Vi flytter hele "bildet" vårt)
        self.rect.x += self.dx 
        self.rect.y += self.dy

        self.flytt_ut_fra_veggen() # Sørg for at vi ikke blir "stuck" i veggen

        # Sjekk om vi kolliderer i veggen:
        # Hvis vi gjør det, så snu retning på dx/dy
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx = -self.dx
            self.liv -= 1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -self.dy
            self.liv -= 1

        if self.liv <= 0:
            # Om vi har mistet alle liv, så "kill" ballen:
            self.kill()
        elif self.liv <= 2:
            # Om vi har mindre enn 2 liv, så endre farge:
            if self.liv == 2:
                self.farge = ORANGE
            else:
                self.farge = RED
            # Må tegne ballen på nytt når vi endrer farge:
            # self.image.fill(WHITE)
            pg.draw.circle(self.image, self.farge, (self.radius, self.radius), self.radius)



    def flytt_ut_fra_veggen(self):
        """ Dytt ballen litt ut fra veggen """
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)


    def kollisjon(self, target):
        """ Sjekk om vi kolliderer med "target """
        if pg.Rect.colliderect(self.rect, target.rect):
            self.dx *= -1
            self.dy *= -1

