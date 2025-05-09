import pygame
import sys

# Konstanter
BREDDE, HØYDE = 800, 600
RADER, KOLONNER = 20, 20
CELLESTØRRELSE = BREDDE // KOLONNER
PALETT_HØYDE = 50

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (200, 200, 200)
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
pygame.init()

# Setter opp skjermen
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Tegnebrett")

# Lager en todimensjonal liste som representerer brettet, 
# der hver rute har fargen hvit
brett = [[HVIT for k in range(KOLONNER)] for r in range(RADER)]

# Valgt farge
valgtFarge = HVIT

# Funksjon for å tegne opp brettet
def tegnBrett():
  for rad in range(RADER):
    for kol in range(KOLONNER):
      pygame.draw.rect(skjerm, brett[rad][kol], (kol * CELLESTØRRELSE, rad * CELLESTØRRELSE, CELLESTØRRELSE, CELLESTØRRELSE))
      pygame.draw.rect(skjerm, GRÅ, (kol * CELLESTØRRELSE, rad * CELLESTØRRELSE, CELLESTØRRELSE, CELLESTØRRELSE), 1)

# Funksjon for å tegne opp fargepaletten
def tegnPalett():
  for i in range(len(FARGER)):
    pygame.draw.rect(skjerm, FARGER[i], (i * CELLESTØRRELSE, HØYDE - PALETT_HØYDE, CELLESTØRRELSE, PALETT_HØYDE))
    pygame.draw.rect(skjerm, GRÅ, (i * CELLESTØRRELSE, HØYDE - PALETT_HØYDE, CELLESTØRRELSE, PALETT_HØYDE), 1)

while True:
  for hendelse in pygame.event.get():
    if hendelse.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif hendelse.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      if y >= HØYDE - PALETT_HØYDE:
        valgtFarge = FARGER[x // CELLESTØRRELSE]
      else:
        rad, kol = y // CELLESTØRRELSE, x // CELLESTØRRELSE
        brett[rad][kol] = valgtFarge

  skjerm.fill(HVIT)
  tegnBrett()
  tegnPalett()
  pygame.display.flip()
