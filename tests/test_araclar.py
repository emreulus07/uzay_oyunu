
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler


def test_hamle_sayaci():
    """Sayaç her çağrıldığında bir artmalı."""
    sayac = hamle_sayaci()

    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3


def test_sayaclar_bagimsiz():
    """İki ayrı sayaç birbirini etkilememeli."""
    sayac1 = hamle_sayaci()
    sayac2 = hamle_sayaci()

    assert sayac1() == 1
    assert sayac1() == 2
    assert sayac2() == 1


def test_en_bagli_gezegenler():
    """Gezegenler bağlantı sayısına ve isme göre sıralanmalı."""
    galaksi = {
        "baglantilar": {
            "Mars": ["Dunya", "Jupiter"],
            "Dunya": ["Mars"],
            "Jupiter": ["Mars", "Dunya"]
        }
    }

    sonuc = en_bagli_gezegenler(galaksi)

    assert sonuc == ["Jupiter", "Mars", "Dunya"]
