from random import randint

# MERK: Dette er typisk måte å lage 2-dimensjonal matrise på:
# En liste som består av lister.
# Merk at første rad får vi ved brett[0]
# Første felt (øverst venstre) får vi ved brett[0][0]
brett = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "] 
]

def printBrett():
    for i in range(len(brett)):
        rad = brett[i]
        for j in range(len(rad)):
            end = " | " if j+1<len(rad) else ""
            print(rad[j], end=end)
        if (i+1 < len(brett)):
            print("\n---------")
    print("\n")

def ledig(x,y):
    return brett[x][y] == " "

def sjekkRad(rad):
    if rad[0] == " ": return False
    for j in range(len(rad)):
        if rad[0] != rad[j]:
            return False
    return "HUMAN" if rad[0] == "O" else "COMPUTER"

def vunnet():
    for i in range(len(brett)):
        radSeier = sjekkRad(brett[i])
        if radSeier: return radSeier

    return False

def ledigeFelt():
    for i in range(len(brett)):
        for j in range(len(brett[i])):
            if ledig(i, j):
                return True
    return False

def computerMove():
    x = 1
    y = 1
    while not ledig(x,y):
        x = randint(0,2)
        y = randint(0,2)
    brett[x][y] = "X"




def humanMove():
    while True:
        try:
            x, y = input("Skriv inn rad og kolonne (ex 2 2 for midten)").split()
            x = int(x) - 1
            y = int(y) - 1
            if ledig(x,y):
                brett[x][y] = "O"
                return
            else:
                print("Det feltet er ikke ledig. Prøv igjen")
        except ValueError:
            print("Feil input")
        except IndexError as e:
            print("Utenfor brettet!", e)


while ledigeFelt() and not vunnet():
    printBrett()
    humanMove()
    if ledigeFelt() and not vunnet():
        computerMove()

if vunnet():
    printBrett()
    print(vunnet(), "vant")
else:
    printBrett()
    print("UAVGJORT!")
