import pygame as pg
import numpy as np
import math

from pg_meny import Knapp
from pg_meny import MENYFARGE, HOVERFARGE

# Ruteinfo
ANTALL_RUTER = 20 # antall ruter i bredden og høyden (20 x 20)
RUTE_STR = 20     # rutenes bredde og høyde

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRAA = (70, 70, 70)

# Farge
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = ANTALL_RUTER * RUTE_STR
MENY_YSTART = 20
MENY_BREDDE = 200
MENY_YAVSTAND = 60  # y-avstand for hver knapp

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = ANTALL_RUTER * RUTE_STR + MENY_BREDDE
VINDU_HOYDE  = ANTALL_RUTER * RUTE_STR
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()


class Rutenett:
  """Klasse for å representere et rutenett"""
  def __init__(self):
    """Konstruktør"""
    self.ruter = [[0]*ANTALL_RUTER for i in range(ANTALL_RUTER)]

  def oppdater(self):
    # Resetter neste status
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        self.ruter[i][j].nesteStatus = self.ruter[i][j].levende

    # Først alle cellene, angi ny status
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        # Nå er vi inne på rute i,j. Da kan vi telle antall naboer
        antall_naboer = 0
        # Går gjennom plassene rundt ruta vår
        for x in [-1, 0, 1]:
          for y in [-1, 0, 1]:
            # Vi må ikke telle med ruta selv
            if not (x == 0 and y == 0):
              # Vi må bare ta med ruter innenfor brettet
              if (i+x >= 0 and i+x < ANTALL_RUTER) and (j+y >= 0 and j+y < ANTALL_RUTER):
                if self.ruter[i+x][j+y].levende:
                  antall_naboer += 1

        # Oppdaterer rutenett-kopien
        if antall_naboer <= 1:
          self.ruter[i][j].nesteStatus = False
        elif antall_naboer == 3:
          self.ruter[i][j].nesteStatus = True
        elif antall_naboer > 3:
          self.ruter[i][j].nesteStatus = False

    # Deretter endre status for alle
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        self.ruter[i][j].oppdater()

class Rute:
  """Klasse for å representere en rute"""
  def __init__(self, rad, kolonne):
    self.rad = rad
    self.kolonne = kolonne
    self.levende = False
    self.nesteStatus = False
    self.farge = HVIT

  def oppdater(self):
    """ Metode for å oppdatere rutens status til neste status """
    self.levende = self.nesteStatus

  def byttTilstand(self):
    """Metode for å gjøre levende celle død og omvendt"""
    self.levende = not self.levende

  def tegn(self, vindu):
    """Metode for å tegne opp en celle i rutenettet"""
    if self.levende:
      self.farge = SVART
    else:
      self.farge = HVIT
    # Tegner selve ruten
    pg.draw.rect(vindu, self.farge, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR))
    # Tegner på en kantlinje rundt ruten
    pg.draw.rect(vindu, GRAA, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR), width=1)

# Funksjon som håndterer museklikk
def museklikk(posisjon):
  xkoordinat = posisjon[0]
  ykoordinat = posisjon[1]

  # Hva ble klikket på?
  # En rute
  if (xkoordinat >= 0 and xkoordinat <= ANTALL_RUTER*RUTE_STR) and (ykoordinat >= 0 and ykoordinat <= ANTALL_RUTER*RUTE_STR):
    x = math.floor(xkoordinat/RUTE_STR)
    y = math.floor(ykoordinat/RUTE_STR)
    rutenett.ruter[x][y].byttTilstand()
  else: # Noe annet (kanskje en knapp)
    for m in meny:
      if m.rektangel.collidepoint(posisjon):
        if m.tekst == "Omstart":
          for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
              rutenett.ruter[i][j].levende = False
        if m.tekst == "Neste":  
          rutenett.oppdater()

meny = [] # liste med knapper

# Lager en omstartsknapp
meny.append(Knapp(MENY_XSTART + 20, MENY_YSTART, "Omstart"))

# Lager en nesteknapp
meny.append(Knapp(MENY_XSTART + 20, MENY_YSTART + MENY_YAVSTAND, "Neste"))

# Lager et rutenett
rutenett = Rutenett()

# Lager rutene
for i in range(ANTALL_RUTER):
  for j in range(ANTALL_RUTER):
    rutenett.ruter[i][j] = Rute(i,j)

    # Trekker tilfeldig ett av tallene 0, 1 eller 2
    tilfeldig = np.random.randint(0,3)
    # Angir cellen som levende hvis tallet er 1 (1/3)
    if tilfeldig == 1:
      rutenett.ruter[i][j].byttTilstand()

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

  # Sjekker om brukeren har lukket vinduet eller klikket med mus
  for event in pg.event.get():
    if event.type == pg.QUIT:
      fortsett = False

    if event.type == pg.MOUSEBUTTONDOWN:
      museklikk(pg.mouse.get_pos())

  # Oppdaterer innholdet
  VINDU.fill(HVIT)

  # Tegner opp alle ruter som døde (hvite) eller levende (svarte) celler
  for i in range(ANTALL_RUTER):
    for j in range(ANTALL_RUTER):
      rutenett.ruter[i][j].tegn(VINDU)

  # Tegner knappene
  musPos = pg.mouse.get_pos()
  for m in meny:
    # Endre farge hvis musen er over knappen (hover)
    if m.rektangel.collidepoint(musPos):
      m.tegn(VINDU, HOVERFARGE)
    else:
      m.tegn(VINDU, MENYFARGE)

  pg.display.flip()
  