# Hente ut elementer:
liste = [1, 2, "a", "b", "her er jeg"]
print(liste[0])   # Første element
print(liste[1])   # andre element
print(liste[-1])  # Nest siste element
print(liste[1:3]) # en "sub-liste"

# Legge til og fjerne elementer:
liste.append(88)          # Legg til til slutt
print(liste)
liste.insert(0, "k")      # legg til på starten (indeks 0)
print(liste)
liste.pop(1)              # fjerne andre elementet i lista
print(liste)
liste.remove("b")         # finn og fjern "b" => DEN FØRSTE! KUN 1!
print(liste)

tall = [3, 1, 2, 6, 8, 2, 7, 7]
# Gå igjennom alle elementer:
for x in tall:
    print(" -", x)

# Sjekk om elementet er i lista:
if 1 in tall:
    print("1 er i lista")
else:
    print("1 er ikke i lista")
if 9 in tall:
    print("9 er i lista")
else:
    print("9 er ikke i lista")
