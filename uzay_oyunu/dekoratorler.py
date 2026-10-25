
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
