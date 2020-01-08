def prestej_nacine(n) : 
    """Funckija presteje nacine postavitve his in podjetji na ulici,
    k je dolzine n. Na vsaki strani ulice je lahko n stavb,
    nobeno podjetje ne sme za soseda imeti drugo podjetje"""
    st_nacinov = [1, 3]

    for i in range(2, n + 1): 
        st_nacinov.append(st_nacinov[i - 1] + 2 * (st_nacinov[i - 2] + (st_nacinov[i - 1] - st_nacinov[i - 2]) // 2))
    
    print("Tabela na po koncani funkciji {0}".format(st_nacinov))
    return st_nacinov[-1] 
  
n = 5
print("Pri cesti dolzine n = {0} lahko hiše in pisarne postavimo na {1} nacinov".format(n, prestej_nacine(n))) 