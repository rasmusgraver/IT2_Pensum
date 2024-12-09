def f(liste):
    liste[0] = "A"

l = [1,2,3]
f(l) # MERK: Listen blir endret "globalt"!
print(l)

# HUSK: Dette var ikke tilfelle i forrige eksempel, der vi sendte
# inn en variabel med verdien 2 - selvom funksjonen gjør endringer
# på verdien 2, så er den globale variabelen fortsatt 2!

