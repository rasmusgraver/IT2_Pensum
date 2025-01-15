import pygame as pg
from constants import *
# from object_5 import Ball, Pad

# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

# Henter inn tekst, bilder, og spilleren:
# Merk: Kan ikke laste inn font og bilder før vi har gjort pg.init:
import tekst
from bilder import *
from mario import Mario


mario = Mario(200, 100)

score = 10
running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)
    # screen.fill(BLACK)

    # Tegner bakgrunnsbildet:
    screen.blit(bg_image, (0, 0))

    # Skriver tekst på skjermen:
    tekst.skriv_tekst(screen, 100, 40, f"Din score er: {score}", farge=WHITE, bakgrunnsfarge=BLACK)


    # Flytter og tegner spilleren:
    mario.move()
    mario.draw(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
