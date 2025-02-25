import pygame as pg
from constants import *

class Rute:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fyll = False

    def __str__(self):
        return f"Jeg er er rute {self.x}, {self.y}"

    def klikk(self):
        self.fyll = not self.fyll

    def tegn(self, screen):
        x_pos = self.x * RUTE_STR
        y_pos = self.y * RUTE_STR

        # Tegn fyllet først, så border kommer "oppå"
        if self.fyll:
            pg.draw.rect(screen, BLUE, (x_pos, y_pos, RUTE_STR, RUTE_STR))

        pg.draw.rect(screen, BLACK, (x_pos, y_pos, RUTE_STR, RUTE_STR), 1)


    def oppdater(self, brett):
        if self.fyll:
            # Fargelegg "den neste" rute (den til høyre)
            neste_x = self.x + 1
            if neste_x < ANT_X:
                neste_rute = brett[neste_x][self.y]
                neste_rute.fyll = True
