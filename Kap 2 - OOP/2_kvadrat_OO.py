class Kvadrat:

    def __init__(self, sidelengde, farge="Sort"):
        self.sidelengde = sidelengde
        self.farge = farge

    def printInfo(self):
        print(f"Jeg er et kvadrat med farge {self.farge} og sidelengde {self.sidelengde}. Jeg har omkrets {self.omkrets()} og areal {self.areal()}")

    def omkrets(self):
        return self.sidelengde * 4 
    
    def areal(self):
        return self.sidelengde**2


# Test Klassen vår, ved å opprette ulike Objekter med ulike sidelengder
k1 = Kvadrat(farge="Blå" , sidelengde=1)
k2 = Kvadrat(2, "Rød")
k3 = Kvadrat(3)
k1.printInfo()
k2.printInfo()
