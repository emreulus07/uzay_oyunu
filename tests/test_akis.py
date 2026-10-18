
from itertools import islice, takewhile

from uzay_oyunu.akis import fibonacci


def test_fibonacci_ilk_uc():
    """next ile ilk üç Fibonacci sayısını kontrol eder."""
    g = fibonacci()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1


def test_fibonacci_ilk_on_iki():
    """islice ile ilk 12 sayıyı kontrol eder."""
    sonuc = list(islice(fibonacci(), 12))

    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_yuzden_kucuk():
    """takewhile ile 100'den küçük sayıları kontrol eder."""
    sonuc = list(takewhile(lambda sayi: sayi < 100, fibonacci()))

    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_uretec_tuketimi():
    """Aynı üreteç ikinci kullanımda kaldığı yerden devam eder."""
    g = fibonacci()

    ilk = list(islice(g, 5))
    ikinci = list(islice(g, 5))

    assert ilk == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]

import pytest

from uzay_oyunu.akis import yakit_gostergesi


def test_yakit_gostergesi():
    """Yakıt her adımda azalmalı."""
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_bittiginde_durur():
    """Yakıt bitince StopIteration oluşmalı."""
    g = yakit_gostergesi(10, 5)

    assert next(g) == 5
    assert next(g) == 0

    with pytest.raises(StopIteration):
        next(g)

from uzay_oyunu.akis import seyir_defteri


def test_seyir_defteri(tmp_path):
    dosya = tmp_path / "seyir.csv"
    dosya.write_text(
        "gezegen,yakit\nMars,45\nJupiter,40\n",
        encoding="utf-8"
    )

    sonuc = list(seyir_defteri(dosya))

    assert len(sonuc) == 2
    assert sonuc[0]["gezegen"] == "Mars"
    assert sonuc[1]["yakit"] == "40"
