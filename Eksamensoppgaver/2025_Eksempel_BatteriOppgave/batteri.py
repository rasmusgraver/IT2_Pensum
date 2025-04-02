# Løsning på Eksempel-eksamensoppgave oppgave 6

class Batteri:
    def __init__(self, batteriId, energiKapasitet):
        if (energiKapasitet <= 0):
            raise "Kan ikke lage batteri med 0 eller negativ kapasitet"
        self.batteriId = batteriId
        self.energiKapasitet = energiKapasitet
        self.energiNivå = 0

    def ladOpp(self, energi):
        if self.energiNivå + energi > self.energiKapasitet:
            # Diskuterte litt i klassen om man skal printe eller raise Exception
            # Begge deler er greit, men gjør det enklere å teste denne feilen med raise.
            # Alternativ 3: Om du returnerer en feilmelding som en tekst-streng
            return "Du kan ikke lade over kapasiteten til batteriet"
            # print("Du kan ikke lade over kapasiteten til batteriet")
            # raise Exception("Du kan ikke lade over kapasiteten til batteriet")
        else:
            self.energiNivå += energi

    def brukEnergi(self, energi):
        if not isinstance(energi, (int, float)):
            # Samme som på ladOpp funksjonen: 3 måter å håndtere feil på:
            # 1: Print en feilmelding
            # 2: Raise Exception
            raise ValueError("Feil datatype")
            # 3: Returner en streng som forklarer feilen return "Feil datatype"
        self.energiNivå -= energi

    def visEnergiNivå(self):
        return self.energiNivå
    
