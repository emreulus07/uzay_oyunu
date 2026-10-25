
# Hafta 5 - Dekoratör Sırası

Bu çalışmada Fibonacci(20) fonksiyonu üç farklı dekoratör sırasıyla test edilmiştir.

| Kullanım | Çağrı sayısı |
|---|---:|
| Sadece `@say` | 21891 |
| `@say` dışta, `@lru_cache` içte | 39 |
| `@lru_cache` dışta, `@say` içte | 21 |

## Açıklama

**1. Sadece @say**

Önbellek kullanılmadığı için aynı Fibonacci değerleri tekrar tekrar hesaplanır. Bu nedenle çağrı sayısı 21891 olur.

**2. @say dışta, @lru_cache içte**

Sayaç her fonksiyon çağrısını sayar. Önbellekte bulunan değerler yeniden hesaplanmasa bile sayaç artar. Çağrı sayısı 39 olur.

**3. @lru_cache dışta, @say içte**

Önbellek önce kontrol edilir. Daha önce hesaplanan değerlerde sayaç çalışmaz. Bu nedenle çağrı sayısı 21 olur.

## Sonuç

Dekoratörlerin sırası programın çalışma şeklini etkiler. Önbellek dışta olduğunda gereksiz fonksiyon çalışmaları engellenir.
