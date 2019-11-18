from DvojiskoDrevo import DvojiskoDrevo
import unittest


def ali_je_izrojeno(drevo):
    """Vrne true, ce je dvojisko drevo izrojeno, dogovor: prazno drevo je izrojeno drevo"""
    if drevo.prazno():
        return True
    if not drevo.levoPoddrevo().prazno() and not drevo.desnoPoddrevo().prazno():
        return False
    return ali_je_izrojeno(drevo.levoPoddrevo()) and ali_je_izrojeno(drevo.desnoPoddrevo())


class TestAliJeIzrojeno(unittest.TestCase):

    def test_ali_je_izrojeno(self):
        """Test za prazno drevo"""
        self.assertEqual(ali_je_izrojeno(DvojiskoDrevo.sestaviIzTabele([None])), True)

    def test_ali_je_izrojeno2(self):
        """Naklucno drevo brez posebnosti"""
        self.assertEqual(ali_je_izrojeno(DvojiskoDrevo.sestaviIzTabele([None, 5, 6, 2, 1, 5, 4, 3, 7])), False)

    def test_ali_je_izrojeno3(self):
        """Primer izrojenega drevesa"""
        self.assertEqual(ali_je_izrojeno(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, None, 3, None, None, None, 4])), True)

    def test_ali_je_izrojeno4(self):
        """Primer drevesa, ki ima pri katerih samo leve ali desne vozle"""
        self.assertEqual(ali_je_izrojeno(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, 4, 3, None, 5, None])), False)

    def test_ali_je_izrojeno5(self):
        """Primer polnega drevesa"""
        self.assertEqual(ali_je_izrojeno(DvojiskoDrevo.sestaviIzTabele([None, 5, 4, 6, 2, 3, 9, 8])), False)


if __name__ == '__main__':
    unittest.main()