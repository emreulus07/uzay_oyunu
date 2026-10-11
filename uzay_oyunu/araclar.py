
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
