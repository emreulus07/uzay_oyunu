
# Uzay Oyunu

Python ile geliştirilmiş metin tabanlı bir uzay macerası oyunudur.

## Özellikler

- Gezegenler arasında yolculuk
- Yakıt tüketimi ve yakıt ikmali
- Hamle sayacı
- JSON dosyasından galaksi oluşturma
- Fibonacci üreteci
- Yakıt göstergesi
- CSV seyir defteri
- Önbellekli rota hesaplama

## Çalıştırma

```bash
py -m uzay_oyunu.oyun
```

## Testler

```bash
py -m pytest -v
```

## Görev 4 - Performans Karşılaştırması

30 adımlık rota hesabı için ölçülen süreler:

| Yöntem | Süre |
|---|---|
| Önbelleksiz | 0.081009 saniye |
| Önbellekli (lru_cache) | 0.000026 saniye |

**Hızlanma: 3164.4 kat**

Önbellek kullanıldığında önceden hesaplanan sonuçlar tekrar hesaplanmadığı için işlem süresi önemli ölçüde azalmıştır.
