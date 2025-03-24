import pygame as pg
from constants import *
from tekst import skriv_tekst

class Rute:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.farge = WHITE

    def __str__(self):
        return f"Rute {self.x}, {self.y} med farge {self.farge}"

    def besok(self):
        self.farge = BLACK if self.farge == WHITE else WHITE

    def tegn(self, screen):
        x_pos = self.x * RUTE_STR
        y_pos = self.y * RUTE_STR

        pg.draw.rect(screen, self.farge, (x_pos, y_pos, RUTE_STR, RUTE_STR))

        # Tegner rammen:
        pg.draw.rect(screen, GREY, (x_pos, y_pos, RUTE_STR, RUTE_STR), 1)

