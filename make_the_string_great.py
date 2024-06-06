import collections

from numpy.core.defchararray import lower

if __name__ == "__main__":

    def check_lower(element) -> bool:
        return "a" <= element <= "z"

    input = "F"
    print(chr(ord("a") + (ord(input) - ord("A"))))

    print(check_lower("."))


class Solution:
    def makeGood(self, s: str) -> str:
        st = []

        def check_lower(element) -> bool:
            return "a" <= element <= "z"

        def check_upper(element) -> bool:
            return "A" <= element <= "Z"

        def to_lower(element):
            return chr(ord("a") + ord(element) - ord("A"))

        def to_upper(element):
            return chr(ord("A") + ord(element) - ord("a"))

        for c in s:
            if len(st):
                if check_upper(c) and check_lower(st[-1]) and to_lower(c) == st[-1]:
                    st.pop()
                elif check_lower(c) and check_upper(st[-1]) and to_upper(c) == st[-1]:
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)

        return "".join(st)
