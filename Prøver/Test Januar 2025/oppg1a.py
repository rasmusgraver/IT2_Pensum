from dyr import Katt, Hund

def dyr_print():
    hund = Hund("Fido")
    katt = Katt("Misse")

    hund.hent_ball()
    hund.hent_ball()
    katt.spis_mus()
    katt.spis_mus()
    katt.spis_mus()

    print(hund)
    print(katt)



dyr_print()
