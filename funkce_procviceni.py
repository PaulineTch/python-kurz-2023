#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
    return a * b

vysledek = mult (2, 3)

print(vysledek)

"""
Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True)."""
#jeste vylepseno poctem noci

def total_price(persons, pocet_noci, breakfast = False):
    cena_noc = 850
    cena_snidane = 125
    
    cena_celkem = cena_noc * persons

    if breakfast :
        cena_celkem = cena_noc * persons + cena_snidane * persons
    
    return cena_celkem * pocet_noci

price = total_price(1, 2, True)
print(price)

#  Python umi vyhodnotit text urcite delky jako True a prazdny jako False, nebo prazdny list jako False a plny jako True apod. Kdyz to vypisujeme, tak True je zapsat jako True nebo 1 a False jako False nebo 0