import json
from pathlib import Path


def galaksi_yukle():
    dosya = Path(__file__).parent / "galaksi.json"

    with open(dosya, "r", encoding="utf-8") as f:
        veriler = json.load(f)

    return veriler

    
def galaksi_kur(veriler):
    gezegenler = veriler["gezegenler"]
    baglantilar = veriler["baglantilar"]
    baslangic = veriler["baslangic"]
    yakit = veriler.get("yakit", 50)

    gezegen_adlari = [gezegen["ad"] for gezegen in gezegenler]

    if baslangic not in gezegen_adlari:
        raise ValueError("Başlangıç gezegeni bulunamadı")

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "baslangic": baslangic,
        "yakit": yakit
    }
