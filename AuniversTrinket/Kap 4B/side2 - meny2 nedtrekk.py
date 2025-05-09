import pygame as pg
from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

# Farger
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer et vindu
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 400
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hver knapp

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Funksjon som håndterer museklikk
def museklikk(posisjon):
    for m in meny:
        # Hvis listen er aktiv så vises alternativene. Klikk utenfor deaktiverer listen.
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(posisjon)

        elif m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)

# En liste med menyelementer
meny = []

# Lager en nedtrekksliste
meny.append(
    Nedtrekksliste(
        MENY_XSTART, MENY_YSTART, ["Gjøk", "Sisik", "Trost", "Stær"]
    )
)

# Gjenta helt til brukeren lukker vinduet
fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

    for m in meny:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    # Tegn de aktive nedtrekkslistene (som viser sine alternativer)
    for m in meny:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)

    pg.display.flip()

pg.quit()
