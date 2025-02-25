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

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def oppdater(self):
        self.x += self.dx 
        self.y += self.dy
        # Sjekk om vi kolliderer i veggen:
        # Hvis vi gjør det, så snu retning på dx/dy
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy

    def kollisjon(self, ball):
        x_avst_kvadrat = (self.x - ball.x)**2
        y_avst_kvadrat = (self.y - ball.y)**2
        avst_mellom_ballene = (x_avst_kvadrat + y_avst_kvadrat)**0.5
        if (avst_mellom_ballene < self.radius + ball.radius):
            # Snu alle retningene:
            self.dx = -self.dx
            self.dy = -self.dy
            ball.dx = -ball.dx
            ball.dy = -ball.dy

ball1 = Ball(farge=BLUE, radius=40, x=50, y=100, dx=5, dy=3)
ball2 = Ball(farge=GREEN, radius=20, x=200, y=200, dx=-5, dy=3)


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
    ball1.tegn(screen)
    ball2.tegn(screen)
    # Flytt ballen:
    ball1.oppdater()
    ball2.oppdater()

    # Sjekk om ballene kolliderer:
    ball1.kollisjon(ball2)

    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
