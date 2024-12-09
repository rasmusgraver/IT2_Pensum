# Funksjon som tar som input "sidelengde" (int) som printer ut
# "Et kvadrat med sidelengde {} har omkrets {} og areal {}"
def printKvadrat(sidelengde):
    print(f"Et kvadrat med sidelengde {sidelengde} har omkrets {4*sidelengde} og areal {sidelengde**2}")

# Test funksjonen med ulike verdier
printKvadrat(2)
printKvadrat(3)

