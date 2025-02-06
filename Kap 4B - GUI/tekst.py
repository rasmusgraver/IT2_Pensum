import pygame as pg


# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 32)

def skriv_tekst(screen, x, y, tekst, farge, bakgrunnsfarge):
    # Lager en tekst-surface:
    tekst_surface = font.render(tekst, True, farge)
    # Lager en bakgrunns-surface:
    back_surface = pg.Surface(tekst_surface.get_size())
    back_surface.fill(bakgrunnsfarge)
    # Putter teksten på bakgrunnen:
    back_surface.blit(tekst_surface, (0, 0))
    # Tegner bakgrunnen på skjermen:
    screen.blit(back_surface, (x, y))


