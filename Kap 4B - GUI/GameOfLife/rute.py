import pygame as pg
from constants import *
import random

class Rute:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Trekk et tilfeldig tall mellom 1 og 3
        tilf_tall = random.randint(1,3)
        self.fyll = tilf_tall == 1 # Hvis tallet er 1, så sett fyll til True 
        self.neste_fyll = False

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
        antall_levende_naboer = 0
        for x_teller in (-1,0,1):
            for y_teller in (-1,0,1):
                if not (x_teller == 0 and y_teller == 0): # Ikke sjekk deg selv
                    # Sjekk at vi ikke går utenfor brettet:
                    nabo_x = self.x + x_teller
                    nabo_y = self.y + y_teller
                    if 0 <= nabo_x < ANT_X and 0 <= nabo_y < ANT_Y:
                        nabo_rute = brett[nabo_x][nabo_y]
                        if nabo_rute.fyll:
                            antall_levende_naboer += 1
        # Enhver levende celle med færre enn to levende naboer dør, som ved underpopulasjon.
        if self.fyll and antall_levende_naboer < 2:
            self.neste_fyll = False
        # Enhver levende celle med to eller tre naboer lever videre til neste generasjon.
        if self.fyll and 2 <= antall_levende_naboer <= 3:
            self.neste_fyll = True
        # Enhver levende celle med flere enn tre levende naboer dør, som ved overpopulasjon.
        if self.fyll and antall_levende_naboer > 3:
            self.neste_fyll = False
        # Enhver død celle med akkurat tre levende naboer blir vekket til live, som ved reproduksjon.
        if self.fyll == False and antall_levende_naboer == 3:
            self.neste_fyll = True




    def neste_frame(self):
        self.fyll = self.neste_fyll
        self.neste_fyll = False

