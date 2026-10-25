
from uzay_oyunu.dekoratorler import zaman_olc


def test_zaman_olc(capsys):
    @zaman_olc
    def toplama(a, b):
        return a + b

    sonuc = toplama(3, 5)

    assert sonuc == 8
    assert "çalışma süresi:" in capsys.readouterr().out


def test_zaman_olc_fonksiyon_adi():
    @zaman_olc
    def ornek():
        return "tamam"

    assert ornek.__name__ == "ornek"
