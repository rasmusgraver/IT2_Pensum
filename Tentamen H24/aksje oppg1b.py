import matplotlib.pyplot as plt
from datetime import datetime


filnavn = "DataFiler/aksjekurs.csv"

datoer = []
aksjekurs = []

with open(filnavn) as fil:
        overskrifter = next(fil)
        print(overskrifter)

        for rad in fil:
            rader = rad.split(";")
            datoer.append(rader[0])
            aksjekurs.append(rader[1])

plt.plot(datoer, aksjekurs, color="green")
plt.xlabel("Tid")
plt.ylabel("Aksjekurs")
plt.title("Aksjekurs første halvår 2023")
# plt.xticks(datoer[::10], rotation=90)
# plt.tight_layout()
plt.show()