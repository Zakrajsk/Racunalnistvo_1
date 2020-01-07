from vrsta import Vrsta
from sklad import Sklad

def obrni_k_elementov(vrsta, k):
    """
    Podano vrsto spremeni tako, da obrne prvih k clenov,
    ostale pa pusti v istem vrstnem redu.
    """
    if k < 0 or vrsta.velikost() < k:
        raise ValueError('Napaka pri vhodnih podatkih')
    if vrsta.velikost() == 0 and k > 0:
        raise ValueError('Napaka pri vhodnih podatkih')

    pomozni_sklad = Sklad()
    for _ in range(k):
        pomozni_sklad.vstavi(vrsta.prvi())
        vrsta.izbrisi()

    while not pomozni_sklad.prazen():
        vrsta.dodaj(pomozni_sklad.vrh())
        pomozni_sklad.odstrani()

    for _ in range(vrsta.velikost() - k):
        vrsta.dodaj(vrsta.prvi())
        vrsta.izbrisi()


primer = Vrsta()
for el in range(2, 13, 2):
    primer.dodaj(el)

print('Primer')
print(primer)
print('-----------------------------------------------')
print('obrni_k_elementov(primer, 4)')
obrni_k_elementov(primer, 4)
print(primer)
print('-----------------------------------------------')

primer2 = Vrsta()
for el in range(-30, 30, 10):
    primer2.dodaj(el)

print('Primer2')
print(primer2)
print('-----------------------------------------------')
print('obrni_k_elementov(primer2, 4)')
obrni_k_elementov(primer2, 5)
print(primer2)
print('-----------------------------------------------')

primer3 = Vrsta()
for el in range(1, 6):
    primer3.dodaj(el)

print('Primer3')
print(primer3)
print('-----------------------------------------------')
print('obrni_k_elementov(primer3, 4)')
obrni_k_elementov(primer3, 5)
print(primer3)
print('-----------------------------------------------')



