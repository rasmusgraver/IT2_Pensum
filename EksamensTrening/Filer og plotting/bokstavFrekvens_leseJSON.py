import json
from pprint import pprint

filnavn = "DataFiler/norgeFrekvens.json"

# DISSE LINJENE MÅ DERE KUNNE! (Eller altså "ha i verktøykassa")
with open(filnavn, encoding="utf-8") as fil:
  bokstavDict = json.load(fil)

pprint(bokstavDict)
print(f"Antall keys: {len(bokstavDict)}")

# OPPGAVE:
# Sorter etter antall forekomster, og hent ut top 10
# ... og plot dem som søylediagram! 

# Denne hjalp ikke: (Men nyttig å vite om...)
# Sorterer på keys: sortertDict = dict(sorted(bokstavDict.items()))

# Sorterer på values: (Den er jo ganske "gresk", men nå har vi den i verktøykassa vår)
sortertDict = dict(sorted(bokstavDict.items(), key=lambda item: item[1], reverse=True))

# NB!!: MERK!!! pprint sorterer dict på keys av seg selv! Så her må vi bruke "vanlig print"!!
# print(sortertDict)

# Dette fungerer ikke - fungerer bare på lister! top10 = sortertDict[:9]
# Må bruke mer fancy google stuff:
from itertools import islice
top10 = dict(islice(sortertDict.items(), 10))

print("TOP 10")
print("="*20)
print(top10)


# Konverter til relativ frekvens: Må hente ut total forekomst av alle bokstaver:
totalForekomst = 0
for key in bokstavDict:
  antall = bokstavDict[key]
  totalForekomst += antall

print(f"Total bokstav forekomst: {totalForekomst}")

# Gjør om vår top 10 til relativ frekvens:
for key in top10:
  value = top10[key]
  relativForekomst = value/totalForekomst
  # Lagrer ny verdi på denne nøkkelen:
  top10[key] = round(relativForekomst*100, 1) # Ganger med hundre for prosent


print("TOP 10 - med relativ prosent forekomst")
print("="*20)
print(top10)


# Og plotter bar-diagram av det:
import matplotlib.pyplot as plt

# Lager diagram som viser oversikt over antall turer for hver ukedag
plt.bar(top10.keys(), top10.values(), color="green")
plt.title("Frekvensanalyse norske bokstaver")
plt.xlabel("bokstav")
plt.ylabel("Relativ frekvens (%)")
plt.show()
