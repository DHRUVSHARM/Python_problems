if __name__ == '__main__':
    s = "011011010101"
    print(s.count('0', 0, len(s)))
    s = s.replace('0', '1', 2)
    print(s)


class Solution:
    """
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        return "1" * (one_count - 1) + ("0" * (len(s) - one_count)) + "1"
    """

    def maximumOddBinaryNumber(self, s: str) -> str:
        elements = list(s)
        # we will use a concept similar to the pivot rearrange for quicksort
        # pivot = 1
        # a[....left , left + 1....]
        # where till left >= 1 and after less than 1
        left = -1
        for i in range(0, len(elements)):
            if elements[i] == '1':
                # swap and put it in left
                elements[i], elements[left + 1] = elements[left + 1], elements[i]
                left += 1
            else:
                # do nothing keep moving
                pass

        # swap the last with the end
        elements[left], elements[-1] = elements[-1], elements[left]
        return "".join(elements)