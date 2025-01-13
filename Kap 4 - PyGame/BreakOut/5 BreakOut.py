import pygame as pg
from constants_5 import *
from object_5 import Ball, Pad

# Start opp PyGame:
pg.init()
# Lag en klokke:
clock = pg.time.Clock()
# Start PyGame vinduet:
screen = pg.display.set_mode(SIZE)


ball = Ball(farge=YELLOW, radius=10, x=50, y=100, dx=3, dy=-3)
pad = Pad(WHITE, 100, HEIGHT-40, 40, PAD_HOYDE, PAD_FART)

running = True

while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Klokka sørger for rett hastighet (ut i fra FPS):
    # TEST: Hva skjer om vi fjerner denne linja?
    clock.tick(FPS)
    # Må tegne på en bakgrunnsfarge
    # TEST: Hva skjer om vi fjerner denne linja?
    screen.fill(BLACK)

    pad.oppdater()
    ball.oppdater()
    ball.kollisjon_med_pad(pad)
    ball.game_over()

    pad.tegn(screen)
    ball.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
