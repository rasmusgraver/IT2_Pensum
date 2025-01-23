import requests as req

class Person:
    def __init__(self, fornavn, etternavn, kjonn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.kjonn = kjonn

    def __str__(self):
        return f"{self.fornavn} {self.etternavn} med kjønn: {self.kjonn}"
    

url = 'https://randomuser.me/api/'
resultat = req.get(url + "?results=5&nat=dk")

print(f"Statuskode: {resultat.status_code}")
data = resultat.json()
print(data)

personer = []
for entry in data["results"]:
    person = Person(entry["name"]["first"], entry["name"]["last"], entry["gender"])
    personer.append(person)

print("Personer:")
for person in personer:
    print(person)