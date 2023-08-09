#pres json se predavaji data na internetu, komunikace api
import json

with open('absolventi.json') as prvni_soubor:
    data = prvni_soubor.read()# read nam to vypise jako string

print(data)
print(type(data))

"""#tady bychom museli ten soubor i zavrit, kdezto v radcich 3 a 4 to udela sam... cte to jen uvnitr a jak se vrati z odsazeneho radku, uz to nebere v potaz (operation on closed file)... kdyz je otevreny, tak je ten soubor zamceny dokud ho python pouziva a nelze ho pouzit jinde
print(open('absolventi.json').read())"""

"""#kdyby ten soubor byl v jine slozce, pak 
with open('data/absolventi.json') as prvni_soubor:
    data = prvni_soubor.read()"""

import json

with open('absolventi.json', encoding='utf-8') as prvni_soubor:# utf-8 je tam kvuli diakritice
    seznam_absolventu = json.load(prvni_soubor)#load nam to vypise jako json

print(seznam_absolventu)
print(seznam_absolventu[0])

#zapis json dat
import json

hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}

with open('hodiny.json', mode='w', encoding='utf-8') as file:#mode je r (read) pokud neni zadan
    json.dump(hours, file)#automaticky file vytvori, pokud jeste neexistuje

"""
Pracuj dál se souborem zavod.json a zjisti čas závodníka, který získal stříbrnou medaili. Dále projdi data pomocí cyklu a vytvoř seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není DNF.

Můžeš postupovat následujícím způsobem:

Vytvoř si prázdný seznam finishers, kam budeš vkládat jména závodníků, kteří závod doběhli.
Pomocí cyklu projdi seznam závodníků. Struktura vyjmuté položky bude obdobná jako struktura dat o vítězi závodu. Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
Dovnitř podmínky vlož kód, který vloží jméno závodníka do seznamu finishers.
Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu finishers."""

import json

with open('zavod.json', encoding='utf-8') as soubor:
    data = json.load(soubor)

print(data[1]['casy']['oficialni'])

dokoncili = []

for zavodnik in data:
    if zavodnik['casy']['oficialni'] != 'DNF':
        dokoncili.append(zavodnik['jmeno'])

print(dokoncili)