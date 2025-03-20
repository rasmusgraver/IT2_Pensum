import pygame as pg
from constants import *

class Maur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.retning = "høyre"
        # Til den siste oppgaven med "animer()":
        self.x_offset = 0
        self.y_offset = 0


    def tegn(self, screen):
        x_pos = self.x * RUTE_STR + RUTE_STR//2 + self.x_offset
        y_pos = self.y * RUTE_STR + RUTE_STR//2 + self.y_offset
        pg.draw.circle(screen, RED, (x_pos, y_pos), RUTE_STR//2 - 4)


    def flytt(self, brett):
        if 0 <= self.x < ANT_X and 0 <= self.y < ANT_Y:
            rute = brett[self.x][self.y]
            retninger = ["høyre", "ned", "venstre", "opp"]
            # Litt fancy måte å gjør det på for å unngå 4 if/else conditions:
            retning_index = retninger.index(self.retning)
            if rute.farge == WHITE:
                # Snu til høyre (Roter med klokka 90 grader)
                retning_index += 1
            else:
                # Snu til venstre (Roter mot klokka 90 grader)
                retning_index -= 1
            self.retning = retninger[retning_index % 4]

            rute.besok()

            # Bruker offset for å animere bevegelsen: Mauren starter 
            # der den var, og beveger seg gradvis mot neste rute
            self.x_offset = 0
            self.y_offset = 0
            if self.retning == "høyre":
                self.x += 1
                self.x_offset = -RUTE_STR
            elif self.retning == "ned":
                self.y += 1
                self.y_offset = -RUTE_STR
            elif self.retning == "venstre":
                self.x -= 1
                self.x_offset = RUTE_STR
            elif self.retning == "opp":
                self.y -= 1
                self.y_offset = RUTE_STR


    def animer(self):
        # Den litt fancy siste oppgaven, med gradvis bevegelse mot ruten
        # Reduser offset, slik at mauren beveger seg mot ruten den skal til
        skritt_lengde = 2
        if self.x_offset < 0 or self.y_offset < 0:
            # gå "motsatt vei"
            skritt_lengde = -skritt_lengde
        if self.x_offset != 0:
            self.x_offset -= skritt_lengde
        if self.y_offset != 0:
            self.y_offset -= skritt_lengde

