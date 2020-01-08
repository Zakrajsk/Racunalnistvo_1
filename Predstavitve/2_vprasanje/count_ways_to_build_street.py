
def prestej_nacine(n):
    """Funckija presteje nacine postavitve his in podjetji na ulici,
    k je dolzine n. Na vsaki strani ulice je lahko n stavb,
    nobeno podjetje ne sme za soseda imeti drugo podjetje"""
    st_HH_nacinov = 1
    st_prejsnjih_nacinov = 3
    st_vseh_nacinov = 3

    for i in range(2, n + 1):
        st_vseh_nacinov = 2 * st_prejsnjih_nacinov + st_HH_nacinov
        st_HH_nacinov = st_prejsnjih_nacinov
        st_prejsnjih_nacinov = st_vseh_nacinov
    return st_vseh_nacinov


dolzina_ulice = 6
print("Pri cesti dolzine n = {0} lahko hiše in pisarne postavimo na {1} nacinov".format(dolzina_ulice, prestej_nacine(dolzina_ulice)))
