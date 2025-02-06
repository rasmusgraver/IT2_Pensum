import pygame as pg
from constants import *

class Rute:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.farge = SORT
        self.fyll = False

    def tegn(self, screen):
        if self.fyll:
            # Uten ekstra-paramter til slutt, så blir hele ruten fargelagt:
            pg.draw.rect(screen, self.farge, (self.x, self.y, RUTE_STR, RUTE_STR))
        else:
            # Angir en paramter til: Bredden på streken - da blir det uten fyll, bare en "tom rute":
            pg.draw.rect(screen, self.farge, (self.x, self.y, RUTE_STR, RUTE_STR), 1)

    def oppdater(self):
        # TODO: Logikk om oppdatering i forhold til naboer osv
        if self.farge == SORT:
            if self.x > SKJERM_BREDDE // 2:
                self.farge = GUL
            else:
                self.farge = BLAA
        else: 
            self.farge = SORT

    # Hva skal skje når ruten blir klikket på:
    def klikk(self):
        # "toggle" fyll av og på:
        self.fyll = not self.fyll
