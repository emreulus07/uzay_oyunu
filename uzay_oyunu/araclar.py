from uzay_oyunu.dekoratorler import sure_olc

def hamle_sayaci():
    """Her çağrıldığında bir artan sayaç fonksiyonu döndürür."""
    hamle = 0

    def arttir():
        nonlocal hamle
        hamle += 1
        return hamle

    return arttir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına ve alfabetik sıraya göre sıralar."""
    baglantilar = galaksi["baglantilar"]

    return sorted(
        baglantilar,
        key=lambda gezegen: (-len(baglantilar[gezegen]), gezegen)
    )

from functools import lru_cache


@lru_cache(maxsize=None)
def rota_sayisi(adim: int) -> int:
    """1 veya 2 adımlık hareketlerle gidilebilecek rota sayısı."""
    if adim < 0:
        return 0

    if adim <= 1:
        return 1

    return rota_sayisi(adim - 1) + rota_sayisi(adim - 2)

@sure_olc
def rota_sayisi_onbelleksiz(adim: int) -> int:
    """Önbellek kullanmadan rota sayısını hesaplar."""
    if adim < 0:
        return 0

    if adim <= 1:
        return 1

    return (
        rota_sayisi_onbelleksiz(adim - 1)
        + rota_sayisi_onbelleksiz(adim - 2)
    )

from functools import reduce, partial


def yakit_istatistikleri(tuketimler):
    """Yakıt tüketimlerinin toplamını ve ortalamasını hesaplar."""
    sayilar = list(map(int, tuketimler))
    pozitifler = list(filter(lambda x: x > 0, sayilar))
    toplam = reduce(lambda a, b: a + b, pozitifler, 0)

    ortalama = toplam / len(pozitifler) if pozitifler else 0

    return {
        "toplam": toplam,
        "ortalama": ortalama,
        "adet": len(pozitifler)
    }


def yakit_hesapla(mesafe, katsayi):
    return mesafe * katsayi


mars_yakiti = partial(yakit_hesapla, katsayi=2)
from uzay_oyunu.dekoratorler import sure_olc