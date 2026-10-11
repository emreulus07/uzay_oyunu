def gorev_kaydi(gorev, *adimlar, oncelik="normal", **ekler):
    metin = "[" + oncelik.upper() + "] " + gorev

    for numara, adim in enumerate(adimlar, 1):
        metin = metin + "\n  " + str(numara) + ". " + adim

    for anahtar, deger in ekler.items():
        metin = metin + "\n  " + anahtar + ": " + str(deger)

    return metin