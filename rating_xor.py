import collections


def foo(arr):
    rating, left, xor_sum, xor_sums = 0, 0, 0, collections.defaultdict(int)

    d = []
    c = 0
    for element in arr:
        c = c ^ element
        d.append(c)

    print(d)

    xor_sum = 0
    for r in range(0, len(arr)):
        xor_sum = xor_sum ^ arr[r]

        print(xor_sum, r)

        if xor_sum in xor_sums:
            # potential ans
            if r - xor_sums[xor_sum] + 1 >= 3:
                rating += (r - xor_sums[xor_sum] - 1)
        else:
            xor_sums[xor_sum] = r

    return rating


def foo1(arr):
    rating, left, xor_sum = 0, 0, 0
    for i in range(0, len(arr) - 1):
        xor_sum = arr[i] ^ arr[i + 1]
        for j in range(i + 2, len(arr)):
            xor_sum ^= arr[j]
            if xor_sum == 0:
                rating += 1
    return rating


if __name__ == '__main__':
    a = [3, 7, 4, 0]
    print(foo1(a))
    # print(2 ^ 2)
