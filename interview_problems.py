from functools import cache, lru_cache
from sys import setrecursionlimit

# setrecursionlimit(10000)


def add(*args, **kwargs):
    sum = 0
    # args is a tuple
    for arg in args:
        sum += arg

    print(kwargs)

    return sum


print(add(1, 2, 3, 4, 5, c=4, m=0, t=9))


@cache
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(100))
