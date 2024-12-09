# Oppgave 1 fra "1D_Lister.pdf"
# MERK - bare c og d oppgaven
ord = ["xax", "er", "foff", "and", "em", "nu", "nei", "nuet", "nan", 
"momom", "sopp", "ost", "yax"]

ant = 0
for o in ord:
	if len(o) >= 3:
		ant += 1
print(f"Det er {ant} ord med 3 eller flere tegn")


ant = 0
for o in ord:
	if len(o) >= 3 and o[0] == o[-1]:
		ant += 1
print(f"Det er  {ant} ord med 3 eller flere tegn, som også har lik første og siste bokstav")
