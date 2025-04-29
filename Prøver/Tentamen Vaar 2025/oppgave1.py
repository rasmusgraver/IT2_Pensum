class Person():
  pass


def hovedprogram():
  brad = Person("Brad Pitt")
  brad.visStatus()    # Jeg er singel.

  angie = Person("Angelina Jolie")
  brad.gifteMeg(angie)
  brad.visStatus()    # Jeg er gift med Angelina Jolie.

  cameron = Person("Cameron Diaz")
  brad.gifteMeg(cameron)   # Beklager Cameron Diaz. Jeg er allerede gift med Angelina Jolie.

  cameron.gifteMeg(brad)   # Brad Pitt er allerde gift med Angelina Jolie.
  cameron.visStatus()      # Jeg er singel.

  cameron.faaBarn("Rosa Diaz")   # Cameron Diaz er singel og kan ikke få barn.
  angie.faaBarn("Rosa Jolie-Pitt")   # Angelina Jolie og Brad Pitt har fått barn: Rosa Jolie-Pitt.

  print(f"Barnet til brad og angie er {brad.barn}.") # Barnet til brad og angie er Rosa Jolie-Pitt.
  print(f"Som er samme som {angie.barn}.") # Som er samme som Rosa Jolie-Pitt.

# Kaller på hovedprogrammet:
hovedprogram()
