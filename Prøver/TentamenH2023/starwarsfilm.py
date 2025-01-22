from film import Film


# Lager en ordbok for å gjøre om fra arabiske tall til romertall
romertall_ordbok = {
    1 : "I",
    2 : "II",
    3 : "III",
    4 : "IV",
    5 : "V",
    6 : "VI"
}

class StarWarsFilm(Film):
    def __init__(self, tittel:str, regissor:str, produsenter:list, dato:str, episode:int):
        super().__init__(tittel, regissor, produsenter, dato)
        # Oppdaterer tittelen basert på spesifikasjonen
        self.tittel = f"Star Wars: Episode {romertall_ordbok[episode]} - {tittel}"
        self.episode = episode
        
    # Oppdaterer metoden som skriver ut informasjon om filmen
    def __str__(self):
        utskrift = super().__str__() + "\n"
        
        utskrift += f'Kronologisk er dette nr. {self.episode}.'
        
        return utskrift