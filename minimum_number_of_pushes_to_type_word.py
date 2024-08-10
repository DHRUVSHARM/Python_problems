import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        # mapping key to number of pushes
        k_p = {key: 0 for key in range(2, 10)}
        # mapping letter to key
        l_k = {}

        word_count = [
            (freq, letter) for letter, freq in collections.Counter(word).items()
        ]

        key_index = 2

        for freq, letter in sorted(word_count, reverse=True):

            # if we have this mapped already
            if letter in l_k:
                ans += k_p[l_k[letter]] * freq

            else:
                # we need to slot the letter in
                k_p[key_index] += 1
                l_k[letter] = key_index
                ans += k_p[key_index] * freq

                key_index += 1
                if key_index == 10:
                    key_index = 2

        return ans
