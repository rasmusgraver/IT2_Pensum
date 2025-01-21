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
from mario import Mario
from goomba import create_goomba
from bowser import create_bowser
import collission

mario = Mario()
goomba = create_goomba()
bowser = None

score = 0
running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:
    screen.blit(bg_image, (0, 0))

    # Skriver tekst på skjermen:
    tekst.skriv_tekst(screen, 100, 40, f"Din score er: {score}", farge=WHITE, bakgrunnsfarge=BLACK)

    # Flytter og tegner spilleren, og andre objekter:
    mario.move()
    mario.draw(screen)
    goomba.move()
    goomba.draw(screen)

    if bowser:
        bowser.move()
        bowser.draw(screen)

    collission.handle_collission(mario, goomba)


    # Start en ny goomba hvis den er død eller har kommet til at x<0
    if goomba.y > HEIGHT or goomba.x < 0:
        # Øk scoren hvis goomba har falt ned av skjermen:
        if goomba.y > HEIGHT:
            score += 10

        goomba = create_goomba()

        if score > 40 and not bowser:
            bowser = create_bowser()

    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
