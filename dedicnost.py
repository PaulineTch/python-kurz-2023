class Zamestnanec: #definice tridy, zacina velkym pismenem
    def __init__(self, jmeno, pozice):# konstruktor tridy, specialni metoda
        self.atribut_jmeno = jmeno # nazev se muze lisit, muze byt i stejny
        self.atribut_pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

class Manazer(Zamestnanec): #Manazer dedi od zamestnance atributy a metody zamestnance; muze dedit i od vice trid
    def __init__(self, jmeno, pocet_podrizenych):
        #Zamestnanec.__init__(self, jmeno, pozice) #kdyby se dedilo od vice trid, tak by se pouzilo toto, aby se vedelo od ktere tridy
        super().__init__(jmeno, pozice="manazer")#alternativa oproti radku vyse
        #self.pocet_podrizenych = pocet_podrizenych
        self.podrizeni = []

    def __str__(self):
        return f"{super().__str__()} a ma tym o velikosti {self.pocet_podrizenych}"
    
    def pridej_podrizeneho(self, novy_podrizeny):
        self.podrizeni.append(novy_podrizeny)
    
    def vypis_podrizene(self):
        podrizeni = ""
        for person in self.podrizeni:
            podrizeni += person.jmeno + ", "
        return podrizeni

alena = Manazer(jmeno="Alena", pocet_podrizenych=3)
milan = Manazer("Milan Velky", pocet_podrizenych=5)
print(alena)
print(milan)