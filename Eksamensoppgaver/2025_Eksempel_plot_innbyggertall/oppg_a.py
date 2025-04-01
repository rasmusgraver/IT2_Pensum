import csv

"""
Filformat: Jeg har valgt å erstatte alle forekomster av \t (tabs)
med ; (semikolon)
"""

filnavn = "DataFiler/Datasett_fodselstall.csv"

def printOverskrifter():
    print(f'{"År":5} | {"Fødsler":10} | {"Innflytt":10} | {"Utflytt":10}')
    print("-"*44)

def printRad(rad):
    # Bruker > for å høyrestille
    print(f"{rad[0]:>5} | {rad[1]:>10} | {rad[2]:>10} | {rad[3]:>10}")



with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    # print(overskrifter)

    printOverskrifter()
    # Oppgave a) Lag et program som presenterer data fra datasettet i en 
    # tabellignende visning med kolonnene
    #  «fødselstall», «innflyttinger» og «utflyttinger».
    for rad in filinnhold:
        printRad(rad)

