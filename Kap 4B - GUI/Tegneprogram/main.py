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



running = True
while running:

    clock.tick(FPS)
    skjerm.fill(HVIT)

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_pos, y_pos = pg.mouse.get_pos()
            print(f"Musklikk ({x_pos}, {y_pos})")


    # Fyll inn oppdatering og tegning av objektene her:



    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
