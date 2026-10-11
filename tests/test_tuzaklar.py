from uzay_oyunu.tuzaklar import yakit_ekle


def test_yakit_ekle():
    ilk_depo = yakit_ekle(10)
    ikinci_depo = yakit_ekle(20)

    assert ilk_depo == [10]
    assert ikinci_depo == [20]