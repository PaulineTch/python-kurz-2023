print("Martin".upper())
print("Martin".lower())
print("   Martin   ".strip())# odstraní mezery
print('po ut st ct pa'.split(' '))# vypíše se seznam
print('+'.join(['1', '2', '3', '4', '5']))


text = "Kurz vede lektor Marek"
novy_text = text.replace("Marek", "Janka")
print(novy_text)



"""
Další úkol v druhé BR bude následující: Mějme seznam pohybů na nějakém bankovním účtu:
pohyby = [1200, -250, -800, 540, 721, -613, -222]
Vypište v pořadí třetí pohyb z uvedeného seznamu.
Vypište všechny pohyby kromě prvních dvou.
Vypište kolik je všech pohybů dohromady.
Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
"""
pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(max(pohyby),min(pohyby))
print(sum(pohyby))

#https://docs.python.org/3/library/string.html?highlight=f%20string#format-specification-mini-language - formatovani pomoci f stringu
