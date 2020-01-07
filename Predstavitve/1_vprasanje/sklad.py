class Sklad:
    def __init__(self):
        self._podatki = []
        
    def vstavi(self, x):
        """
        Vstavi x v sklad
        """
        self._podatki.append(x)
        
    def prazen(self):
        """
        Vrne true, ce je sklad prazen
        """
        return len(self._podatki) == 0
    
    def odstrani(self):
        """
        Odstrani element iz sklada, ce je sklad prazer sprozi izjemo ValueError
        """
        if self.prazen():
            raise ValueError('ODSTRANI: Sklad je prazen.')
        self._podatki.pop()
        
    def vrh(self):
        """
        Vrne vrhnji element v skladu, ce je sklad prazen sprozi izjemo ValueError
        """
        if self.prazen():
            raise ValueError('VRH: Sklad je prazen.')
        return self._podatki[len(self._podatki)-1]
    
    def __str__(self):
        return 'DNO : {0} : VRH'.format(' : '.join(map(str, self._podatki)))
