
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

from uzay_oyunu.dekoratorler import (
    fib_sadece_say,
    fib_say_ustte,
    fib_cache_ustte,
)


def test_fibonacci_dekorator_sirasi():
    """Üç yöntemin de Fibonacci sonucu aynı olmalı."""
    assert fib_sadece_say(20) == 6765
    assert fib_say_ustte(20) == 6765
    assert fib_cache_ustte(20) == 6765


def test_fibonacci_cagri_sayilari():
    """Dekoratör sırası çağrı sayısını değiştirmeli."""
    assert fib_sadece_say.cagri == 21891
    assert fib_say_ustte.cagri == 39
    assert fib_cache_ustte.__wrapped__.cagri == 21

from uzay_oyunu.oyun import hedef_menusu
from uzay_oyunu.galaksi import galaksi_kur


def test_hedef_menusu_log(capsys):
    sonuc = hedef_menusu(["Mars", "Dunya"])

    cikti = capsys.readouterr().out

    assert "Mars" in sonuc
    assert "-> hedef_menusu(" in cikti
    assert "<- hedef_menusu =" in cikti


def test_galaksi_kur_log(capsys):
    sonuc = galaksi_kur(
        gezegenler=["Dunya", "Mars"],
        baglantilar={"Dunya": ["Mars"], "Mars": []},
        baslangic="Dunya"
    )

    cikti = capsys.readouterr().out

    assert sonuc["baslangic"] == "Dunya"
    assert "-> galaksi_kur(" in cikti
    assert "<- galaksi_kur =" in cikti

import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut


def test_yardim_komutu():
    durum = {}
    fonksiyon, aciklama = KOMUTLAR["yardim"]
    sonuc = fonksiyon(durum)

    assert "yardim" in sonuc
    assert "envanter" in sonuc
    assert "harita" in sonuc


def test_envanter_komutu():
    durum = {
        "credits": True,
        "engines": True,
        "copilot": False
    }

    fonksiyon, aciklama = KOMUTLAR["envanter"]
    sonuc = fonksiyon(durum)

    assert "bol kredi" in sonuc
    assert "güçlü motorlar" in sonuc


def test_harita_komutu():
    durum = {
        "konum": "Dunya",
        "baglantilar": {
            "Dunya": ["Mars"],
            "Mars": []
        }
    }

    fonksiyon, aciklama = KOMUTLAR["harita"]
    sonuc = fonksiyon(durum)

    assert "Dunya" in sonuc
    assert "Mars" in sonuc


def test_ayni_komut_iki_kez_eklenemez():
    with pytest.raises(ValueError):
        @komut("yardim")
        def tekrar(durum):
            return "Tekrar"

from uzay_oyunu.dekoratorler import yakit_harca


def test_yakit_harca_normal():
    assert yakit_harca(30) == 70


def test_yakit_harca_sinirlar():
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0


def test_yakit_harca_hatali():
    with pytest.raises(ValueError):
        yakit_harca(150)

    with pytest.raises(ValueError):
        yakit_harca(-5)


def test_yakit_harca_keyword():
    assert yakit_harca(miktar=25) == 75

from functools import lru_cache
from uzay_oyunu.dekoratorler import hafiza


def test_hafiza_onbellek():
    cagri = [0]

    @hafiza()
    def kare(sayi):
        cagri[0] += 1
        return sayi * sayi

    assert kare(5) == 25
    assert kare(5) == 25
    assert cagri[0] == 1


def test_hafiza_kapasite():
    cagri = [0]

    @hafiza(maxsize=2)
    def kare(sayi):
        cagri[0] += 1
        return sayi * sayi

    kare(1)
    kare(2)
    kare(3)
    kare(1)

    assert cagri[0] == 4


def test_hafiza_lru_cache_karsilastirma():
    @hafiza()
    def kare_ozel(sayi):
        return sayi * sayi

    @lru_cache(maxsize=None)
    def kare_lru(sayi):
        return sayi * sayi

    for sayi in range(10):
        assert kare_ozel(sayi) == kare_lru(sayi)
