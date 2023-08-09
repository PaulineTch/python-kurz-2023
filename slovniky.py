#pekarna na polozky a ceny v korunach
# slovnik  - slozena zavorka
pekarna = {
    "houska": 20,
    "rohlik": 5,
    "chleba": 40,
    "loupak": 20
}

#seznam - hranata zavorka
produkty = ["houska", "rohlik", "chleba", "loupak"]

print(pekarna)
print(pekarna["chleba"])

klic = "rohlik"
print(f'Klic: {klic}, hodnota: {pekarna[klic]} korun.')

# vypis hodnoty
produkt = input("Zadej produkt")
print(f' {produkt} stoji {pekarna[produkt]} korun.')

# je produkt v pekarne (klic ve slovniku)
if ...:
    print(f' {produkt} stoji {pekarna[produkt]} korun.')
else:
    print(f'Bohuzel, produkt {produkt} neprodavame.')

#pridani do slovniku
pekarna["zakusek"]=35
print(pekarna)

#odebirani
cena_houska = pekarna.pop("houska")
print(pekarna)
print(cena_houska)

"""Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print()."""
vysvedceni = {
    "cesky jazyk": 2,
    "matematika": 1,
    "dejepis": 3
}

print(vysvedceni)

"""Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
Zkopíruj si slovník do svého programu.
Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100."""

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"]=0
print(sales)

sales["Vrah zavolá v deset"]=sales["Vrah zavolá v deset"]+100
print(sales)

"""
V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.

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
Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál."""

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

cislo_listku = int(input("Zadej cislo sveho listku"))

if cislo_listku in tombola:
    print(f'Vyhravas {tombola[cislo_listku]}.')
else:
    print(f'Nevyhravas bohuzel nic.')