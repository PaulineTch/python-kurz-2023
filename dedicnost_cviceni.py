""" Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída. Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek, který reprezentuje velikost úvazku oproti plnému. Přidej informaci o úvazku k výpisu informací do funkce __str__. """

class Zamestnanec: 
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno 
        self.pozice = pozice

    def __str__(self):
        return f'Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}'

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, pozice, uvazek):
        super().__init__(jmeno, pozice)
        self.uvazek = uvazek

    def __str__(self):
        return f'{super().__str__()} a ma uvazek {self.uvazek}'
        
b1 = Brigadnik("Martin", "brigadnik", "castecny")
print(b1)
z1 = Zamestnanec("Jan", "sef")
print(z1)