

def handle_collission(mario, goomba):
    if goomba.dead or mario.dead:
        # Hvis en av de er døde allerede, så sjekker vi ikke...
        return
    mario_rect = mario.image.get_rect( topleft=(mario.x, mario.y) )
    goomba_rect = goomba.image.get_rect( topleft=(goomba.x, goomba.y) )
    if mario_rect.colliderect(goomba_rect):
        if mario.dy > 0 and mario.y < goomba.y: # Hvis Mario er fallende OG han er over goomban
            goomba.dead = True
        else:
            mario.dead = True

