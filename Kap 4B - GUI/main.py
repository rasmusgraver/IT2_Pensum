import pygame as pg
from constants import *
from rute import Rute

# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SKJERM_STR)



# Fra tegneprogram på Aunivers: brett = [[HVIT for k in range(KOLONNER)] for r in range(RADER)]
brett = []
for y in range(RADER):
    rad = []
    for x in range(KOLONNER):
        rute = Rute(x*RUTE_STR, y*RUTE_STR)
        rad.append(rute)
    # Setter opp et todimensjonalt brett: Rader som inneholder ruter bortover
    brett.append(rad)


frame_count = 0
running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            rad, kol = y // RUTE_STR, x // RUTE_STR
            if rad < RADER and kol < KOLONNER:
                rute = brett[rad][kol]
                rute.klikk()

    # Venter til neste "frame"
    clock.tick(FPS)


    # Oppdaterer skjermen bare hvert sekund:
    frame_count += 1
    if frame_count > FPS:
        frame_count = 0
        screen.fill(HVIT)

        # Hvis vi vil skrive noe tekst på skjermen:
        # import tekst
        # tekst.skriv_tekst(screen, 100, 40, f"Din score er: {score}", farge=WHITE, bakgrunnsfarge=BLACK)

        for rad in brett:
            for rute in rad:
                rute.oppdater()
                rute.tegn(screen)



    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
