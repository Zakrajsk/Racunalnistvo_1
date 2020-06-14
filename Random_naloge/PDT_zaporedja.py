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
        


def pdt_zaporedje(niz):
    """podan je nek niz znakov PDT, če operacija p sledi D se ta izničita
    prav tako velja za tp in dt
    """
    pomozni_sklad = Sklad() #belezimo kaj je bilo nazadnje
    for znak in niz:
        if znak == 'D':
            #Pogledamo, če imamo predhonjo črko P in v tem primeru to izničimo drugače dodamo v sklad
            if pomozni_sklad.prazen() or pomozni_sklad.vrh() != 'P': #ce je prazen samo vstavimo drgace pogledamo ce je bilo nazadnje p
                pomozni_sklad.vstavi('D')
            else:
                pomozni_sklad.odstrani() #samo odstranimo prejšnjega, novega pa ne rabimo vstavljat ker se oba izničita

        if znak == 'P':
            #pogledamo če imamo predhodnjo črko T in v tem primeru to izničimo drugače dodamo v sklad
            if pomozni_sklad.prazen() or pomozni_sklad.vrh() != 'T':
                pomozni_sklad.vstavi('P')
            else:
                pomozni_sklad.odstrani()
        if znak == 'T':
            #pogledamo če imamo predhonjo črko D in v tem primeru to izničimo drugače dodamo v sklad
            if pomozni_sklad.prazen() or pomozni_sklad.vrh() != 'D':
                pomozni_sklad.vstavi('T')
            else:
                pomozni_sklad.odstrani()
    
    #sedaj imamo v skladu vse kar je ostalo
    obratni_koncni_niz = ''
    while not pomozni_sklad.prazen():
        obratni_koncni_niz += pomozni_sklad.vrh()
        pomozni_sklad.odstrani()
    
    return obratni_koncni_niz[::-1]

print(pdt_zaporedje('PPPDDDTTT'))