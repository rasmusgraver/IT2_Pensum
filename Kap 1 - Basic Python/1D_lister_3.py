# Oppgave 3 fra "1D_Lister.pdf"
tall1 = [7, 24, 10, 26, 35, 10, 29, 2, 29, 40, 40, 26, 16, 8, 9, 26, 
5, 18, 9, 13, 40, 28, 37, 32, 6, 11, 35, 9, 26, 6, 11, 2, 10, 11, 
27, 4, 8, 22, 40, 19]
tall2 = [56, 49, 28, 52, 58, 33, 26, 27, 58, 36, 36, 48, 55, 25, 58, 
57, 30, 27, 36, 39, 58, 50, 58, 28, 56, 52, 21, 39, 22, 27, 48, 37, 
20, 32, 38, 31, 31, 25, 42, 54]

def fjernDuplikater(liste):
	nyListe = []
	for el in liste:
		if not el in nyListe:
			nyListe.append(el)
	return nyListe

print(f"tall1 uten duplikater: {fjernDuplikater(tall1)}")
print(f"tall2 uten duplikater: {fjernDuplikater(tall2)}")


def elementerIBeggeLister(liste1, liste2):
	lst = []
	for el in liste1:
		if el in liste2 and not el in lst:
			lst.append(el)
	return lst
print(f"Elemeter som finnes i begge lister: {elementerIBeggeLister(tall1, tall2)}")

def elementerIkkeBeggeLister(liste1, liste2):
	lst = []
	for el in liste1:
		if el not in liste2 and not el in lst:
			lst.append(el)
	for el in liste2:
		if el not in liste1 and not el in lst:
			lst.append(el)
	lst.sort() # så den blir enklere å lese
	return lst
print(f"Elemeter som IKKE finnes i begge lister: {elementerIkkeBeggeLister(tall1, tall2)}")
