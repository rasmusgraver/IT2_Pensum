import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "DataFiler/aksjekurs.csv"

datoer = []
aksjekurs = []

with open(filnavn) as fil:
        linje = next(fil)
        print(linje)

        for rad in fil:
            rader = rad.split(";")
            date_object = datetime.strptime(rader[0], "%Y-%m-%d")
            datoer.append( date_object  )
            aksjekurs.append(float(rader[1]))

plt.plot(datoer, aksjekurs, color="green")
plt.xlabel("Tid")
plt.ylabel("Aksjekurs")
plt.title("Aksjekurs første halvår 2023")
# plt.xticks(datoer[::10], rotation=70)
plt.tight_layout()
plt.show()