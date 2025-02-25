import pygame as pg
from constants import *
from ball import Ball

# Start opp PyGame:
pg.init()
# Lag en klokke:
clock = pg.time.Clock()
# Start PyGame vinduet:
screen = pg.display.set_mode(SIZE)



def start_forfra():
    baller = [] # Sett til tom liste, og fyll med 1 ball
    baller.append(Ball(farge=YELLOW, radius=10, x=50.0, y=100.0, dx=3.0, dy=2.0))
    return baller


# En liste med ballene. Starter med 1, også blir det en ny ball når de treffer kanten
baller = start_forfra()
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
    screen.fill(WHITE) 

    # Liten sikkerhetsfunksjon... Så det ikke blir HELT fullt på skjermen, og pygame slutter å svare
    if len(baller) > 1000:
        baller = start_forfra()


    # Flytt ballen, OG ta vare på nye baller som oppstår:
    nye_baller = []
    for ball in baller:
        ny_ball = ball.oppdater()
        if ny_ball: # Må sjekke om vi fikk en ny ball (eller None hvis ikke - teller som "false")
            nye_baller.append(ny_ball)

    # Merge de nye ballene inn sammen med de eksisterende:
    baller.extend(nye_baller)
    # MERK måten jeg gjorde dette på: Ikke push nye baller inn i listen før vi er ferdig med å iterere gjennom og oppdatere ballene!
    # Hvis man gjør det så blir den "for ball in baller" forvirret - ikke endre "baller" i en slik for-løkke - det skaper kluss!

    # Tegn ballene:
    for ball in baller:
        ball.tegn(screen)

    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
