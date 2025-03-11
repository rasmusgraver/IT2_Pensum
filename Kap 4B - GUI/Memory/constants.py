# Definer andre konstanter som hastigheter osv her:
RUTE_STR = 60
GAP = 10

ANT_X = 4
ANT_Y = 4

# Definerer størrelsen på pygame-vinduet:
GAME_WIDTH = ANT_X * (RUTE_STR + GAP)

WIDTH = GAME_WIDTH + 200 # Setter av plass til knappene
HEIGHT = ANT_Y * (RUTE_STR + GAP)
SIZE = (WIDTH, HEIGHT)

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = GAME_WIDTH + 50
MENY_YSTART = 50
MENY_YAVSTAND = 80  # y-avstand for hver knapp

# Definerer Frames Per Second:
FPS = 60


# Noen farger vi kan bruke:
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (200, 200 , 0)
