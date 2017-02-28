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


if __name__ == "__main__":
    unittest.main()
