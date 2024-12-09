import mystisk as m

tekst = "Hei på deg"
krypt = m.hokuspokus(tekst, 2)

print(krypt)
print()

# dekrypt = m.simsalabim(krypt, 2)
dekrypt = m.hokuspokus(krypt, -2)

print(dekrypt)

