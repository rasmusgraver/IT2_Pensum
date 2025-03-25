import json
from pprint import pprint

filnavn = "DataFiler/05994_20240126-145813-json.json"

with open(filnavn, encoding="utf-8") as fil:
  tidsListe = json.load(fil)

# Rydd opp stygt tegn for inntrykk:
for tidsbruk in tidsListe:
    for key in tidsbruk:
        if key == 'alle aktiviteter':
            value = tidsbruk[key]
            if value[1] == " ":
                print(f"{key} med value {value}")
                tidsbruk[key] = "-> " + value[2:]

pprint(tidsListe)
print(f"Antall oppføringer: {len(tidsListe)}")
