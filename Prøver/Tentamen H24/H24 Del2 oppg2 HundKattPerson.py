
"""
Oppgave 2 a): Lag Dyr, Hund og Katt, med "siLyd()"
"""

class Dyr:
    def __init__(self, navn):
        self.navn = navn
    def __str__(self):
        return self.navn
    def siLyd(self):
        print("...")

class Hund(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
    def siLyd(self):
        print("Bjeff")

class Katt(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
    def siLyd(self):
        print("Mjau")

bolivar = Hund("Bolivar")
bolivar.siLyd()
sussi = Katt("Sussi")
sussi.siLyd()


"""
Oppgave 2 b) Klassen Person med metoden leggTilDyr. 
             En person kan eie 0 eller 1 hund og samme med katt
"""

class Person:
    def __init__(self, navn):
        self.navn = navn
        self.katt = None
        self.hund = None
    def __str__(self):
        return f"Personen {self.navn} med hund: {self.hund} og katt: {self.katt}"

    def leggTilDyr(self, dyr):
        if isinstance(dyr, Katt):
            self.leggTilKatt(dyr)
        elif isinstance(dyr, Hund):
            self.leggTilHund(dyr)
        else:
            raise ValueError("Kan ikke legge til et dyr som ikke er hverken hund eller katt")

    def leggTilKatt(self, katt):
            if self.katt != None:
                raise ValueError(f"Personen {self.navn} har allerede en katt: {self.katt.navn}")
            self.katt = katt
    def leggTilHund(self, hund):
            if self.hund != None:
                raise ValueError(f"Personen {self.navn} har allerede en hund: {self.hund.navn}")
            self.hund = hund

rasmus = Person("Rasmus")
print(rasmus)
rasmus.leggTilDyr(bolivar)
print(rasmus)
rasmus.leggTilDyr(sussi)
print(rasmus)

# Får en ValueError: Rasmus har allerede en hund (Bolivar)
hund = Hund("Balder")
rasmus.leggTilDyr(hund)
