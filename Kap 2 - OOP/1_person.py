class Person:

    def __init__(self, fornavn, etternavn, alder):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
    
    def siHei(self):
        print(f"{self.fornavn} sier hei!")
    
    def erMyndig(self):
        if self.alder >= 18:
            print(f"{self.fornavn} er myndig (Alder: {self.alder})")
        else:
            print(f"{self.fornavn} er ikke myndig (Alder: {self.alder})")

    # Øker alderen til personen med 1 år
    def bliEldre(self):
        pass # Fyll inn! 

t = Person("Tommy", "Normann", 16)
t.erMyndig()
t.bliEldre()
t.erMyndig()
t.bliEldre()
t.erMyndig()
