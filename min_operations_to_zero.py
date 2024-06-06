if __name__ == "__main__":
    x, mask, msb = 0, 1, 0
    while mask <= x:
        print("x : ", x)
        mask = mask << 1
        msb += 1

    msb -= 1
    print("msb : ", msb)
    # -1 msb refers to no 1 bit


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        mask, msb = 1, 0
        while mask <= n:
            mask = mask << 1
            msb += 1

        msb -= 1
        return (1 << (msb + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << msb))
