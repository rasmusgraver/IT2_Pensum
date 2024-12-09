class Kvadrat:

    def __init__(self, sidelengde, farge="Sort"):
        self.sidelengde = sidelengde
        self.farge = farge

    def __str__(self):
        return f"Jeg er et kvadrat med farge {self.farge} og sidelengde {self.sidelengde}. Jeg har omkrets {self.omkrets()} og areal {self.areal()}"

    def printInfo(self):
        print(f"Jeg er et kvadrat med farge {self.farge} og sidelengde {self.sidelengde}. Jeg har omkrets {self.omkrets()} og areal {self.areal()}")

    def omkrets(self):
        return self.sidelengde * 4 
    
    def areal(self):
        return self.sidelengde**2

