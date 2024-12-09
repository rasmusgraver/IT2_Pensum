# Oppgave 2 fra "1D_Lister.pdf"
tall = [89, 3, 89, 87, 46, 63, 54, 68, 15, 69, 27, 20, 68, 62, 25, 
26, 74, 19, 96, 85, 56, 88, 98, 87, 1, 78, 24, 64, 64, 39, 14, 9, 1, 
30, 18, 82, 41, 52, 77, 81]

# Med innebygde funksjoner:
print(f"Minst: {min(tall)}")
print(f"Størst: {max(tall)}")

# Vi har også sort muligheten:
tall.sort()
print(tall)
# Så kan man skrive ut derfra:
print(f"-- Minst: {tall[0]}")
print(f"-- Størst: {tall[-1]}")

# Og da kan man kanskje bruke den til å finne nest minst og størst:
nestMinst = tall[0]
for t in tall:
	if t != nestMinst: # fortsett til vi finner et nytt tall
		nestMinst = t
		break # Fornøyd - har funnet neste tall
print(f"-- NestMinst: {nestMinst}")

nestStr = tall[-1]
tall.reverse() # Reverserer lista for å kjøre samme metode på nest størst:
for t in tall:
	if t != nestStr: # fortsett til vi finner et nytt tall
		nestStr = t
		break # Fornøyd - har funnet neste tall
print(f"-- NestStørst: {nestStr}")



# METODE som ikke bruker noen innebygde funksjoner som sort og reverse:
tall = [89, 3, 89, 87, 46, 63, 54, 68, 15, 69, 27, 20, 68, 62, 25, 
26, 74, 19, 96, 85, 56, 88, 98, 87, 1, 78, 24, 64, 64, 39, 14, 9, 1, 
30, 18, 82, 41, 52, 77, 81]

# Starter med "ekstreme" verdier:
strst = 0
nestStr = 0
minst = 999999
nestMinst = 999999
for t in tall:
	if t > strst:
		nestStr = strst
		strst = t
	if t < minst:
		nestMinst = minst
		minst = t
	if t > nestStr and t != strst:
		nestStr = t
	if t < nestMinst and t != minst:
		nestMinst = t

print(f"Størst: {strst}, NestStørst: {nestStr}")
print(f"Minst: {minst}, NestMinst: {nestMinst}")
