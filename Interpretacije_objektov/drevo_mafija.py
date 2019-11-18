class Drevo:

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self._prazno = False
            self.ime = args[0]
            self.vrednost = args[1]
            self.levo = kwargs.get('levo', Drevo())
            self.desno = kwargs.get('desno', Drevo())
        else:
            self._prazno = True

    def __repr__(self):
        if self._prazno:
            return 'Drevo()'
        else:
            opis = repr(self.ime) + ', ' + repr(self.vrednost)
            if not self.levo._prazno: opis += ', levo={0}'.format(self.levo)
            if not self.desno._prazno: opis += ', desno={0}'.format(self.desno)
            return 'Drevo({0})'.format(opis)

    def prazno(self):
        """Vrne true, ce je drevo prazno"""
        return self._prazno

    def desnoPoddrevo(self):
        """Vrne desno poddrevo danega drevesa"""
        return self.desno

    def levoPoddrevo(self):
        """Vrne levo poddrevo danega drevesa"""
        return self.levo

    def vrniPodatek(self):
        """Vrne trenutno vrednost v tem primeru denar elementa v korenu"""
        return self.vrednost

    def vrniIme(self):
        """Vrne ime trenutnega elementa v korenu"""
        return self.ime