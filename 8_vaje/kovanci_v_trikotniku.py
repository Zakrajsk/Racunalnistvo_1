
def naj_vsota(trikotnik):
    '''najvecja vsota kovancev v trikotniku'''
    globina = len(trikotnik[-1]) - 1
    for i in range(globina - 1, -1, -1):
        for j in range(i + 1):
            trikotnik[i][j] += max(trikotnik[i + 1][j], trikotnik[i + 1][j + 1])
    return trikotnik[0][0]


def vsota(trikotnik):
    '''vrne optimalno pot zapisano v podseznamih'''
    pot = [[' ' for i in range(j+1)] for j in range(len(trikotnik)-1)]
    for i in range(len(trikotnik) - 2, -1, -1):
        for j in range(i+1):
            trikotnik[i][j] = max(
                trikotnik[i][j]+trikotnik[i + 1][j], trikotnik[i][j] + trikotnik[i + 1][j + 1])
            pot[i][j] = 'levo' if trikotnik[i + 1][j] > trikotnik[i + 1][j + 1] else 'desno'
    return pot


def optimalna_pot(trikotnik):
    '''vrne opis optimalne poti z nizoma 'levo', 'desno' '''
    pot = vsota(trikotnik)
    optimalna_pot = list()
    j = 0
    for i in range(len(pot)):
        if pot[i][j] == 'levo':
            optimalna_pot.append('levo')
        if pot[i][j] == 'desno':
            j += 1
            optimalna_pot.append('desno')
    return optimalna_pot


trikotnik = [[10], [5, 8], [12, 6, 5], [4, 7, 10, 12], [4, 6, 6, 4, 2], [2, 5, 5, 3, 3, 8], [4, 4, 2, 6, 4, 2, 4], [5, 4, 6, 6, 10, 2, 4, 6]]

print(naj_vsota(trikotnik))
print(optimalna_pot(trikotnik))
