from DvojiskoDrevo import DvojiskoDrevo
import unittest

def kti_nivo(drevo, k):
    """Vrne vse elemente v ktem nivoju drevesa"""
    if drevo.prazno():
        return []
    if k == 1:
        return [drevo.vrniPodatek()] + kti_nivo(drevo.levoPoddrevo(), k - 1) +\
               kti_nivo(drevo.desnoPoddrevo(), k - 1)
    return kti_nivo(drevo.levoPoddrevo(), k - 1) + kti_nivo(drevo.desnoPoddrevo(), k - 1)


class TestKtiNivo(unittest.TestCase):

    def test_kti_nivo1(self):
        """Test za prazno drevo"""
        self.assertEqual(kti_nivo(DvojiskoDrevo.sestaviIzTabele([None]), 2), [])

    def test_kti_nivo2(self):
        """Naklucno drevo brez posebnosti"""
        self.assertEqual(kti_nivo(DvojiskoDrevo.sestaviIzTabele([None, 5, 6, 2, 1, 5, 4, 3, 7]), 3), [1, 5, 4, 3])

    def test_kti_nivo3(self):
        """Primer izrojenega drevesa"""
        self.assertEqual(kti_nivo(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, None, 3, None, None, None, 4]), 2), [2])

    def test_kti_nivo4(self):
        """Primer drevesa, ki ima pri katerih samo leve ali desne vozle"""
        self.assertEqual(kti_nivo(DvojiskoDrevo.sestaviIzTabele([None, 1, 2, 4, 3, None, 5, None]), 3), [3, 5])

    def test_kti_nivo5(self):
        """Primer polnega drevesa"""
        self.assertEqual(kti_nivo(DvojiskoDrevo.sestaviIzTabele([None, 5, 4, 6, 2, 3, 9, 8]), 3), [2, 3, 9, 8])


if __name__ == '__main__':
    unittest.main()