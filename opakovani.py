print("Vítejte v dlouhodobém kurzu Pythonu!") # string
nazev_hry = "Romeo a Julie"
cena_listku = 150 # int
pocet_listku = int(input("Zadej počet lístků")) #string - převod na integer

celkova_cena = cena_listku * pocet_listku

print(f"Cena všech lístků je {celkova_cena}")
print("Cena všech lístků je", celkova_cena)

if pocet_listku >= 3:
    zlevnena_cena = celkova_cena * 0.9
    print(f"Zlevněná cena je {zlevnena_cena} z původní {celkova_cena}")
else:
    print(f"Celková cena je {celkova_cena}")

"""
    Zadání cvičení: : Využijte příklady z výkladu. Upravte je tak, aby
- se program zeptal uživatele i na věk, a ověříš, že má alespoň 13 let. Pokud nemá alespoň 13 let, nezeptá se už na počet lístků a skončí(tj. nákup neproběhne).
- bonus pro netrpělivé :) viz výše + místo slevy 10% uplatní akci "při nákupu alespoň 3 lístků je jeden lístek zdarma"
"""

vek = int(input("Zadej svůj věk"))

if vek < 13:
    print("Jsi moc mladý")
    exit() # ukončí běh programu, tzn. můžu pokračovat 
elif pocet_listku >= 3:
    print(f"Zlevněná cena je {zlevnena_cena} z původní {celkova_cena}")
else:
    print(f"Celková cena je {celkova_cena}")



#Jakub
    CENA_LISTKU = 150

vek = int(input('Zadej svůj věk: '))
# zkontrolovat věk a případně skončit
if vek < 13:
    print('Jsi moc mladý.')
    exit()  # ukončí běh programu

pocet_listku = int(input("Zadej počet lístků: "))

vysledna_cena = CENA_LISTKU * pocet_listku

if pocet_listku > 3:
    # aplikujeme slevu
    vysledna_cena = vysledna_cena * 0.9

print(f'zaplatis {vysledna_cena}')


CENA_LISTKU = 150

vek = int(input('Zadej svůj věk: '))
# zkontrolovat věk a případně skončit
if vek < 13:
    print('Jsi moc mladý.')
    exit()  # ukončí běh programu

pocet_listku = int(input("Zadej počet lístků: "))

vysledna_cena = CENA_LISTKU * pocet_listku

if pocet_listku > 3:
    # aplikujeme slevu
    # vysledna_cena = CENA_LISTKU * (pocet_listku - 1)   # <-- take moznost
    vysledna_cena = vysledna_cena - CENA_LISTKU
    
print(f'zaplatis {vysledna_cena} Kč')