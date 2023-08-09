def eur_to_czk(pocet_eur):
    """
    Funkce na prevod eur do korun.
    Bere jeden parametr - pocet eur. Kurz fixni 25 Kc za 1 euro.
    Vrati kolik stoji eura v korunach
    """ # ten dokumentacni komentar se zobrazi kdyz se pouziva ta funkce - jen musi byt v tech trojitych uvozovkach
    kurz = 25 # lokalni promenna, ktera neni videt mimo telo funkce (mohla bych tu pouzit i globalni promennou, definovanou mimo telo funkce - ta se pak pise velkyma KURZ)
    pocet_czk = pocet_eur * kurz
    return pocet_czk


print(eur_to_czk(10))

eura_uzivatel = int(int(input("Kolik si prejete smenit euro?")))
print(eur_to_czk(eura_uzivatel))

#funkce bez kodu - na pozdeji
def code_me_later(a, b):
    pass


def eur_to_czk2(pocet_eur, kurz = 25): # nastaveni defaultni hodnoty
    """
    Funkce na prevod eur do korun.
    Bere jeden parametr - pocet eur. Kurz fixni 25 Kc za 1 euro.
    Vrati kolik stoji eura v korunach
    """ 
    pocet_czk = pocet_eur * kurz
    return pocet_czk

eura_uzivatel = int(int(input("Kolik si prejete smenit euro?")))
print(eur_to_czk2(eura_uzivatel))# kurz bude 25


print(eur_to_czk2(eura_uzivatel, 28))# prepiseme defaultni hodnotu

#zalezi na poradi

# slozitejsi priklad
#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def get_mark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")

