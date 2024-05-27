import collections


def solution(sentence):
    words = sentence.strip().split(" ")
    # print(words)
    ans = 0
    for word in words:
        frequency = collections.defaultdict(int)
        for c in word:
            frequency[c.lower()] += 1

        for key, value in frequency.items():
            if value >= 3:
                ans += 1
                break

    return ans


if __name__ == '__main__':
    ans = solution("Dooddle moodle Pepper unsuccessfully")
    print(ans)
