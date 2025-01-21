import matplotlib.pyplot as plt
import csv

# Oppg 1 a) Gjennomsnittsfunksjon:
def gjennomsnitt_av_liste(liste):    
    totalt = sum(liste)
    lengde = len(liste)
    return totalt / lengde

# Tester
print("-"*30)
print("Tester gjennomsnitt_av_liste:")
print(gjennomsnitt_av_liste([1, 2, 3]))              # Skal printe 2.0
print(gjennomsnitt_av_liste([2, 2, 3]))              # Skal printe 2.333...
print(gjennomsnitt_av_liste([1, 2, 3, 3, 2, 7, 6]))  # Skal printe 3.42857..

# Oppg 1 b) Plotte aksjekurs:
filnavn = "DataFiler/aksjekurs.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    print("-"*30)
    overskrifter = next(filinnhold)
    print(overskrifter)
    print("-"*30)

    # Listene vi skal plotte:
    datoer = []
    kurs_liste = []
    # Det blir for trangt å printe alle datoer: Vi lagrer bare hver 10ende, og bruker det som "xticks"
    labels = []
    ticks = []

    i = 0
    for rad in filinnhold:
        datoer.append(rad[0])
        kurs_liste.append(float(rad[1]))
        # Lagrer hver 10ende til å bruke som "xticks"
        # MERK: Det er en mer fancy/enklere måte å gjøre det på, som gjør
        #       at vi ikke trenger å generere "labels" og "ticks" (se lenger ned i koden)
        if i%10 == 0:
            labels.append(rad[0])
            ticks.append(i)
        i += 1


# Oppg 1 c) Legg til rullerende gjennomsnitt: 
snitt_liste = []
lengde = len(kurs_liste)
for i in range(lengde):
    # Skal gå 5 skritt bakover, og 5 skritt frem i listen, MEN kan ikke gå
    # lenger bakover enn 0, eller lenger frem en lengden av kurs-listen:
    start = max(0, i-5)
    slutt = min(lengde, i+5)
    snitt = gjennomsnitt_av_liste(kurs_liste[start:slutt])
    snitt_liste.append(snitt)


plt.plot(datoer, kurs_liste, label="aksjekurs")
plt.plot(datoer, snitt_liste, label="snittkurs 10 dager")

plt.xlabel("Dato")
plt.ylabel("Kurs")
plt.legend(loc="upper left")

# Det blir for mange datoer: Bare vis hver 10ende:
# MERK: Det holder å gi med listen over labels:
plt.xticks(labels, rotation=90)

# Fancy, og enklere, måte å skrive det på: Generer listen "her og nå":
# plt.xticks(datoer[::10], rotation=90)

# Tight layout gjør at vi får plass til å se etikettene på x-aksen (datoene)
plt.tight_layout()

plt.show()

