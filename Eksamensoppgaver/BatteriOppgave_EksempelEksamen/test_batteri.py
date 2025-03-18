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
    print(f"Batteriet burde ha vært 19.1 nå, men var {batteri.visEnergiNivå()}")
    antallFeil += 1


# Tester med feil datatype
forventetFeil = batteri.brukEnergi("asv")
if forventetFeil != "Feil datatype":
    print(f"Forventet en feil med feil datatype, men fikk {forventetFeil}")
    antallFeil += 1

print(f"Ferdig med testene, med totalt {antallFeil} feil")
