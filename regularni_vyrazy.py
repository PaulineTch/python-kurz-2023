#  https://kodim.cz/kurzy/python-data-1/ziskavani-dat/regularni-vyrazy/regularni-vyrazy
"""
Vítejte ve Směnárně na Růžku!
Kurzy měn pro 19. 12. 2020 jsou:
1 €   = 26.35 Kč
1 $   = 21.76 Kc
1 £   = 28.78 Kč
1 DKK = 3.54 kc
1 DKK = .54 kc  
Neúčtujeme žádné poplatky.

\d?\d\.\d\d [Kk][cč]
podminka OR
(\d|\d\d)\.\d\d [Kk][cč]
jedna nebo vice
\d+\.\d\d [Kk][cč]
zadna nebo vice
\d*\.\d\d [Kk][cč]
"""

"""
9. led. 2021 sobota 9:30 - 16:30 Úvod do programování 1 - Java
16. led. 2021 sobota 7:30 - 15:30 Úvod do programování 1 - Javascript
16. led. 2021 úterý 9:30 - 16:30 Úvod do programování 1 - Python
18. led. 2021 sobota 8:30 - 15:30 Úvod do programování 1 - Java
23. led. 2021 pondělí 9:30 - 16:30 Úvod do programování 1 - Javascript
27. led. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python
ONLINE
14. úno. led. 2021 neděle 8:30 - 17:30 Úvod do programování 1 - Python
ONLINE
20. úno. 2021 sobota 9:30 - 16:30 Úvod do programování 1 - Tes

{} pro pocet znaku
\d?\d\. (led|úno)\. \d{4}
mezera muze nebo nemusi byt
\d?\d\. ?(led|úno)\. \d{4}
znak pro alfanumericky znak, tedy pismeno i cislo
\d?\d\. ?\w+\. \d{4}
"""
import re
# Vytvoreni regularni vyrazu
regularni_vyraz = re.compile(r"(\+420)? ?\d{3} ?\d{3} ?\d{3}")

vstup = input("Zadej tel. číslo: ")
# Vstup musi presne odpovidat regularnimu vyrazu
vstup_ok = regularni_vyraz.fullmatch(vstup)

print(vstup_ok)

if vstup_ok:
    print("Tel. číslo je v pořádku")
else:
    print("Nesprávné tel. číslo!")


import re
regularni_vyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularni_vyraz.match(rezetec))
rezetec = "ahoj"
print(regularni_vyraz.match(rezetec))

#prisnejsi overeni
import re
regularni_vyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularni_vyraz.match(rezetec))
rezetec = "9511121234$ je moje rodné číslo"
print(regularni_vyraz.fullmatch(rezetec))


"""
Uživatelské jméno
Náš systém vyžaduje od uživatele zadání uživatelského jména. Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé. Požádej uživatele o zadání uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.
"""
import re

regularni_vyraz = re.compile(r"[a-z]{1,8}")

vstup = input("Zadej uzivatelske jmeno: ")
vstup_ok = regularni_vyraz.fullmatch(vstup)

print(vstup_ok)

if vstup_ok:
    print("Uzivatelske jmeno je v pořádku")
else:
    print("Nesprávné uzivatelske jmeno!")


"""Uprav program na ověření e-mailu tak, aby akceptoval i e-maily, které mají v první části tečku, např. jiri.pesik@python.cz."""

import re

regularni_vyraz = re.compile(r"\w+\.?\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regularni_vyraz.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")


