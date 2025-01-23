import csv
from dyr import Hund, Katt

# Les dataene fra fila dyr.csv, og gjennopprett objekter fra dem:
filnavn = "dyr.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    # print(overskrifter)

    dyrene = []
    for rad in filinnhold:
        if (rad[0] == "Hund"):
            dyr = Hund(rad[1])
            dyr.antall_baller = int(rad[2])
        elif (rad[0] == "Katt"):
            dyr = Katt(rad[1])
            dyr.antall_mus = int(rad[3])
        else:
            print("Ukjent dyr:", rad[0])

        if (dyr):
            dyrene.append(dyr)


# Skriv ut alle dyrene:
for dyr in dyrene:
    print(dyr)
