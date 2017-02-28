import unittest
import przyklad
__author__ = "Grzegorz Holak"


class TestPrzyklad(unittest.TestCase):
    def test_czy_2_jest_parzyste(self):
        self.assertTrue(przyklad.czy_parzysta(2))

    def test_czy_5_nie_jest_parzyste(self):
        self.assertFalse(przyklad.czy_parzysta(5))

    def test_czy_1231_nie_jest_parzysta(self):
        self.assertFalse(przyklad.czy_parzysta(1231))

if __name__ == "__main__":
    unittest.main()
