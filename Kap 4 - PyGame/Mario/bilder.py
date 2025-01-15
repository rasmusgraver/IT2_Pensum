import pygame as pg

bg_image = pg.image.load("assets/bg.png").convert_alpha()
mario_image = pg.image.load("assets/mario.png").convert_alpha()
goomba_img = pg.image.load("assets/goomba.png").convert_alpha()

bg_image = pg.transform.scale(bg_image, (1024, 704))
mario_image = pg.transform.scale(mario_image, (50, 50))
goomba_img = pg.transform.scale(goomba_img, (50, 50))
goomba_img = pg.transform.flip(goomba_img, True, False)
