#zamestnanec: jmeno, pozice

#frantisek = ["Frantisek Novak", "ucetni"]
#alena = ["Alena Drobna", "sefova"]

#frantisek = {"jmeno": "Frantisek Novak", "pozice": "ucetni"}
#alena = {"jmeno": "Alena Drobna", "pozice": "sefova"}

#zamestnanci = [frantisek, alena]

class Zamestnanec: #definice tridy, zacina velkym pismenem
    jmeno = ""
    pozice = ""

frantisek = Zamestnanec() #objekt
frantisek.jmeno = "Frantisek Novak"
frantisek.pozice = "ucetni"

alena = Zamestnanec()
alena.jmeno = "Alena Drobna"
alena.pozice = "sefova"

print(frantisek.pozice)
zamestnanci = [frantisek, alena]

class Zamestnanec: #definice tridy, zacina velkym pismenem
    def __init__(self, jmeno, pozice):# konstruktor tridy, specialni metoda
        self.atribut_jmeno = jmeno # nazev se muze lisit, muze byt i stejny
        self.atribut_pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def info(self): #metoda tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def cerpani_dovolene(self, days):
        if self.pocet_dni_dovolene >= days:
            self.pocet_dni_dovolene -= days
            return f"Uzij si to"
        else:
            return f"Bohuzel uz mas narok jen na {self.pocet_dni_dovolene} dni."

frantisek = Zamestnanec("Frantisek Novak", "ucetni")
alena = Zamestnanec ("Alena Drobna", "sefova")

print(frantisek.atribut_jmeno)
print(frantisek.info())

print(frantisek) #print(str(frantisek))

print(frantisek.cerpani_dovolene(5))
print(frantisek.pocet_dni_dovolene)