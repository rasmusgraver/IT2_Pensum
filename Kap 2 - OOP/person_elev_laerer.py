class Person:
	def __init__(self, id, fornavn, etternavn):
		self.id = id
		self.fornavn = fornavn
		self.etternavn = etternavn

	def __str__(self):
		# Returnerer en "string-representasjon" av objektet
		# MERK: Kan bruke isinstance for å sjekke type objekt self er:
		typePerson = "Lærer" if isinstance(self, Laerer) else "Elev"
		return f"{typePerson}: {self.fornavn} {self.etternavn} (#{self.id})"

	def visInfo(self):
		# Bare printer "sting-representasjonen":
		print(self)
		# Kan også printe ut mer info, basert på hva slags type object self er:
		if isinstance(self, Laerer):
			self.visKontordager()
		if isinstance(self, Elev):
			self.visInstrumenter()

class Laerer(Person):
	def __init__(self, id, fornavn, etternavn, kontor, kontordager):
		super().__init__(id, fornavn, etternavn)
		self.kontor = kontor
		self.kontordager = kontordager

	def visKontordager(self):
		print("Kontordager:", self.kontordager)

class Elev(Person):
	def __init__(self, id, fornavn, etternavn, fodselsaar, instrumenter):
		super().__init__(id, fornavn, etternavn)
		self.fodselsaar = fodselsaar
		self.instrumenter = instrumenter

	def visInstrumenter(self):
		print("Instrumenter:", self.instrumenter)

class Gruppe():
	def __init__(self, navn, klasserom, laerer):
		self.navn = navn
		self.klasserom = klasserom
		self.laerer = laerer
		self.elever = []

	def leggTilElev(self, elev):
		self.elever.append(elev)

	def visGruppeListe(self):
		print("Gruppe", self.navn, "i rom", self.klasserom)
		print(self.laerer) # Bruker __str__ funksjonen fra Person
		if len(self.elever) == 0:
			print("Ingen elever i gruppa")
		else:
			print("     Elev-liste:")
			print("    ", "-"*24)
			for elev in self.elever:
				print("    ", elev) # Bruker __str__ funksjonen fra Person
			print("    ", "-"*24)


# Tester koden vår:
ane = Elev(1, "Ane", "Borch", 2004, ["fiolin", "bass"])
rasmus = Laerer(23, "Rasmus", "Graver", "A201", ["mand", "tirsd", "torsd"])

ane.visInfo()
print()
rasmus.visInfo()
print()

# Og så oppretter vi gruppa:
it2 = Gruppe("IT2", "B203", rasmus)
it2.visGruppeListe()
print()

# og legger til eleven, og viser info på nytt:
it2.leggTilElev(ane)
it2.visGruppeListe()
print()

# Sluttkomentar: Nå er det ingen enkel måte å sjekke hvilken
# gruppe en lærer har, eller en elev tilhører.
# For å løse dette måtte vi også hatt referanse fra Elev og fra Lærer
# til gruppe. Men da blir koden en del større, så jeg droppa det her...