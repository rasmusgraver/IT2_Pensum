# Kast en terning (virtuelt…) 100 ganger og plot som et stolpediagram antall 1,2,3,4,5,6ere. 
# Det finnes en «rett fram» enkel måte å gjøre dette på. 

# I denne fila:
# Utfordring: Etter du har gjort den enkle varianten: Kan du lagre alle kastene som en liste med 100 elementer i (hvert kast). Og så undersøke histogram plotting? (HINT: Lag 6 «bins») 
import random
import matplotlib.pyplot as plt

restultater = []

# MERK! Litt endring fra timen: Morsommere å se på summen av terninger
# Da får vi flere utfall, og vi kan se at det nærmer seg en normal-fordeling - moro! :) 
for i in range(1000):
    kast1 = random.randint(1,6)
    kast2 = random.randint(1,6)
    kast3 = random.randint(1,6)
    restultater.append(kast1 + kast2 + kast3)

# print(restultater)

plt.hist(restultater, bins=7)
plt.show()
