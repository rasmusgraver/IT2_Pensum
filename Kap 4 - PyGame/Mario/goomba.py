from constants import *
from bilder import *
from character import Character

class Goomba(Character):

    def __init__(self, x, y):
        super().__init__(x, y, goomba_img)

    def move(self):
        # Goomba beveger seg med konstant fart mot venstre:
        self.x -= GOOMBA_SPEED
        super().move()



def create_goomba():
    return Goomba(WIDTH, 200)