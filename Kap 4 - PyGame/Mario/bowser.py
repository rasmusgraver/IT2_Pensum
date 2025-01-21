from constants import *
from bilder import *
from character import Character

class Bowser(Character):

    def __init__(self, x, y):
        super().__init__(x, y, bowser_img)
        self.vx = -BOWSER_SPEED

    def move(self):
        self.x += self.vx
        super().move()
        # Flip speed when hitting the sides of the screen:
        if self.x < 0 or self.x > WIDTH - self.width:
            self.vx *= -1



def create_bowser():
    return Bowser(WIDTH-160, 100)