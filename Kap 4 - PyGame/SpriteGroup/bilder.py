import pygame as pg
from constants import *

bg_image = pg.image.load("assets/bg.png")
bg_image = pg.transform.scale(bg_image, SCREEN_SIZE)

link_d = pg.image.load("assets/link_d.png").convert_alpha()
link_u = pg.image.load("assets/link_u.png").convert_alpha()
link_r = pg.image.load("assets/link_r.png").convert_alpha()
link_l = pg.transform.flip(link_r, True, False)
