
import pytest

from uzay_oyunu.galaksi import galaksi_kur, galaksi_yukle


def test_varsayilan_yakit():
    """Yakıt belirtilmezse 50 olmalı."""
    galaksi = galaksi_kur(
        ["Mars"],
        {"Mars": []},
        "Mars"
    )

    assert galaksi["yakit"] == 50
    assert galaksi["konum"] == "Mars"


def test_gecersiz_baslangic():
    """Başlangıç gezegeni listede yoksa hata vermeli."""
    with pytest.raises(ValueError):
        galaksi_kur(
            ["Mars"],
            {"Mars": []},
            "Dunya"
        )


def test_json_dosyasindan_galaksi():
    """JSON dosyasındaki verilerle galaksi kurulabilmeli."""
    veri = galaksi_yukle()
    galaksi = galaksi_kur(**veri)

    assert galaksi["baslangic"] == veri["baslangic"]
    assert galaksi["baglantilar"] == veri["baglantilar"]
