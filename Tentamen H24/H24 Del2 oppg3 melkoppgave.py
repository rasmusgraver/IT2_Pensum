
'''
Oppgavetekst:

- Velg et firesifret tall
- Algoritme:
	- Sorter tallet i stigende rekkefølge, OG i synkende rekkefølge. Dette kaller du t1 og t2
	  (eksempel: Om tallet er 1392, så blir t1=1239 og t2=9321)
	- Så tar du differansen mellom disse to tallene: t2 - t1
	- Dette er ditt nye tall. Om tallet er 3-sifret, så legger du til en 0 foran på det. 
- Følg denne algoritmen 20 ganger. Om du har gjort det rett, så kommer det samme tallet på nytt og på nytt etterhvert. Hvilket tall er det?
'''

tall = 1391

for i in range(20):
	# Gjør tallet om til tekst, så vi kan enkelt legge på 0 foran, og sortere tekst-strengen:
	tall = str(tall)
	if len(tall) == 2:
		tall = "0" + tall
	if len(tall) == 3:
		tall = "0" + tall
	# Tekster kan enkelt sorteres (husk, de er som en liste av bokstaver):
	t1 = sorted(tall)
	t2 = sorted(tall, reverse=True)

	# Gjør tallene tilbake igjen til tall:
	t1 = int(''.join(t1))
	print("t1", t1)
	t2 = int(''.join(t2))
	print("t2", t2)

	tall = t2 - t1
	print("tallet er nå:", tall)

# Tallet som kommer igjen og igjen etterhvert er 6174
# Dette tallet kalles Kaprekars konstant (Hentet fra en Q-melk :)