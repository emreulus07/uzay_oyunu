
def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun sahip olduğu eşyaları metin olarak döndürür."""
    esyalar = []

    if credits:
        esyalar.append("bol kredi")

    if engines:
        esyalar.append("güçlü motorlar")

    if copilot:
        esyalar.append("yetenekli bir pilot")

    if esyalar:
        return "Sende: " + ", ".join(esyalar)

    return ""



def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek gezegenleri numaralı menü olarak döndürür."""
    metin = "Nereye gitmek istersin?"

    for numara, gezegen in enumerate(hedefler, 1):
        metin = metin + "\n[" + str(numara) + "] " + gezegen

    return metin
