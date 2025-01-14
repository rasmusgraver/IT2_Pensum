import pygame as pg
from constants import *


# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

# Henter inn tekst, bilder, og spilleren:
# Merk: Kan ikke laste inn font og bilder før vi har gjort pg.init:
import tekst
from bilder import *
from player import Player


player = Player(200, 100)

score = 10
running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)
    screen.fill(BLACK)

    # Tegner bakgrunnsbildet:


    # Skriver tekst på skjermen:
    # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)


    # Flytter og tegner spilleren:


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
