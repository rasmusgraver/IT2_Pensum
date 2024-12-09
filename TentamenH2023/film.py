import datetime as dt

class Film:
    """Klasse for å representere en film"""
    def __init__(self, tittel:str, regissor:str, produsenter:list, dato:str):
        self.tittel = tittel # Tittelen på filmen
        self.regissor = regissor # Filmens regissør
        self.produsenter = produsenter # Filmens produsenter
        self.dato = dato # Datoen filmen hadde premiere/ble utgitt
        
    def finn_dager(self):
        # Tar inspirasjon fra følgende kode: https://tecadmin.net/calculate-days-between-two-dates-in-python/
        dato_start = dt.datetime.strptime(self.dato, '%Y-%m-%d')
        i_dag = dt.datetime.today()
        
        antall_dager = (i_dag - dato_start).days
        
        print(f"Filmen ble utgitt for {antall_dager} dager siden.")
        
        
    def __str__(self):
        utskrift = f'Filmen "{self.tittel}" ble utgitt {self.dato}.\n'
        utskrift += f'Filmen ble regissert av {self.regissor}'
        utskrift += f' og produsert av'
        
        # Formatterer utskrift basert på antall produsenter (ikke nødvendig, men ser litt bedre ut)
        if len(self.produsenter) == 1:
            utskrift += f' {self.produsenter[0]}.'
        else:
            for i in range(len(self.produsenter)):
                if i != len(self.produsenter) - 1:
                    utskrift += f' {self.produsenter[i]},'
                else:
                    utskrift += f' {self.produsenter[i]}.'
        
        return utskrift
        