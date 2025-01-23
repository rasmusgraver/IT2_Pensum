class Dyr:
    def __init__(self, navn):
        self.navn = navn


class Hund(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
        self.antall_baller = 0
    
    def hent_ball(self):
        self.antall_baller += 1

    def __str__(self):
        return f"Hunden {self.navn} har hentet {self.antall_baller} baller"

    def skriv_til_fil(self, fil):
        fil.write(f"Hund;{self.navn};{self.antall_baller};0\n")

class Katt(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
        self.antall_mus = 0

    def spis_mus(self):
        self.antall_mus += 1
    
    def __str__(self):
        return f"Katten {self.navn} har spist {self.antall_mus} mus"

    def skriv_til_fil(self, fil):
        fil.write(f"Katt;{self.navn};0;{self.antall_mus}\n")




