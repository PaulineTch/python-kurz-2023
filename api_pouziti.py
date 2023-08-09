"""import requests

response = requests.get('https://api.kodim.cz/python-data/people')


data = response.json()
print(data)"""

"""
Seznam lidí
to dáš
Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. Proveďte následující úkoly.

Zjistěte kolik lidí celkem seznam obsahuje.
Zjistěte jaké všechny informace máme o jednotlivých osobách.
Zjistěte, kolik je v souboru mužů a žen."""

import requests

response = requests.get('https://api.kodim.cz/python-data/people')

data = response.json()
print(len(data))
print(data[0].keys())
print(list(data[0].keys()))#kdyz tam zadam to list, tak se to zobrazi jako seznam, ne jako klice

muzi = []
zeny = []
pocet_muzu = 0
pocet_zen = 0

"""for osoba in data:
    if osoba['gender'] == 'Male':
        muzi.append(osoba['email'])
    if osoba['gender'] == 'Female':
        zeny.append(osoba['email'])"""

for osoba in data:
    if osoba['gender'] == 'Male':
        pocet_muzu = pocet_muzu + 1
    if osoba['gender'] == 'Female':
        pocet_zen = pocet_zen + 1

#print(f'muzu je {len(muzi)} a zen je {len(zeny)}')

print(f'muzu je {pocet_muzu} a zen je {pocet_zen}')
