
import csv
from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Sonsuz Fibonacci sayılarını üretir."""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int):
    """Her yolculukta yakıtı azaltır, sıfıra gelince durur."""
    if tuketim <= 0:
        raise ValueError("Tüketim sıfırdan büyük olmalı.")

    while yakit > 0:
        yakit = max(0, yakit - tuketim)
        yield yakit


def seyir_defteri(dosya_yolu):
    """CSV dosyasındaki yolculuk kayıtlarını tek tek okur."""
    with open(dosya_yolu, "r", encoding="utf-8", newline="") as dosya:
        okuyucu = csv.DictReader(dosya)

        for satir in okuyucu:
            yield satir
