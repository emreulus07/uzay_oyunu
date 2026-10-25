
import time
from functools import wraps


def zaman_olc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            bitis = time.perf_counter()
            print(f"{func.__name__} çalışma süresi: {bitis - baslangic:.6f} saniye")

    return wrapper

from functools import lru_cache


def say(func):
    """Fonksiyonun kaç kez çağrıldığını sayar."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper


@say
def fib_sadece_say(n: int) -> int:
    """Önbelleksiz Fibonacci hesabı."""
    if n < 2:
        return n
    return fib_sadece_say(n - 1) + fib_sadece_say(n - 2)


@say
@lru_cache(maxsize=None)
def fib_say_ustte(n: int) -> int:
    """Önbellek içeride, sayaç dışarıda."""
    if n < 2:
        return n
    return fib_say_ustte(n - 1) + fib_say_ustte(n - 2)


@lru_cache(maxsize=None)
@say
def fib_cache_ustte(n: int) -> int:
    """Önbellek dışarıda, sayaç içeride."""
    if n < 2:
        return n
    return fib_cache_ustte(n - 1) + fib_cache_ustte(n - 2)

def log_cagri(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parametreler = [repr(a) for a in args]
        parametreler += [f"{k}={v!r}" for k, v in kwargs.items()]

        print(f"-> {func.__name__}({', '.join(parametreler)})")
        sonuc = func(*args, **kwargs)
        print(f"<- {func.__name__} = {sonuc!r}")

        return sonuc

    return wrapper
