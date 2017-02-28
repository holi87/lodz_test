
__author__ = "Grzegorz Holak"


def czy_parzysta(liczba):
    if not liczba % 2 == 0:
        return False
    return True


def zrob_parzysta(nieparzysta):
    return nieparzysta + 1


def dzielenie(dzielna, dzielnik):
    if czy_parzysta(dzielnik):
        return dzielna / dzielnik
    else:
        dzielnik = zrob_parzysta(dzielnik)
        return dzielna / dzielnik
