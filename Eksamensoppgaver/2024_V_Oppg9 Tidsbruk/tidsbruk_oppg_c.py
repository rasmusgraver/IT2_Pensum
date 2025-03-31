import json
from pprint import pprint
import matplotlib.pyplot as plt

filnavn = "DataFiler/05994_20240126-145813-json.json"

def fiksInnrykk(data):
    # Rydd opp stygt tegn for inntrykk:
    for ordbok in data:
        for key in ordbok:
            if key == 'alle aktiviteter':
                value = ordbok[key]
                if not value[0].isalpha():
                    # print(f"{key} med value {value}")
                    ordbok[key] = "-> " + value[2:]

def fiksMinuttTilDesimaltall(data):
    # Det som kommer etter punktum i tidsbruk er antall minutter
    # => Gjør det om til et desimaltall
    for ordbok in data:
        for key in ordbok:
            if key == 'Tidsbruk 2000 I alt':
                tid = str(ordbok[key])
                tidsArr = tid.split(".")
                time = tidsArr[0]
                # MERK: Her bruker jeg ints og sammenslåing av strings
                # Kunne alternativt ha regnet ut desimal som 0 komma .....
                # og så regnet timer + desimal
                desimal = 0
                if len(tidsArr) == 2:
                    minutt = int(tidsArr[1])
                    desimal = round(100*minutt/60)
                # (time, minutt) = tid.split(".")
                # print(key, time, desimal)
                ordbok[key] = float(str(time) + "." + str(desimal))


def filtrerData(data, filterKey, filterVerdi):
    nyData = []
    for ordbok in data:
        for key in ordbok:
            value = ordbok[key]
            if key == filterKey and value == filterVerdi:
                # Legg til "hele denne bolken" i den nye lista
                nyData.append(ordbok)

    return nyData

def printData(data):
    print("|" + "-"*66 + "|")
    print(f'| {"Aktivitet":42}| {"Kjønn":10}|{"Tidsbruk":10}|')
    print("|" + "-"*66 + "|")
    for tidsbruk in data:
            print(f'| {tidsbruk["alle aktiviteter"]:42}| {tidsbruk["kjønn"]:10}|{tidsbruk["Tidsbruk 2000 I alt"]:10}|')

    print("|" + "-"*66 + "|")

def stolpeDiagram(data):
    x_verdier = []
    y_verdier = []
    farger = []
    for ordbok in data:
        if ordbok["alle aktiviteter"] != "I alt":
            # and  ordbok["alle aktiviteter"][0] != "-":
            x_verdier.append(ordbok["alle aktiviteter"])
            y_verdier.append(ordbok["Tidsbruk 2000 I alt"])
            if ordbok["alle aktiviteter"][0] == "-":
                farger.append("blue")
            else:
                farger.append("red")

    #subplot(rader, kolonner, figurnr)
    plt.subplot(1, 2, 1)
    # plt.title("Tidsbruk 2000")
    # plt.xlabel("Aktivitet")
    # plt.ylabel("Tidsbruk")
    plt.bar(x_verdier, y_verdier, color=farger)
    # plt.legend()
    # plt.xticks(x_verdier, rotation=45)
    plt.xticks(rotation=90, fontsize=6 )
    plt.tight_layout()
    # plt.show()

def sektorDiagram(data):
    x_verdier = []
    y_verdier = []
    for ordbok in data:
        # Ta bare "topp-postene" her (sum-postene - "i alt"):
        if ordbok["alle aktiviteter"] != "I alt" \
               and  ordbok["alle aktiviteter"][0] != "-":
            x_verdier.append(ordbok["alle aktiviteter"])
            y_verdier.append(ordbok["Tidsbruk 2000 I alt"])

    #subplot(rader, kolonner, figurnr)
    plt.subplot(1, 2, 2)
    # plt.title("Tidsbruk 2000")
    # plt.xlabel("Aktivitet")
    # plt.ylabel("Tidsbruk")
    plt.pie(y_verdier, labels=None)
    # plt.legend()
    # plt.legend(loc="upper left")
    plt.legend(x_verdier, loc="lower right", fontsize=6)

    # plt.xticks(x_verdier, rotation=45)
    # plt.xticks(rotation=90, fontsize=6 )
    # plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    # plt.tight_layout()
    plt.show()


with open(filnavn, encoding="utf-8") as fil:
    tidsListe = json.load(fil)

fiksInnrykk(tidsListe)
fiksMinuttTilDesimaltall(tidsListe)
# pprint(tidsListe)
# print(f"Antall oppføringer: {len(tidsListe)}")

running = True
filtData = None
while running:
    print("")
    inp = input("Skriv a,m,k for alle, menn eller kvinner. Skriv q for avslutt: ")
    if inp == "q":
        running = False
    elif inp == "a":
        filtData = filtrerData(tidsListe, "kjønn", "Alle")
    elif inp == "m":
        filtData = filtrerData(tidsListe, "kjønn","Menn")
    elif inp == "k":
        filtData = filtrerData(tidsListe, "kjønn", "Kvinner")

    if filtData and running:
        printData(filtData)
        stolpeDiagram(filtData)
        sektorDiagram(filtData)

    # Om man bare vil kjøre 1 gang i loopen:
    running = False

