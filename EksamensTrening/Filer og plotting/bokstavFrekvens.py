from pprint import pprint
import json

txtFil = "DataFiler/norge.txt"

bokstavDict = {}

with open(txtFil, encoding="utf-8") as fil:
  innhold = fil.read()
  for bokstav in innhold:
    b = bokstav.lower()
    if b.isalpha():
      if b in bokstavDict:
        bokstavDict[b] += 1
      else:
        bokstavDict[b] = 1

pprint(bokstavDict)
print(f"Antall keys: {len(bokstavDict)}")

jsonFilNavn = "DataFiler/norgeFrekvens.json"
json_object = json.dumps(bokstavDict, indent=4)
with open(jsonFilNavn, "w") as outfile:
    outfile.write(json_object)

