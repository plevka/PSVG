import unittest
import RimskeCislice


class ZnameHodnoty(unittest.TestCase):
    zname_hodnoty = ((1, 'I'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (9, 'IX'),
                     (10, 'X'),
                     (47, 'XLVII'),
                     (60, 'LX'),
                     (100, 'C'),
                     (162, 'CLXII'),
                     (282, 'CCLXXXII'),
                     (333, 'CCCXXXIII'),
                     (486, 'CDLXXXVI'),
                     (599, 'DXCIX'),
                     (614, 'DCXIV'),
                     (744, 'DCCXLIV'),
                     (811, 'DCCCXI'),
                     (948, 'CMXLVIII'),
                     (1000, 'M'),
                     (1526, 'MDXXVI'),
                     (2269, 'MMCCLXIX'),
                     (6912, 'V/MCMXII'),
                     (19236, 'X/I/X/CCXXXVI'),
                     (47511, 'X/L/V/MMDXI'),
                     (128364, 'C/X/X/V/MMMCCCLXIV'),
                     (688423, 'D/C/L/X/X/X/V/MMMCDXXIII'),
                     (1288997, 'M/C/C/L/X/X/X/V/MMMCMXCVII'))

    def test_prevod(self):
        # Porovnává výsledek se známou hodnotou
        for cisla, rimskecislice in self.zname_hodnoty:
            rimske_cisla = RimskeCislice.int_to_rim(cisla)
            self.assertEqual(rimskecislice, rimske_cisla)


if __name__ == "__main__":
    unittest.main()
