
from uzay_oyunu.oyun import envanter_metni, hedef_menusu



def test_envanter_metni():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    sonuc = hedef_menusu(["centauri", "sirius"])
    assert sonuc == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"

from uzay_oyunu.kayit import gorev_kaydi


def test_gorev_kaydi():
    sonuc = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        oncelik="yüksek",
        sorumlu="Ayşe"
    )

    assert "[YÜKSEK] Kara deliğe atla" in sonuc
    assert "1. Kredi kazan" in sonuc
    assert "2. Pilot bul" in sonuc
    assert "sorumlu: Ayşe" in sonuc
    
def test_travel():
    from uzay_oyunu.oyun import travel
    from uzay_oyunu.galaksi import galaksi_yukle

    veri = galaksi_yukle()
    baglantilar = veri["baglantilar"]

    assert travel("Dunya", "Mars", baglantilar) == "Mars"
    assert travel("Mars", "Jupiter", baglantilar) == "Jupiter"