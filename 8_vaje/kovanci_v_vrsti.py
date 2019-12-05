
import itertools

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



test = [2, 4, 4, 7]
print(naprej(test))

test2 = [5, 3, 2, 8, 9]

print(naprej(test2))

test3 = [3, 7, 6, 1, 6, 10, 5, 8, 9, 12, 3]
print(naprej(test3))