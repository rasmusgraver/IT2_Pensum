class Bok:
   def __init__(self, tittel, forfatter):
       self.tittel = tittel
       self.forfatter = forfatter
       self.utlånt = None  # Skal være en referanse til en Låner eller None

   def visInfo(self):
       status = f"Utlånt til Låner {self.utlånt.lånerID}" if self.utlånt else "Tilgjengelig"
       print(f"Tittel: {self.tittel}, Forfatter: {self.forfatter}, Status: {status}")


class Låner:
   def __init__(self, lånerID):
       self.lånerID = lånerID
       self.lånteBøker = []

   def lånBok(self, bok):
       if bok.utlånt is not None:
           raise Exception(f"Boken '{bok.tittel}' er allerede utlånt.")
       bok.utlånt = self
       self.lånteBøker.append(bok)
       print(f"Låner {self.lånerID} har lånt '{bok.tittel}'.")

   def leverTilbakeBok(self, bok):
       if bok not in self.lånteBøker:
           raise Exception(f"Låner {self.lånerID} har ikke lånt boken '{bok.tittel}'.")
       bok.utlånt = None
       self.lånteBøker.remove(bok)
       print(f"Låner {self.lånerID} har levert tilbake '{bok.tittel}'.")

# Testprogram
def test_bibliotek():
   # Opprett bøker
   bok1 = Bok("Python slange", "Anna Lovinda")
   bok2 = Bok("Objektorientering", "Per Vers")
   bok3 = Bok("Algoritmer", "Willy Knikkersen")

   # Opprett låner
   låner1 = Låner(1)

   # Lån ut bok1 og bok2
   låner1.lånBok(bok1)
   låner1.lånBok(bok2)

   # Vis informasjon om bøkene
   bok1.visInfo()
   bok2.visInfo()
   bok3.visInfo()

   # Prøv å låne ut en bok som allerede er utlånt
   try:
       låner1.lånBok(bok1)
   except Exception as e:
       print("Feil:", e)

   # Returner en bok
   låner1.leverTilbakeBok(bok1)

   # Bekreft at den nå kan lånes på nytt
   låner1.lånBok(bok1)

   # Prøv å levere en bok som ikke er lånt
   try:
       låner1.leverTilbakeBok(bok3)
   except Exception as e:
       print("Feil:", e)

test_bibliotek()
