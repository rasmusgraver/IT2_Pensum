import json
from pprint import pprint 

"""
Felter i dataene:
    model - navn på bilen
    mpg Miles/(US) gallon
    cyl Number of cylinders
    disp Displacement (cu.in.)
    hp Gross horsepower
    drat Rear axle ratio
    wt Weight (1000 lbs)
    qsec 1/4 mile time
    vs Engine (0 = V-shaped, 1 = straight)
    am Transmission (0 = automatic, 1 = manual)
    gear Number of forward gears
    carb Number of carburetors
"""

filnavn = "DataFiler/mtcars.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

biler = []
for bil in data:
    if int(bil["hp"]) > 200:
        print( "HP: " + str(bil["hp"]) + ": " + bil["model"] )
        biler.append(bil)


# Bruker denne til sorted funksjonen
def sort_key(b):
	return b["hp"]

biler = sorted(biler, key=sort_key, reverse=False)

print("SORTED")
print("="*30)
for bil in biler:
    print("HP: " + str(bil["hp"]) + ": " + bil["model"] )