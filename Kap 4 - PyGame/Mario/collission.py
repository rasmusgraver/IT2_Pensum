from constants import *

def handle_collission(mario, enemy):
    if enemy.dead or mario.dead:
        # Hvis en av de er døde allerede, så sjekker vi ikke...
        return
    mario_rect = mario.image.get_rect( topleft=(mario.x, mario.y) )
    enemy_rect = enemy.image.get_rect( topleft=(enemy.x, enemy.y) )
    if mario_rect.colliderect(enemy_rect):
        if mario.dy > 0 and mario.y < enemy.y: # Hvis Mario er fallende OG han er over goomban
            enemy.looseLife()
            mario.dy = MARIO_JUMP*0.5  # Gi et lite hopp opp
            # og dytt han over enemy:
            mario.y = enemy.y - enemy.height*0.9
        else:
            mario.looseLife()

