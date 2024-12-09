from random import randint 

kast = [0]*6
print(kast)

for _ in range(100):
    indeks = randint(0,5)
    kast[indeks] += 1

print(kast)
