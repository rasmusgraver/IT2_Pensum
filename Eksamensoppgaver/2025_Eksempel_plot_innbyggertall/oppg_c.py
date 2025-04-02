import csv
import matplotlib.pyplot as plt

"""
Filformat: Jeg har valgt å erstatte alle forekomster av \t (tabs)
med ; (semikolon)
"""

filnavn = "DataFiler/Datasett_fodselstall.csv"


def beregnVekst(rad):
    vekst = ".."
    if rad[1] != ".." and rad[2] != ".." and rad[3] != "..":
        # Formelen er:    Folkevekst = fødsler+innflytt-utflytt
        vekst = int(rad[1]) + int(rad[2]) - int(rad[3])
    return vekst

def visDiagram(aar, vekst):
    plt.plot(aar, vekst, marker='o')
    plt.xticks(aar[::2], rotation=45)
    plt.title(f"Netto folkevekst i perioden {min(aar)}-{max(aar)}")
    # plt.xlabel("År")
    plt.ylabel("Netto Folkevekst")
    plt.grid()
    plt.show()



with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    # print(overskrifter)

    # printOverskrifter()
    # Oppgave c) Utvid programmet til å vise et egnet diagram som viser utviklingen 
    # for «netto folkevekst» for en valgfri periode mellom 1945 og 2024.  
    # Man skal kunne velge start- og sluttår i brukergrensesnittet.

    start = int(input("Startår: "))
    slutt = int(input("Sluttår: "))

    gyldig = True
    if start >= slutt:
        print("Ugyldig: Slutt må være etter start")
        gyldig = False

    if start < 1945 or start > 2024:
        print("Start må være mellom 1945 og 2024")
        gyldig = False

    if slutt < 1945 or slutt > 2024:
        print("Slutt må være mellom 1945 og 2024")
        gyldig = False

    if gyldig:
        aarListe = []
        vekstListe = []
        for rad in filinnhold:
            aar = int(rad[0])
            if start <= aar <= slutt:
                vekst = beregnVekst(rad)
                if isinstance(vekst, (int, float)):
                    aarListe.append(aar)
                    vekstListe.append(vekst)

        visDiagram(aarListe, vekstListe)
