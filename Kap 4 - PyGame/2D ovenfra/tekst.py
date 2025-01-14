import pygame as pg


# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 32)

def skriv_tekst(screen, x, y, tekst, farge):
    bilde = font.render(tekst, True, farge)
    screen.blit(bilde, (x, y))
