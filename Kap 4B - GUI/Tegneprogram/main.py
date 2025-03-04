import pygame as pg

# Konstanter
BREDDE, HOYDE = 800, 600
RADER, KOLONNER = 20, 20
CELLESTR = BREDDE // KOLONNER
PALETTSTR = 50
FPS = 60

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRAA = (200, 200, 200)
FARGER = [
  (255, 0, 0),   # Rød
  (0, 255, 0),   # Grønn
  (0, 0, 255),   # Blå
  (255, 255, 0), # Gul
  (255, 165, 0), # Oransje
  (0, 255, 255), # Cyan
  (255, 0, 255)  # Magenta
]

# Initialiser pygame
pg.init()

# Setter opp skjermen
skjerm = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Tegnebrett")
clock = pg.time.Clock()



brett = [[HVIT for k in range(KOLONNER)] for r in range(RADER)]

def tegn_ruter():
    for x in range(RADER):
        for y in range(KOLONNER):
            farge = brett[x][y]
            x_pos = x * CELLESTR
            y_pos = y * CELLESTR
            pg.draw.rect(skjerm, farge, (x_pos, y_pos, CELLESTR, CELLESTR))
            pg.draw.rect(skjerm, GRAA, (x_pos, y_pos, CELLESTR, CELLESTR), 1)

def tegn_palett():
    for i in range(len(FARGER)):
        farge = FARGER[i]
        y = HOYDE - PALETTSTR
        x = i * PALETTSTR
        pg.draw.rect(skjerm, farge, (x, y, PALETTSTR, PALETTSTR))


# Sett opp "initielle verdier"
running = True
valgt_farge = FARGER[0]
tegner = False

while running:

    clock.tick(FPS)
    skjerm.fill(HVIT)

    # MERK: Vi kan alltid spørre om mouse.get_pos() - også når brukeren ikke klikker
    # Vi bruker x_pos og y_pos flere steder nedover, så lagrer dem her med en gang
    x_pos, y_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            tegner = True
            # print(f"Musklikk ({x_pos}, {y_pos})")
            if HOYDE - PALETTSTR <= y_pos <= HOYDE:
                # print("Du er i palett-høyde")
                if 0 <= x_pos <= len(FARGER)*PALETTSTR:
                    # print("Du er i palette-bredde")
                    farge_indeks = x_pos // PALETTSTR
                    farge = FARGER[farge_indeks]
                    print(f"Du har valgt farge nr {farge_indeks} som er {farge}")
                    valgt_farge = farge
                    tegner = False # Det var ikke museklikk for å begynne å tegne

        elif event.type == pg.MOUSEBUTTONUP:
            tegner = False


    if tegner:
        x = x_pos // CELLESTR
        y = y_pos // CELLESTR
        if x < RADER and y < KOLONNER:
            brett[x][y] = valgt_farge


    # Fyll inn oppdatering og tegning av objektene her:
    tegn_ruter()
    # PASS PÅ: Paletten må tegnes etter rutene - den ligger "oppå" rutene
    tegn_palett()

    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
