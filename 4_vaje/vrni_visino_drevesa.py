from DvojiskoDrevo import DvojiskoDrevo
import unittest


def vrni_visino_drevesa(drevo):
    '''Vrne višino drevesa 'drevo'.'''
    if drevo.prazno():
        return 0
    return max(1 + vrni_visino_drevesa(drevo.levoPoddrevo()), 1 + vrni_visino_drevesa(drevo.desnoPoddrevo()))


class TestVrniVisinoDrevesa(unittest.TestCase):

    def test_vrni_visino_drevesa(self):
        """Test za prazno drevo"""
        self.assertEqual(vrni_visino_drevesa(DvojiskoDrevo.sestaviIzTabele([None])), 0)

    def test_vrni_visino_drevesa2(self):
        """Naklucno drevo brez posebnosti"""
        self.assertEqual(vrni_visino_drevesa(DvojiskoDrevo.sestaviIzTabele([None, 5, 6, 2, 1, 5, 4, 3, 7])),4)

    def test_vrni_visino_drevesa3(self):
        """Primer izrojenega drevesa"""
        self.assertEqual(vrni_visino_drevesa(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, None, 3, None, None, None, 4])), 4)

    def test_vrni_visino_drevesa4(self):
        """Primer drevesa, ki ima pri katerih samo leve ali desne vozle"""
        self.assertEqual(vrni_visino_drevesa(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, 4, 3, None, 5, None])), 3)

    def test_vrni_visino_drevesa5(self):
        """Primer polnega drevesa"""
        self.assertEqual(vrni_visino_drevesa(DvojiskoDrevo.sestaviIzTabele([None, 5, 4, 6, 2, 3, 9, 8])), 3)


if __name__ == '__main__':
    unittest.main()