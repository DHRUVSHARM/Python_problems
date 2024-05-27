import collections

if __name__ == '__main__':
    d = collections.defaultdict(set)
    print(d["a"])


class Solution:
    def minDeletions(self, s: str) -> int:
        frequency, final_set, deletions = collections.defaultdict(int), set(), 0
        for element in s:
            frequency[element] += 1
        for _, value in frequency.items():
            while value > 0 and value in final_set:
                value -= 1
                deletions += 1
            # now we can add the element
            final_set.add(value)

        return deletions

