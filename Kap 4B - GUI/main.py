import pygame as pg
from constants import *
from rute import Rute

# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SKJERM_STR)



# Fra tegneprogram på Aunivers: brett = [[HVIT for k in range(KOLONNER)] for r in range(RADER)]
brett = []
for x in range(ANT_X):
    kolonne = []
    for y in range(ANT_Y):
        rute = Rute(x*RUTE_STR, y*RUTE_STR)
        kolonne.append(rute)
    # Setter opp et todimensjonalt brett: kolonner som inneholder ruter bortover
    brett.append(kolonne)


frame_count = 0
running = True
while running:

    clock.tick(FPS)

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_pos, y_pos = pg.mouse.get_pos()
            x, y = x_pos // RUTE_STR, y_pos // RUTE_STR
            if x < ANT_X and y < ANT_Y:
                rute = brett[x][y]
                rute.klikk()
                frame_count = 0 # Tilbakestiller klokka, så man rekker å klikke mer før noe endres


    # Oppdaterer skjermen bare hvert sekund:
    frame_count += 1
    if frame_count > FPS:
        frame_count = 0

        for kolonne in brett:
            for rute in kolonne:
                rute.oppdater()


    # Hvis vi vil skrive noe tekst på skjermen:
    # import tekst
    # tekst.skriv_tekst(screen, 100, 40, f"Din score er: {score}", farge=WHITE, bakgrunnsfarge=BLACK)

    # Tegn brettet for hver frame, men ikke kall oppdater hele tiden
    screen.fill(HVIT)
    for kolonne in brett:
        for rute in kolonne:
            rute.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()




# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
