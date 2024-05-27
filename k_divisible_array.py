import collections


def solution(a, k):
    ans, freq = 0, collections.defaultdict(int)

    for element in a:
        freq[element % k] += 1

    print(freq)

    for element in sorted(freq.keys()):
        if k - element == element:
            # print("key element : ", element)
            ans += (
                       ((freq[element]) * (freq[k - element] - 1)) // 2
            )
        elif element == 0:
            # print("key element : ", element)

            ans += (
                ((freq[element]) * (freq[element] - 1)) // 2
            )
        elif element < k - element and k - element in freq:
            print("key element : ", element)

            ans += (
                    (freq[element]) * (freq[k - element])
            )

    return ans


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    ans = solution(a, 2)
    print(ans)
