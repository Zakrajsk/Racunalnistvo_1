from DvojiskoDrevo import DvojiskoDrevo
import unittest


def stevilo_vseh_vozlisc(drevo):
    """Vrne stevilo vseh vozlisc v drevesu"""
    if drevo.prazno():
        return 0
    return 1 + stevilo_vseh_vozlisc(drevo.levoPoddrevo()) + stevilo_vseh_vozlisc(drevo.desnoPoddrevo())


class TestSteviloVsehVozlisc(unittest.TestCase):

    def test_stevilo_vseh_vozlisc1(self):
        """Test za prazno drevo"""
        self.assertEqual(stevilo_vseh_vozlisc(DvojiskoDrevo.sestaviIzTabele([None])), 0)

    def test_stevilo_vseh_vozlisc2(self):
        """Naklucno drevo brez posebnosti"""
        self.assertEqual(stevilo_vseh_vozlisc(DvojiskoDrevo.sestaviIzTabele([None, 5, 6, 2, 1, 5, 4, 3, 7])), 8)

    def test_stevilo_vseh_vozlisc3(self):
        """Primer izrojenega drevesa"""
        self.assertEqual(stevilo_vseh_vozlisc(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, None, 3, None, None, None, 4])), 4)

    def test_stevilo_vseh_vozlisc4(self):
        """Primer drevesa, ki ima pri katerih samo leve ali desne vozle"""
        self.assertEqual(stevilo_vseh_vozlisc(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, 4, 3, None, 5, None])), 5)

    def test_stevilo_vseh_vozlisc5(self):
        """Primer polnega drevesa"""
        self.assertEqual(stevilo_vseh_vozlisc(DvojiskoDrevo.sestaviIzTabele([None, 5, 4, 6, 2, 3, 9, 8])), 7)


if __name__ == '__main__':
    unittest.main()



