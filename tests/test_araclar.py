
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

from uzay_oyunu.araclar import rota_sayisi


def test_rota_sayisi():
    assert rota_sayisi(0) == 1
    assert rota_sayisi(1) == 1
    assert rota_sayisi(5) == 8
    assert rota_sayisi(10) == 89


def test_rota_onbellek():
    rota_sayisi.cache_clear()

    rota_sayisi(10)
    ilk = rota_sayisi.cache_info()

    rota_sayisi(10)
    ikinci = rota_sayisi.cache_info()

    assert ikinci.hits > ilk.hits

from uzay_oyunu.araclar import yakit_istatistikleri, mars_yakiti


def test_yakit_istatistikleri():
    sonuc = yakit_istatistikleri(["10", "20", "0", "30"])

    assert sonuc["toplam"] == 60
    assert sonuc["ortalama"] == 20
    assert sonuc["adet"] == 3


def test_bos_istatistik():
    sonuc = yakit_istatistikleri([])

    assert sonuc["toplam"] == 0
    assert sonuc["ortalama"] == 0


def test_partial():
    assert mars_yakiti(10) == 20
