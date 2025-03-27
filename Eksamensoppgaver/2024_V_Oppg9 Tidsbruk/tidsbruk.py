import json
from pprint import pprint

filnavn = "DataFiler/05994_20240126-145813-json.json"

with open(filnavn, encoding="utf-8") as fil:
    tidsListe = json.load(fil)


# Fjern "stygt tegn":
for ordbok in tidsListe:
    for key in ordbok.keys():
        value = ordbok[key]
        if key == "alle aktiviteter" and not value[0].isalpha():
            ordbok[key] = "->  " + value[2:]

pprint(tidsListe)


for ordbok in tidsListe:
    print(f'{ordbok["alle aktiviteter"]:42} | {ordbok["kjønn"]:10}')

