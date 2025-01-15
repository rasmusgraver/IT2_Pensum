import pygame as pg


def handle_collission(mario, goomba):
    if goomba.dead or mario.dead:
        # Hvis en av de er døde allerede, så sjekker vi ikke...
        return
    mario_rect = mario.image.get_rect()
    goomba_rect = goomba.image.get_rect()
    # TODO: Les om rect.colliderect (google it)
    # TODO: Disse "rect" objektene er plassert på (0,0) - du må "dytte dem" på rett plass
    #       for at colliderect skal fungere
