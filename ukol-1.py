"""Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.

Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz."""

jmeno = "Pavla"
email = f'{jmeno}@czechitas.cz'
print(email)

"""Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:

všechna písmena velká (vypíše např. JANA MALÁ)
všechna písmena malá (vypíše např. jana malá)
standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
iniciály (vypíše např. J. M.)
křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?)."""

jmeno_a_prijmeni = input("Zadej jméno a příjmení")
seznam_jmeno_prijmeni = jmeno_a_prijmeni.split()
jmeno = seznam_jmeno_prijmeni[0].capitalize()
prijmeni = seznam_jmeno_prijmeni[1].capitalize()
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(f'{jmeno} {prijmeni}')
print(f'{jmeno[0]}. {prijmeni[0]}.')
if len(jmeno)>5:
    print(f'{jmeno[0]}. {prijmeni}')
else:
    print(f'{jmeno} {prijmeni}')
