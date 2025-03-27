import json
from pprint import pprint

filnavn = "DataFiler/05994_20240126-145813-json.json"

def fiksInnrykk(data):
    # Rydd opp stygt tegn for inntrykk:
  for tidsbruk in data:
      for key in tidsbruk:
          if key == 'alle aktiviteter':
              value = tidsbruk[key]
              if not value[0].isalpha():
                  # print(f"{key} med value {value}")
                  tidsbruk[key] = "-> " + value[2:]

def filtrerData(data, filterKey, filterVerdi):
  nyData = []
  for tidsbruk in data:
      for key in tidsbruk:
          value = tidsbruk[key]
          if key == filterKey and value == filterVerdi:
              # Legg til "hele denne bolken" i den nye lista
              nyData.append(tidsbruk)

  return nyData

def printData(data):
    print("|" + "-"*66 + "|")
    print(f'| {"Aktivitet":42}| {"Kjønn":10}|{"Tidsbruk":10}|')
    print("|" + "-"*66 + "|")
    for tidsbruk in data:
            print(f'| {tidsbruk["alle aktiviteter"]:42}| {tidsbruk["kjønn"]:10}|{tidsbruk["Tidsbruk 2000 I alt"]:10}|')

    print("|" + "-"*66 + "|")


with open(filnavn, encoding="utf-8") as fil:
    tidsListe = json.load(fil)

fiksInnrykk(tidsListe)
# pprint(tidsListe)
# print(f"Antall oppføringer: {len(tidsListe)}")


running = True
while running:
    print("")
    inp = input("Skriv a,m,k for alle, menn eller kvinner. Skriv q for avslutt: ")
    if inp == "q":
        running = False
    elif inp == "a":
        filtData = filtrerData(tidsListe, "kjønn", "Alle")
        printData(filtData)
    elif inp == "m":
        filtData = filtrerData(tidsListe, "kjønn","Menn")
        printData(filtData)
    elif inp == "k":
        filtData = filtrerData(tidsListe, "kjønn", "Kvinner")
        printData(filtData)

