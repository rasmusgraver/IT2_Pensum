import pygame as pg
from constants import *

# Initialiser pygame
pg.init()

from rute import Rute
from maur import Maur
from pg_meny import Knapp

# Setter opp skjermen
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Langtons maur")
clock = pg.time.Clock()


# Her setter du opp objektene dine:
knapper = []
knapper.append(Knapp(MENY_XSTART, MENY_YSTART, "Flytt"))
knapper.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, "Restart"))
knapper.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND*2, "Animasjon"))
knapper.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND*3, "Avslutt"))


def restart():
    # Sett opp brettet:
    global brett, maur
    brett = []
    for x in range(ANT_X):
        y_verdier = []
        for y in range(ANT_Y):
            rute = Rute(x,y)
            y_verdier.append(rute)
        brett.append(y_verdier)

    maur = Maur(ANT_X//2,ANT_Y//2)

def museklikk():
    global running, animasjon_running, animasjon_counter
    x_pos, y_pos = pg.mouse.get_pos()

    for knapp in knapper:
        if knapp.rektangel.collidepoint( (x_pos, y_pos) ):
            print(f"Klikket på: {knapp.tekst}")
            if knapp.tekst == "Flytt":
                maur.flytt(brett)
            if knapp.tekst == "Restart":
                restart()
            if knapp.tekst == "Animasjon":
                animasjon_running = not animasjon_running
                animasjon_counter = 0
                knapp.toggleFarge()
            if knapp.tekst == "Avslutt":
                running = False

    # Sjekk om vi trykket på en rute:
    # Trengs ikke her?
    # x = x_pos // RUTE_STR
    # y = y_pos // RUTE_STR
    # if x < ANT_X and y < ANT_Y:
    #    rute = brett[x][y]
    #    print("Du klikket på rute", rute)
    #    rute.klikk()


# Sett opp "initielle verdier"
running = True
animasjon_running = False
animasjon_counter = 0
restart()

while running:
    animasjon_counter += 1
    clock.tick(FPS)
    screen.fill(WHITE)
    # Den litt fancy siste oppgaven - med å flytte mauren gradvis
    maur.animer()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            museklikk()

    # Dersom animasjon er aktivert: Flytt maur hvert halve sekund:
    if animasjon_running and animasjon_counter > FPS//2:
        maur.flytt(brett)
        animasjon_counter = 0


    # Tegn ruter og knapper:
    for rad in brett:
        for rute in rad:
            rute.tegn(screen)

    maur.tegn(screen)

    for knapp in knapper:
        knapp.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
