class Sklad:
    ''' Špartanska predstavitev sklada 
    '''
    def __init__(self):
        self._podatki = []
        
    def vstavi(self, x):
        self._podatki.append(x)
        
    def prazen(self) :
        return (len(self._podatki) == 0)
    
    def odstrani(self) :
        if self.prazen() :
            raise ValueError('ODSTRANI: Sklad je prazen.')
        self._podatki.pop()
        
    def vrh(self) :
        if self.prazen() :
            raise ValueError('VRH: Sklad je prazen.')
        return self._podatki[len(self._podatki)-1]
    
    def __str__(self) :
        izp = 'DNO'
        for i in range(len(self._podatki)) :
            izp = izp + " : " + str(self._podatki[i])
        izp = izp + ' : VRH'
        return izp
