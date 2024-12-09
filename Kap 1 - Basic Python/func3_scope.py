total = 10

def f(x):
    # Her kan jeg bruke variabelen "x"
    # Her kan jeg bruke global variabel "total"
    x += 2
    global total # MERK: Hvis jeg vil endre en global variabel må jeg deklarere "global" på denne måten
    total += 1
    print(total, x)


x = 2
f(x)
print(x)
# MERK: Variabelen "x" her blir ikke endret selvom funksjonen gjør endringer
# på verdien 2. Den (globale) variabelen x er fortsatt 2!

