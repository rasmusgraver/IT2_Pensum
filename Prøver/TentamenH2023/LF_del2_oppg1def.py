import requests as req
from pprint import pprint
from starwarsfilm import StarWarsFilm

# d) er å lage klassen StarWarsFilm - se fila starwarsfilm.py

# e) er å bruke API for å hente EN film, og lage objekter av den:
url = "https://swapi.dev/api/films/1/"
resultat = req.get(url)
print(f"Statuskode: {resultat.status_code}")

data = resultat.json()
# pprint(data)

for char in data["characters"]:
    print("Character:", char)

# results = data["results"]
#pprint(results)





# f) er å bruke API for å hente filmene, og lage objekter av dem:
url = "https://swapi.dev/api/films/"
resultat = req.get(url)
print(f"Statuskode: {resultat.status_code}")

data = resultat.json()
# pprint(data)
results = data["results"]

pprint(results)






filmer = []
for result in data["results"]:
    film = StarWarsFilm(result["title"], result["director"],  result["producer"],  result["release_date"], result["episode_id"])
    filmer.append(film)


# Om vi skal printe dem etter episode nr:
# Sørger for at utskriften kommer i kronologisk rekkefølge (episode 1-6)
rekkefolge = [4,5,6, 1,2,3]
for nr in rekkefolge:
    print(filmer[nr-1])
    print("-"*30)

