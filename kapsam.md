# Görev 4B - Değişken Kapsamı

## Örnek 1 - Yerel ve Global Değişken

Fonksiyonun içinde gezegen değişkenine Mars değeri verildiğinde,
bu değişiklik sadece fonksiyonun içinde geçerli olur.

Bu yüzden ilk çıktı Mars, ikinci çıktı Dünya olur.

Çıktı:
Mars
Dünya

## Örnek 2 - Global Kullanımı

Başlangıçta yakit değişkeninin değeri 50'dir.

Fonksiyonun içinde global yakit yazıldığı için dışarıdaki
değişken kullanılır.

Fonksiyon yakit değerine 20 ekler.

Bu yüzden çıktı 70 olur.

Çıktı:
70

## Örnek 3 - Nonlocal Kullanımı

Dış fonksiyonda yakit değişkeninin değeri 50'dir.

İç fonksiyonda nonlocal yakit kullanıldığı için
dış fonksiyondaki değişken değiştirilir.

İç fonksiyon yakit değerine 20 ekler.

Bu yüzden çıktı 70 olur.

Çıktı:
70

Global genel düzeydeki değişkeni, nonlocal ise
dış fonksiyondaki değişkeni değiştirmek için kullanılır.