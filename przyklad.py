
__author__ = "Grzegorz Holak"


def czy_parzysta(liczba):
    if not liczba % 2 == 0:
        return False
    return True


def zrob_parzysta(nieparzysta):
    return nieparzysta + 1


def dzielenie(dzielna, dzielnik):
    if not czy_parzysta(dzielnik):
        dzielnik = zrob_parzysta(dzielnik)
    if dzielnik == 0:
        return dzielna
    return dzielna / dzielnik
