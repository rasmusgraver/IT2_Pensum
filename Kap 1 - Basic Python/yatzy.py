import random

# Generelt i funksjonene: t er en liste med 5 tall (våre ternigner)
# MERK: En "0" på en terning betyr at den er klar
# til å bli kastet (skal ikke beholdes)


# Funksjon: Fylle "de ledige plassen" i "t" med tilfeldige tall
# dvs: Alle terninger som viser "0" skal erstattes med 
# et tilfeldig tall
def kast(t):
	# Går igjennom de 5 terningene:
	for i in range(5):
		# Om terningen viste 0: Bytt til et tilfeldig tall (1 - 6)
		if t[i] == 0:
			t[i] = random.randint(1,6) 


# Funksjon: Gå igjennom tallene i "t" og returner det tallet som
# går igjen oftest (høyest "frekvens")
def finnTalletSomSkalBeholdes(t):
	vinner = 0 # hva er "vinnertallet" - som skal beholdes
	max_frekvens = 0 # hva er den høyeste frekvensen (til nå)
	for tall in range(1,7): # Gå igjennom de 6 mulighetene en terning kan vise:
		frekvens = 0     # Starter med å si at tallet ikke finnes på noen av terningene
		for j in range(5):
			if t[j] == tall: # Hvis terningen viser tallet, så øker vi frekvensen
				frekvens += 1

		if frekvens > max_frekvens: # Har vi en ny "vinner"?
			max_frekvens = frekvens
			vinner = tall

	return vinner

# Funksjon: Fjern alle terninger som ikke er riktig "tall"
# Dvs: Sett dem til 0, dersom de ikke viser "det de skal"
def forkastAlleSomIkkeErTalletMitt(tall, t):
	for i in range(5):
		if t[i] != tall:
			t[i] = 0


# Funksjon: Spill en omgang Yatzy, og se om du fikk Yatzy til slutt!
# Nå har vi alle byggeblokkene (funskjonene over), og vi kan
# begynne å spille Yatzy!
# MERK: Returnerer True/False: Fikk vi Yatzy eller ikke?
def spill():
	t = [0,0,0,0,0] # starter med "tomme" terninger for hvert spill
	for i in range(3): # Vi har 3 kast på oss
		kast(t)
		tall = finnTalletSomSkalBeholdes(t)
		forkastAlleSomIkkeErTalletMitt(tall, t)
	if totalt <= 1000:
		print("FERDIG. Terningene viser:", t)
	return t == [tall]*5


# Og så til selve hoved-programmet vårt: 
# MERK: Frem til nå har vi bare definert funksjoner!
# MERK: Se hvor enkelt og pent hovedprogrammet blir! :)
yatzy = 0
totalt = 10000
for i in range(totalt):
	if spill(): # MERK: spill() returnerer True/False
		yatzy += 1
		if totalt <= 1000:
			print("----------YATZY!!!---------------")

print()
print(f"Du fikk Yatzi i {yatzy*100/totalt:.2f} prosent av spillene")

