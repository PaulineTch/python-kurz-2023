"""Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json."""

import json

with open('python-kurz-2023/Ukol-3/body.json', encoding='utf-8') as puvodni_soubor:
    pisemka = json.load(puvodni_soubor)

vysledky = {}

for zak, body in pisemka.items():
    if body >= 60: 
        vysledky[zak] = "Pass"
    else:
        vysledky[zak] = "Fail"

with open('python-kurz-2023/Ukol-3/prospech.json', mode='w', encoding='utf-8') as finalni_soubor:
    json.dump(vysledky, finalni_soubor, ensure_ascii = False)


