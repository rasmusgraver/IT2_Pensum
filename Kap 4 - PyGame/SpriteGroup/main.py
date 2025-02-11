import pygame as pg
from constants import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)

from square import Square
from player import Player

square_group = pg.sprite.Group()
link = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

running = True
while running:

    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            square = Square(x, y)
            square_group.add(square)

    square_group.update()
    square_group.draw(screen)

    # Tegner link etter firkantene, så han er på toppen
    link.update()
    link.draw(screen)

    # Check for collission: 
    # Merk: Bruker True på "dokill" for å fjerne firkanten om det er kollisjon
    pg.sprite.spritecollide(link, square_group, dokill=True)

    # print("Number of squares", len(square_group))

    pg.display.flip() # flip eller update - same, same

pg.quit()
