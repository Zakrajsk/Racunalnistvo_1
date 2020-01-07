class Vrsta:
    def __init__(self):
        self._queue = []

    def dodaj(self, element):
        """
        Doda element na konec vrste
        """
        self._queue.append(element)

    def izbrisi(self):
        """
        Izbrise prvi element v vrsti
        """
        if not self._queue:
            raise ValueError('Vrsta je prazna')
        self._queue = self._queue[1:]

    def velikost(self):
        """
        Vrne velikost vrste
        """
        return len(self._queue)

    def prvi(self):
        """
        Vrne prvi element v vrsti
        """
        if not self._queue:
            raise ValueError('Vrsta je prazna')
        return self._queue[0]

    def __str__(self):
        return 'ZACETEK : {0} : KONEC'.format(' : '.join(map(str, self._queue)))
