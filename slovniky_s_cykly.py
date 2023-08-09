tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
# cyklus
for listek in tombola:
    print(f'Vyhravas {tombola[listek]}.')

#Metody, ktere muzeme volat u slovniku
#jake jsou klice ve slovniku
print(tombola.keys())

#jake jsou hodnoty ve slovniku
print(tombola.values())

#prakticky priklad
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
print(sum(sales.values())/len(sales))

#vypis jednotlivych hodnot
print(sales.items())
#vyuziti
for nazev, prodano in sales.items():
    print(f'Knihy s nazvem {nazev} se prodalo {prodano} ks.')

"""
Uvažujme vysvědčení, které máme zapsané jako slovník.

Napiš program, který spočte průměrnou známku ze všech předmětů.
Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1."""

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

print(sum(school_report.values())/len(school_report))
for predmet, znamka in school_report.items():
    if znamka == 1: #musi byt == nebo if znamka < 2
        print(f'{predmet}')# to odsazeni je nutne

"""
Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

Napiš program, který spočte celkový počet stran, které Gustav přečetl.
Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8."""

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0
for item in books:
    total_pages = total_pages + item["pages"]
print(total_pages)

for item in books:
    if item["rating"]>7:
        print(item["title"])
