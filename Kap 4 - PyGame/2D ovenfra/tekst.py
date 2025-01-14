import pygame as pg



# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 32)

def skriv_tekst(screen, x, y, tekst, farge):
    # Lager en tekst-surface:
    tekst_surface = font.render(tekst, True, farge)
    # Tegner teksten på skjermen:
    screen.blit(tekst_surface, (x, y))

