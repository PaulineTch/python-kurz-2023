""" Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.
Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje. """

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa 
        self.hmotnost = hmotnost
        self.doruceno = False

    def __str__(self):
        return f"Balik na adresu {self.adresa} o hmotnosti {self.hmotnost} kg je dorucen {self.doruceno}."

    def doruc(self):
        self.doruceno = True

xyz = Balik("Udolni 23, Praha", 23)
abc = Balik("Rokycanova 12, Brno", 2)

print(abc) #zavola metodu str
xyz.doruc()
print(xyz)


""" Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Kniha, která reprezentuje knihu. Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.

Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.
 """

 