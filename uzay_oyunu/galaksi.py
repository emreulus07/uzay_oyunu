
import json
from pathlib import Path


def galaksi_yukle() -> dict:
    """Galaksi bilgilerini JSON dosyasından okur."""
    dosya = Path(__file__).parent / "galaksi.json"

    with open(dosya, "r", encoding="utf-8") as f:
        veriler = json.load(f)

    return veriler


def galaksi_kur(
    gezegenler: list,
    baglantilar: dict,
    baslangic: str,
    **kwargs
) -> dict:
    """Gezegen bilgilerini kontrol ederek galaksi oluşturur."""

    gezegen_adlari = [
        gezegen["ad"] if isinstance(gezegen, dict) else gezegen
        for gezegen in gezegenler
    ]

    if baslangic not in gezegen_adlari:
        raise ValueError("Başlangıç gezegeni bulunamadı")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "baslangic": baslangic,
        "konum": baslangic,
        "yakit": yakit
    }
