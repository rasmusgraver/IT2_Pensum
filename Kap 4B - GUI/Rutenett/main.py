import pygame as pg
from constants import *
from rute import Rute

# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)


# Her setter du opp objektene dine:
brett = []
for x in range(ANT_X):
    y_verdier = []
    for y in range(ANT_Y):
        rute = Rute(x,y)
        y_verdier.append(rute)
    brett.append(y_verdier)


print(brett[0][0]) # "Jeg er rute (0,0)"
print(brett[5][2]) # "Jeg er rute (5,2)"


animasjons_teller = 0
running = True
while running:

    animasjons_teller += 1

    clock.tick(FPS)
    screen.fill(WHITE)

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_pos, y_pos = pg.mouse.get_pos()
            print(f"Musklikk ({x_pos}, {y_pos})")
            x = x_pos // RUTE_STR
            y = y_pos // RUTE_STR
            rute = brett[x][y]
            print("Du klikket på rute", rute)
            rute.klikk()
            animasjons_teller = 0 # Reset animasjons-telleren når vi klikker på en rute


    # Fyll inn oppdatering og tegning av objektene her:
    if animasjons_teller > 40:
        animasjons_teller = 0
        for rad in brett:
            for rute in rad:
                rute.oppdater(brett)


    # Tegn brettet for hver "frame":
    for rad in brett:
        for rute in rad:
            rute.tegn(screen)



    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
