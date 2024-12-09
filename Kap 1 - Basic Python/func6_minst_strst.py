# Definer en funksjon som tar inn en liste av tall
# som input. Returner BÅDE det minste og det største tallet
def strstOgMinst(liste):
    minst = min(liste)
    strst = max(liste)
    return (minst, strst) # MERK: Vi returnerer 2 verdier som en tuppel

# Eks: strstOgMinst([1,2,3,6,7,0] skal returnere 0 og 7)
minst, strst = strstOgMinst([1,2,3,6,7,0]) # MERK Vi kan "pakke ut" tuplen på denne måten!
print(f"Minst {minst} Størst: {strst}" )
