
from functools import wraps

KOMUTLAR = {}


def komut(ad, aciklama=""):
    """Fonksiyonu komut listesine kaydeder."""
    def dekorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"Komut zaten kayıtlı: {ad}")

        KOMUTLAR[ad] = (func, aciklama)
        return func

    return dekorator


@komut("yardim", "Kullanılabilir komutları gösterir")
def yardim(durum):
    return "\n".join(
        f"{ad}: {aciklama}"
        for ad, (_, aciklama) in KOMUTLAR.items()
    )


@komut("envanter", "Oyuncunun eşyalarını gösterir")
def envanter(durum):
    esyalar = []

    if durum.get("credits"):
        esyalar.append("bol kredi")
    if durum.get("engines"):
        esyalar.append("güçlü motorlar")
    if durum.get("copilot"):
        esyalar.append("yetenekli bir pilot")

    return "Sende: " + ", ".join(esyalar) if esyalar else "Envanter boş"


@komut("harita", "Bulunduğun gezegenin bağlantılarını gösterir")
def harita(durum):
    konum = durum["konum"]
    hedefler = durum["baglantilar"].get(konum, [])

    return f"{konum} -> {', '.join(hedefler)}"
