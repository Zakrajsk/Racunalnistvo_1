
import itertools


#za test naredil najbolj neoptimiziran program, vendar tukaj opazimo, da se že pri n > 10 pojavi memory error.
def naprej(kovanci):
    """Funkcija presteje optimalno vsoto kovancev, v primeru da lahko vzamemo kovanec, ce nismo vzeli sosednjega.
    Pri tem uporabi vse mozne permutacije"""
    st_kovancev = len(kovanci)
    min_st_enk = round(st_kovancev / 3 + 0.5)
    max_st_enk = round(st_kovancev / 2 + 0.5)
    vse_moznosti = set()
    naj_vsota = 0
    for i in range(min_st_enk, max_st_enk + 1):
        vse_moznosti = vse_moznosti.union(set(list(itertools.permutations([1] * i + [0] * (st_kovancev - i)))))
    for moznost in vse_moznosti:
        if '11' not in ''.join(map(str, moznost)):
            vsota = sum([(a * b) for a, b in zip(moznost, kovanci)])
            naj_vsota = max(vsota, naj_vsota)
    return naj_vsota


#rekurzivna rešitev
def rekurzija(i, K):
    '''Funkcija presteje optimalno vsoto kovancev,
     v primeru da lahko vzamem kovanec, ce nismo vzeli sosednjega.
     Pri tem uporabi rekurzijo'''
    dolzina = len(K) - 1
    if i == dolzina: return K[dolzina]
    if i == dolzina - 1: return max(K[dolzina], K[dolzina -1])
    vzamemo = K[i] + rekurzija(i + 2, K)
    ne_vzamemo = rekurzija(i + 1, K)
    return max(vzamemo, ne_vzamemo)


#Rešitev, pri kateri se izpiše tudi kombinacija kovancev, ki sestavljajo maksimalno vsoto
def kateri_kovanci(kovanci):
    """Funkcija presteje optimalno vsoto kovancev, v primeru da lahko vzamemo kovanec, ce nismo vzeli sosednjega.
    Pri tem uporabi vse mozne permutacije, program vrne zaporedje teh kovancev in pa maksimalno vsoto"""
    st_kovancev = len(kovanci)
    min_st_enk = round(st_kovancev / 3 + 0.5)
    max_st_enk = round(st_kovancev / 2 + 0.5)
    vse_moznosti = set()
    najboljsa_kombinacija = list()
    naj_vsota = 0
    for i in range(min_st_enk, max_st_enk + 1):
        vse_moznosti = vse_moznosti.union(set(list(itertools.permutations([1] * i + [0] * (st_kovancev - i)))))
    for moznost in vse_moznosti:
        if '11' not in ''.join(map(str, moznost)):
            vsota = sum([(a * b) for a, b in zip(moznost, kovanci)])
            if vsota > naj_vsota:
                naj_vsota = vsota
                najboljsa_kombinacija = [el for i, el in enumerate(kovanci) if moznost[i] == 1]
    return naj_vsota, najboljsa_kombinacija