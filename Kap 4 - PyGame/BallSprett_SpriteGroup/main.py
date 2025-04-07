import pygame as pg
from constants import *
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)

from ball import Ball

ball_group = pg.sprite.Group()

ball1 = Ball(farge=BLUE, radius=40, x=50, y=100, dx=5, dy=7)
ball2 = Ball(farge=PURPLE, radius=30, x=350, y=200, dx=-5, dy=3)
ball3 = Ball(farge=YELLOW, radius=20, x=150, y=200, dx=-3, dy=-2)

ball_group.add(ball1, ball2, ball3)

running = True
while running:
    clock.tick(FPS)
    screen.fill(LIGHT_BLUE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    """
        # Opprett ball med museklikk:

        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            farge = random.choice(COLOR_LIST)
            radius = random.randint(10, 50)
            dx = random.randint(-3, 5)
            dy = random.randint(-4, 4)
            ball = Ball(farge=farge, radius=radius, x=x, y=y, dx=dx, dy=dy)
            ball_group.add(ball)        
    """


    # MERK: Disse to funksjonene er litt forskjellige:
    # - update() kaller update funksjonen på hver ball
    # - draw() kaller IKKE draw funksjon på ballen, men "blitter" ball.image på screen
    ball_group.update()
    ball_group.draw(screen)


    # Hmm. Denne ble fortsatt ikke noe pen da...
    for ball1 in ball_group:
        for ball2 in ball_group:
            if ball1 != ball2:
                ball1.kollisjon(ball2)


    pg.display.flip() # flip eller update - same, same

pg.quit()

