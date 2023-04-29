"""Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420"."""
telefonni_cislo = input("Zadej telefonni cislo k zaslani zpravy")

def over_spravnost(telefonni_cislo):
    if len(telefonni_cislo) == 9 or (telefonni_cislo[0:4] == "+420" and len(telefonni_cislo) == 13):
        return True
    else:
        return False
    
spravne_cislo = over_spravnost(telefonni_cislo)

def vypocti_cenu(z):
    cena_znaku = 3
    pocet_180_useku = (len(z) - 1) // 180 + 1
    return cena_znaku*pocet_180_useku

if spravne_cislo:
    zprava = input("Zadej zpravu k odeslani")
    cena_zpravy = vypocti_cenu(zprava)
    print(f'Cena zpravy je {cena_zpravy} Kc.')
else:
    print(f'Telefonni cislo neni spravne.')
