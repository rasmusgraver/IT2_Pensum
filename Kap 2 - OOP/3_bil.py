class Bil:
    def __init__(self, modell, farge, årstall):
        self.modell = modell
        self.farge = farge
        self.årstall = årstall

    def __str__(self):
        return f"Jeg er en {self.farge} {self.modell} fra {self.årstall}"

a = Bil("Audi", farge="blå", årstall="1978")



class Elbil(Bil):
    def __init__(self, modell, farge, årstall, batteriKapasitet):
        super().__init__(modell, farge, årstall)
        self.batteriKapasitet = batteriKapasitet

    def __str__(self):
        return f"Jeg er en Elbil {self.farge} {self.modell} fra {self.årstall} med kapasitet {self.batteriKapasitet}"

a = Bil("Audi", farge="blå", årstall="1978")
t = Bil("Toyota", "rød", 2012)
tes = Elbil("Tesla", "Rød", 2020, 80)

print("Mine biler:")
a.visInfo()
print(tes)
