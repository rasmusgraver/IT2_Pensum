# Kast en terning (virtuelt…) 100 ganger og plot som et stolpediagram antall 1,2,3,4,5,6ere. 
# Det finnes en «rett fram» enkel måte å gjøre dette på. 

# I fil 2:
# Utfordring: Etter du har gjort den enkle varianten: Kan du lagre alle kastene som en liste med 100 elementer i (hvert kast). Og så undersøke histogram plotting? (HINT: Lag 6 «bins») 

import random
import matplotlib.pyplot as plt

# FORRIGE FIL:
# Lagrer en liste som tar vare på antall
# 1,2,3,4,5,6ere (MERK: Lite "indeks problem")

# DENNE FILA:
# Alternativ løsning: Lag en ordbok der
# "kastet" er nøkkel, og verdien er antallet
resultater = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(100):
    kast = random.randint(1,6)
    resultater[kast] += 1

# MERK: Se så pent man kan bar-plotte ordbøker!
plt.bar(resultater.keys(), resultater.values())
plt.show()
