from uzay_oyunu.araclar import hamle_sayaci
from typing import List


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


def hedef_menusu(hedefler: List[str]) -> str:
    """Gidilebilecek gezegenleri numaralı menü olarak döndürür."""
    metin = "Nereye gitmek istersin?"

    for numara, gezegen in enumerate(hedefler, 1):
        metin = metin + "\n[" + str(numara) + "] " + gezegen

    return metin


def travel(bulundugun_gezegen: str, hedef: str, baglantilar: dict) -> str:
    """Gezegenler arasında doğrudan bağlantı olup olmadığını kontrol eder."""
    gidilebilecek_yerler = baglantilar.get(bulundugun_gezegen, [])

    if hedef in gidilebilecek_yerler:
        return hedef

    raise ValueError("Bu gezegene doğrudan gidemezsin")


def oyun_baslat():
    from uzay_oyunu.galaksi import galaksi_yukle, galaksi_kur
    from uzay_oyunu.tuzaklar import yakit_ekle

    print("UZAY MACERASINA HOŞ GELDİN!")
    print("--------------------------")

    veriler = galaksi_yukle()
    galaksi = galaksi_kur(veriler)

    bulunan_gezegen = galaksi["baslangic"]
    baglantilar = galaksi["baglantilar"]

    print("Başlangıç gezegeni:", bulunan_gezegen)
    print("Başlangıç yakıtı:", galaksi["yakit"])

    print("\nKeşfedilebilecek gezegenler:")

    for gezegen in galaksi["gezegenler"]:
        print("-", gezegen["ad"])

    sayac = hamle_sayaci()
    toplam_hamle = 0
    while True:
        print("\n--------------------------")
        print("Bulunduğun gezegen:", bulunan_gezegen)
        print("Kalan yakıt:", galaksi["yakit"])

        print("\nGidebileceğin gezegenler:")

        hedefler = baglantilar.get(bulunan_gezegen, [])

        for hedef in hedefler:
            print("-", hedef)

        print("- cikis")
        print("- yakit")

        secim = input("\nHangi gezegene gitmek istiyorsun? ")

        if secim == "cikis":
            print("Uzay macerası sona erdi!")
            break

        if secim == "yakit":
            depo = yakit_ekle(20)
            galaksi["yakit"] += depo[0]
            print("20 yakıt eklendi!")
            print("Güncel yakıt:", galaksi["yakit"])
            continue

        if secim not in hedefler:
            print("Bu gezegene doğrudan gidemezsin!")
            continue

        if galaksi["yakit"] < 10:
            print("Yetersiz yakıt! Yolculuk yapılamadı.")
            break

        bulunan_gezegen = travel(bulunan_gezegen, secim, baglantilar)
        galaksi["yakit"] = galaksi["yakit"] - 10
        toplam_hamle = sayac()

        print("\nYolculuk başarılı!")
        print("Yeni gezegenin:", bulunan_gezegen)
        print("Kalan yakıt:", galaksi["yakit"])

    print(f"Oyunu {toplam_hamle} hamlede bitirdin!")
if __name__ == "__main__":
    oyun_baslat()
