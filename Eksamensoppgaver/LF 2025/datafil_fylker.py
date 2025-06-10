import matplotlib.pyplot as plt
import numpy as np
import csv

# Klasse for å holde orden på data for hvert fylke
class Fylke:
   """Klasse for å representere data for ett fylke"""
   def __init__(self, fylke:str):
       """Konstruktør"""
       self.fylke = fylke
       self.aktivitet = {} # Ordiste med aktivitet og antall for dette fylket
       self.deltagere = 0  # Totalt i fylket

   def leggTilAktivitet(self,aktivitet:str,antall:int):
       self.aktivitet[aktivitet] = antall
       self.deltagere += antall

   def visAktiviteterSortert(self):
       """Skriver ut informasjon om aktivitetene i stigende rekkefølge etter antall"""
       sortert = dict(sorted(self.aktivitet.items(), key=lambda x: x[1]))
       print(f"Fylke: {self.fylke}.")
       for navn,antall in sortert.items():
           prosent = (antall/self.deltagere)*100
           print(f"{navn}: antall = {antall}, andel = {round(prosent,1)}%.")

   def visDiagram(self):
       """Viser et søylediagram med de tre mest populære aktivitetene"""
       sortert = dict(sorted(self.aktivitet.items(),reverse=True, key=lambda x: x[1]))
       merkelapper = []
       verdier = []
       for navn, antall in sortert.items():
           merkelapper.append(navn)
           verdier.append(antall)

       # Vise de tre mest populære aktivitetene i et søylediagram
       plt.figure(figsize=(10, 5))
       plt.bar(merkelapper[0:3],verdier[0:3])
       plt.ylim(120, max(verdier) + 10)
       plt.xlabel("Aktivitet")
       plt.ylabel("Deltagere")
       plt.title(f"Populære aktiviteter i {self.fylke}.")
       plt.xticks(rotation=5)
       plt.show()

# Liste for å holde på fylke-objekter
fylke = []

# Ordliste med informasjon om totalt antall deltagere pr aktivitet
aktivitet = {}

# Leser inn datasettet
filnavn = "friluftsaktiviteter.csv"

with open(filnavn, encoding="latin-1") as fil:
   filinnhold = csv.reader(fil, delimiter=";")

   rad1 = next(filinnhold)    # Navn på fylkene
   # Opprette fylkes objektene
   for i in range(1,len(rad1)):
     fylkeNavn = rad1[i][23:]   # Posisjonen til fylkesnavnet
     nyttFylke = Fylke(fylkeNavn)
     fylke.append(nyttFylke)

   # Legge til friluftsaktivitetene pr fylke og totalt
   for rad in filinnhold:
       totalt = 0  # Deltagere pr aktivitet
       for i in range(1,len(rad)-1): # En og en kolonne
           fylke[i].leggTilAktivitet(rad[0],int(rad[i]))
           totalt += int(rad[i])
       # Lagre totalt antall deltagere pr aktivitet
       aktivitet[rad[0]] = totalt

# Funksjon for å skrive ut deltagere pr aktivitet i tabellform
def visTabell():
 print("")
 # Siden navnene på aktivitetene har veldig ulik lengde, skriver jeg en aktivitetpå hver linje
 print(f"{'Aktivitet':60} Deltagere")
 for navn, antall in aktivitet.items():
   print(f"{navn:60}  {antall}")
 print("")

visTabell()

def velgFylke():
   print("")
   for i in range(0,len(fylke)):
       print(f"{i+1}: {fylke[i].fylke}")
   fylkeIndeks = int(input("Velg et fylke ved å skrive tallet foran: "))
   fylke[fylkeIndeks-1].visAktiviteterSortert()
   fylke[fylkeIndeks-1].visDiagram()

velgFylke()
