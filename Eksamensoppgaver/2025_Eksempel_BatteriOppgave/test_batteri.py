from batteri import Batteri

batteri = Batteri("AK123", 80)

antallFeil = 0
batteri.ladOpp(10)
if (batteri.visEnergiNivå() != 10):
    print(f"Batteriet burde ha vært 10 nå, men var {batteri.visEnergiNivå()}")
    antallFeil += 1

batteri.ladOpp(10)
if (batteri.visEnergiNivå() != 20):
    print(f"Batteriet burde ha vært 20 nå, men var {batteri.visEnergiNivå()}")
    antallFeil += 1

batteri.brukEnergi(0.1)
if (batteri.visEnergiNivå() != 19.9):
    print(f"Batteriet burde ha vært 19.9 nå, men var {batteri.visEnergiNivå()}")
    antallFeil += 1


# Tester med feil datatype
try:
    batteri.brukEnergi("asv")
    # Skal ikke komme hit, fordi vi har en feil datatype:
    antallFeil += 1
    print("Skulle fått feil datatype på brukEnergi() med string")
except ValueError as forventetFeil:
    print(f"Fikk forventet feil: {forventetFeil}")
except Exception as uventetFeil:
    antallFeil += 1
    print(f"Fikk en uventet feil: {uventetFeil} av type {type(uventetFeil)}")


print(f"Ferdig med testene, med totalt {antallFeil} feil")
