# this is and algo that finds primes
# complexity is sqrt n


def pf(n):
    prime_factors, f = [], 2

    while f * f <= n:
        if n % f == 0:
            # factor , prime actually
            # the smallest factor will be prime (1 is ignored, and we will never reach the number
            # itself atleast in the loop
            # we remove all powers of this prime
            prime_factors.append(f)
            while n % f == 0:
                n = n // f
            # all the occ of f removed which will prevent composite factors from being formed

        f += 1
    # there is a chance some pf is left or the number itself is left ( if prime) or 1 is left
    # the power of this factor will also be one since if greater than we will enter the loop
    if n > 1:
        print("here , left ...")
        prime_factors.append(n)

    return prime_factors


if __name__ == '__main__':
    print(pf(1))
    print(pf(2))
    print(pf(17))
    print(pf(15))
    print(pf(2 ** 3 * 5 ** 3 * 17 ** 2))
    print(pf(2 ** 3 * 5 ** 3 * 17))
