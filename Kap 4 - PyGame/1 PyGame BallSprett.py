import pygame as pg

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Definerer størrelsen på pygame-vinduet:
WIDTH = 300
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

# Definerer Frames Per Second:
FPS = 60

# Start opp PyGame:
pg.init()
# Lag en klokke:
clock = pg.time.Clock()
# Start PyGame vinduet:
screen = pg.display.set_mode(SIZE)



class Ball:

    def __init__(self, farge, radius, x, y, dx, dy):
        self.farge = farge
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx 
        self.dy = dy 

    def oppdater(self):
        self.x += self.dx 
        self.y += self.dy
        # Sjekk om vi kolliderer i veggen:
        # Hvis vi gjør det, så snu retning på dx/dy
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy


ball1 = Ball(farge=BLUE, radius=40, x=50, y=100, dx=5, dy=3)



running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Klokka sørger for rett hastighet (ut i fra FPS):
    clock.tick(FPS)
    screen.fill(WHITE)

    # Tegn ballen:
    # TODO: Lag en funksjon for dette: ball1.tegn(screen)
    pg.draw.circle(screen, ball1.farge, (ball1.x, ball1.y), ball1.radius)
    # Flytt ballen:
    ball1.oppdater()

    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
