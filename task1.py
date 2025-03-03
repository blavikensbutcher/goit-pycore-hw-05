from typing import Callable


def caching_fibonacci(n: int) -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci(n)
