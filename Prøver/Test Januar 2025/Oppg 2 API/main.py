import requests as req

url = 'https://randomuser.me/api/'

resultat = req.get(url + "?results=5&nat=dk")

print(f"Statuskode: {resultat.status_code}")

data = resultat.json()

print(data)

for entry in data["results"]:
    print(entry["name"]["first"], entry["name"]["last"], "(" + entry["gender"] + ")")
