# Definer en funksjon som tar inn to parametere (tall)
# og returnerer det minste av tallene
def minst(a,b):
    if a < b:
        return a
    else:
        return b

# Test funksjonen med litt ulike tall
print(minst(1,2))
print(minst(2,1))
print(minst(7,7))
print(minst(17,7))


