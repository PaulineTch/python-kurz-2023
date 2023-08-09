a = 5
b = 7

#print(a + b)

#input
#round
#len
#sum

print(a + b)

def secti(l, k): #parametry
    print(l + k) #jen se to printuje, nikam se to neuklada

secti(8, 5) #argumenty

# print(l + k) - nefunguje,promenne nejsou definovane mimo funkci

vysledek = secti(8, 5)
print(f'Vysledek je : {vysledek}') # nevrati se nic, jen se to printuje

def secti2(l, k): #parametry
    return(l + k) #return zajisti, aby nam ta funkce neco vratila a my s ni mohli dale pracovat

vysledek = secti2(8, 5)
print(f'Vysledek je : {vysledek}')

#ke kazdemu cislu v seznamu pricti 1 pomoci funkce secti2

seznam_cisel = [2, 5, 9, 8]

for cislo in seznam_cisel:
    print(secti2(cislo, 1))

#vysledek ulozime do noveho seznamu
soucty = []

for cislo in seznam_cisel:
    soucty.append(secti2(cislo, 1))

print(soucty)

seznam_cisel = soucty #timhle si prepisu ten puvodni seznam
print(seznam_cisel)


