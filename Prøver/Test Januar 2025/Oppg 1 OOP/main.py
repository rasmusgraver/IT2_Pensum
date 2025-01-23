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


def dyr_til_fil():
    hund = Hund("Fido")
    katt = Katt("Misse")

    hund.hent_ball()
    hund.hent_ball()
    katt.spis_mus()
    katt.spis_mus()
    katt.spis_mus()

    
    with open("dyr.csv", "w") as fil:
        fil.write("Type;Navn;Baller;Mus\n")  # Skriver overskriften i filen
        hund.skriv_til_fil(fil)
        katt.skriv_til_fil(fil)


dyr_til_fil()
