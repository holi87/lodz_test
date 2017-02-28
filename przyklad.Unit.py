import unittest
import przyklad
__author__ = "Grzegorz Holak"


class TestPrzyklad(unittest.TestCase):
    # funkcja czy_parzysta
    def test_czy_2_jest_parzyste(self):
        self.assertTrue(przyklad.czy_parzysta(2))

    def test_czy_5_nie_jest_parzyste(self):
        self.assertFalse(przyklad.czy_parzysta(5))

    def test_czy_1231_nie_jest_parzysta(self):
        self.assertFalse(przyklad.czy_parzysta(1231))

    def test_czy_zero_jest_parzyste(self):
        self.assertTrue(przyklad.czy_parzysta(0))

    # funkcja zrob_parzysta
    def test_zrob_parzysta_z_3(self):
        wynik = przyklad.zrob_parzysta(3) % 2 == 0
        self.assertTrue(wynik)

    def test_czy_parzysta_z_3_to_4(self):
        self.assertEqual(4, przyklad.zrob_parzysta(3))

    def test_czy_parzysta_z_5_to_6(self):
        self.assertEqual(6, przyklad.zrob_parzysta(5))

    # funkcja dzielenie
    def test_czy_4_dzielone_przez_2_rowne_2(self):
        self.assertEqual(2, przyklad.dzielenie(4, 2))

    def test_czy_6_dzielone_przez_2_rowne_3(self):
        self.assertEqual(3, przyklad.dzielenie(6, 2))

    def test_czy_8_dzielone_przez_3_rowne_2(self):
        self.assertEqual(2, przyklad.dzielenie(8, 3))

    def test_czy_2_dzielone_przez_0_rowne_2(self):
        self.assertEqual(2, przyklad.dzielenie(2, 0))

if __name__ == "__main__":
    unittest.main()
