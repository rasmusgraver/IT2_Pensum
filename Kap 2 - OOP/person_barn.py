class Person:
	def __init__(self, navn, alder = 0):
		self.navn = navn
		self.alder = alder
		self.barn = []
		self.mor = None
		self.far = None

	def __str__(self):
		return f"{self.navn}, mor: {Person.kortVersjon(self.mor)}, far: {Person.kortVersjon(self.far)}. \n    Barn: {self.barnSomTekst()}"

	def barnSomTekst(self):
		return list(map(Person.kortVersjon, self.barn))

	def kortVersjon(pers):
		return pers.navn if pers else "-"

	def setMor(self, mor):
		self.mor = mor
		mor.barn.append(self)

	def setFar(self, far):
		self.far = far
		far.barn.append(self)


m = Person("MAmma")
p = Person("PAPpa")
b1 = Person("Kari")
b2 = Person("Ole")
bb = Person("Baby")

b1.setMor(m)
b1.setFar(p)
b2.setMor(m)
b2.setFar(p)
bb.setFar(b2)

print(m  , "\n")
print(p  , "\n")
print(b1 , "\n")
print(b2 , "\n")

print("-----")
# Kan printe barna til mor: 
print(m.barn[0].navn) # "Kari"
print(m.barn[1].navn) # "Ole"

print(".....")
# Eller barnet til Ole sitt navn: 
print(m.barn[1].barn[0].navn) # "Baby"
# Kan til og med skrive ut faren til barne-barnet sitt navn! :) 
print(m.barn[1].barn[0].far.navn) # "Ole"


