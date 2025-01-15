import pygame as pg


def handle_collission(mario, goomba):
    if goomba.dead or mario.dead:
        # Hvis en av de er døde allerede, så sjekker vi ikke...
        return
    mario_rect = mario.image.get_rect(topleft=(mario.x, mario.y))
    goomba_rect = goomba.image.get_rect()
    goomba_rect.x = goomba.x
    goomba_rect.y = goomba.y
    if mario_rect.colliderect(goomba_rect):
        if mario.y < goomba.y and mario.dy > 0:
            goomba.dead = True
        else:
            mario.dead = True
