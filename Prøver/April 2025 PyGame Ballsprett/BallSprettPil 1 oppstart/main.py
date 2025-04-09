import pygame as pg
from constants import *
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)

from ruby import Ruby

ruby = Ruby()

def draw_background(screen):
    screen.fill(LIGHT_BLUE)
    # Tegner gresset:
    grass_start_x = 0
    grass_end_x = SCREEN_WIDTH
    grass_start_y = SCREEN_HEIGHT - GRASS_HEIGHT
    grass_end_y = SCREEN_HEIGHT
    pg.draw.rect(screen, GREEN, (grass_start_x, grass_start_y, grass_end_x, grass_end_y))
    # Tegner en sol:
    sun_radius = 40
    sun_x = SCREEN_WIDTH - sun_radius - 10
    sun_y = sun_radius + 10
    pg.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)


running = True
while running:
    clock.tick(FPS)
    draw_background(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    ruby.oppdater()
    ruby.tegn(screen)

    pg.display.flip() # flip eller update - same, same

pg.quit()

