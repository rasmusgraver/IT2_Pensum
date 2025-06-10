# Oppgave 9 Skogbrann
import pygame
import random

# --- Konfigurasjon ---
celleStørrelse = 10
antallKolonner = 80
antallRader = 60

treVekstSjanse = 0.003    # 0.3 %
lynSjanse = 0.0003        # 0.03 %
bilderPerSekund = 10

# --- Farger ---
HVIT = (255, 255, 255)
GRØNN = (34, 139, 34)
ORANSJE = (255, 140, 0)

# --- Tilstander ---
TOM = "tom"
TRE = "tre"
BRENNER = "brenner"

class Celle:
   def __init__(self):
       self.tilstand = TOM
       self.nyTilstand = TOM

   def erTre(self):
       return self.tilstand == TRE

   def brenner(self):
       return self.tilstand == BRENNER

   def vokser(self):
       if self.tilstand == TOM and random.random() < treVekstSjanse:
           self.tilstand = TRE

   def blirTruffetAvLyn(self):
       if self.tilstand == TRE and random.random() < lynSjanse:
           self.tilstand = BRENNER

class Skog:
   def __init__(self, kolonner, rader):
       self.kolonner = kolonner
       self.rader = rader
       self.rutenett = [[Celle() for _ in range(kolonner)] for _ in range(rader)]
       self.brannPågår = False

   def oppdater(self):
       if self.brannPågår:
           self.spredBrann()
       else:
           self.voksOgSjekkLyn()

   def voksOgSjekkLyn(self):
       for rad in self.rutenett:
           for celle in rad:
               celle.vokser()

       for rad in self.rutenett:
           for celle in rad:
               celle.blirTruffetAvLyn()
               if celle.brenner():
                   self.brannPågår = True
                   return

   def spredBrann(self):
       # Bestem ny tilstand for hver celle
       for y in range(self.rader):
           for x in range(self.kolonner):
               celle = self.rutenett[y][x]
               if celle.brenner():
                   celle.nyTilstand = TOM
                   # Sjekk naboer
                   for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                       naboX = x + dx
                       naboY = y + dy
                       if 0 <= naboX < self.kolonner and 0 <= naboY < self.rader:
                           nabo = self.rutenett[naboY][naboX]
                           if nabo.erTre():
                               nabo.nyTilstand = BRENNER
               else:
                   celle.nyTilstand = celle.tilstand

       # Oppdater tilstanden til alle celler
       for rad in self.rutenett:
           for celle in rad:
               celle.tilstand = celle.nyTilstand

       # Sjekk om det fortsatt brenner et sted
       brannFortsatt = False
       for rad in self.rutenett:
           for celle in rad:
               if celle.brenner():
                   brannFortsatt = True
                   break
           if brannFortsatt:
               break

       self.brannPågår = brannFortsatt

   def tegn(self, skjerm):
       for y in range(self.rader):
           for x in range(self.kolonner):
               celle = self.rutenett[y][x]
               farge = HVIT
               if celle.tilstand == TRE:
                   farge = GRØNN
               elif celle.tilstand == BRENNER:
                   farge = ORANSJE

               pygame.draw.rect(
                   skjerm,
                   farge,
                   (x * celleStørrelse, y * celleStørrelse, celleStørrelse, celleStørrelse)
               )

# --- Hovedprogram ---
def hoved():
   pygame.init()
   skjermBredde = antallKolonner * celleStørrelse
   skjermHøyde = antallRader * celleStørrelse
   skjerm = pygame.display.set_mode((skjermBredde, skjermHøyde))
   pygame.display.set_caption("Skogbrannsimulering")

   klokke = pygame.time.Clock()
   skog = Skog(antallKolonner, antallRader)
   fortsett = True

   while fortsett:
       for hendelse in pygame.event.get():
           if hendelse.type == pygame.QUIT:
               fortsett = False

       skog.oppdater()
       skjerm.fill(HVIT)
       skog.tegn(skjerm)
       pygame.display.flip()
       klokke.tick(bilderPerSekund)

   pygame.quit()

if __name__ == "__main__":
   hoved()

   