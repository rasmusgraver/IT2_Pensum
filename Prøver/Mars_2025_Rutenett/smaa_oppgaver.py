tall = 1
nr = 1
while tall < 10000:
    tall = tall * 2 + 1
    nr += 1
    # print(f"Tall nr {nr}: {tall}")

print("Tallet er: ", tall)
print("Tallet er nr: ", nr)


def antall_a(str):
    ant_a = 0
    for c in str:
        # Trenger ikke ha med lower(), men det var jo litt nice da
        if c.lower() == "a":
            ant_a += 1

    return ant_a

print(f'Antall a i "abc": {antall_a("abc")}')
print(f'Antall a i "abba": {antall_a("abba")}')
print(f'Antall a i "bls": {antall_a("bls")}')
print(f'Antall a i "NMAKSA": {antall_a("NMAKSA")}')
print(f'Antall a i "": {antall_a("")}')

# Hvis du ville kunne du også validert slik:
if antall_a(323) != 3:
    print("FEIL: Det er 3 a'er i naskaa")