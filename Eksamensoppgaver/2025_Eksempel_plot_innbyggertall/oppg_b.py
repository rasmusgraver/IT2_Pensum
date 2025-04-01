import csv

"""
Filformat: Jeg har valgt å erstatte alle forekomster av \t (tabs)
med ; (semikolon)
"""

filnavn = "DataFiler/Datasett_fodselstall.csv"

def printOverskrifter():
    print(f'{"År":5} | {"Fødsler":10} | {"Innflytt":10} | {"Utflytt":10} | {"Folkvekst":10}')
    print("-"*57)


def printRad(rad):
    vekst = ".."
    if rad[0] != ".." and rad[1] != ".." and rad[2] != "..":
        vekst = int(rad[0]) + int(rad[1]) - int(rad[2])

    # Bruker > for å høyrestille
    print(f"{rad[0]:>5} | {rad[1]:>10} | {rad[2]:>10} | {rad[3]:>10} | {vekst:>10}")

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    # print(overskrifter)

    printOverskrifter()
    # Oppgave b) Utvid programmet ved å legge til kolonnen «netto folkevekst» i visningen.
    # Feltene i denne skal være beregnet ut ifra de tre andre.
    # Formelen er:
    # Folkevekst = fødsler+innflytt-utflytt
    for rad in filinnhold:
        printRad(rad)

