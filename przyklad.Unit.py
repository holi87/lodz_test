import unittest2 as unittest
import przyklad
__author__ = "Grzegorz Holak"

class TestPrzyklad(unittest.TestCase):
    def test_czy_2_jest_parzyste(self):
        self.assertTrue(przyklad.czy_parzysta(2))


if __name__ == "__main__":
    unittest.main()
