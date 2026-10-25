
import time
from functools import wraps, lru_cache


# GOREV 1 - SURE OLCME

def sure_olc(func):
    """Fonksiyonun calisma suresini olcer."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            sure = time.perf_counter() - baslangic
            print(f"{func.__name__} çalışma süresi: {sure:.4f} sn")

    return wrapper


# Onceki testlerle uyumluluk
zaman_olc = sure_olc


# GOREV 2 - CAGRI SAYACI

def say(func):
    """Fonksiyonun kac kez cagrildigini sayar."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper


@say
def fib_sadece_say(n: int) -> int:
    """Onbelleksiz Fibonacci."""
    if n < 2:
        return n
    return fib_sadece_say(n - 1) + fib_sadece_say(n - 2)


@say
@lru_cache(maxsize=None)
def fib_say_ustte(n: int) -> int:
    """Say disarida, onbellek iceride."""
    if n < 2:
        return n
    return fib_say_ustte(n - 1) + fib_say_ustte(n - 2)


@lru_cache(maxsize=None)
@say
def fib_cache_ustte(n: int) -> int:
    """Onbellek disarida, say iceride."""
    if n < 2:
        return n
    return fib_cache_ustte(n - 1) + fib_cache_ustte(n - 2)


# GOREV 3 - FONKSIYON LOGU

def log_cagri(func):
    """Fonksiyonun giris ve cikis bilgilerini yazdirir."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        parametreler = [repr(a) for a in args]
        parametreler += [
            f"{k}={v!r}" for k, v in kwargs.items()
        ]

        print(f"-> {func.__name__}({', '.join(parametreler)})")

        sonuc = func(*args, **kwargs)

        print(f"<- {func.__name__} = {sonuc!r}")

        return sonuc

    return wrapper


# GOREV 5 - SINIR KONTROLU

def sinirla(alt, ust):
    """Ilk parametreyi verilen aralikta kontrol eder."""
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                miktar = args[0]
            else:
                miktar = kwargs["miktar"]

            if not alt <= miktar <= ust:
                raise ValueError(
                    f"{func.__name__}: {miktar} değeri "
                    f"{alt}-{ust} aralığında değil"
                )

            return func(*args, **kwargs)

        return wrapper

    return dekorator


@sinirla(0, 100)
def yakit_harca(miktar):
    """100 birimlik depodan yakit harcar."""
    return 100 - miktar


# BONUS - KENDI ONBELLEK DEKORATORUMUZ

def hafiza(maxsize=None):
    """Sonuclari sozlukte saklayan onbellek dekoratoru."""
    def dekorator(func):
        onbellek = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            anahtar = (
                args,
                tuple(sorted(kwargs.items()))
            )

            if anahtar in onbellek:
                return onbellek[anahtar]

            sonuc = func(*args, **kwargs)

            if maxsize != 0:
                if maxsize is not None and len(onbellek) >= maxsize:
                    ilk_anahtar = next(iter(onbellek))
                    del onbellek[ilk_anahtar]

                onbellek[anahtar] = sonuc

            return sonuc

        return wrapper

    return dekorator
