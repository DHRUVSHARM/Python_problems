class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = {n}

        def sum_of_digits_squared(element: int) -> int:
            sum = 0
            while element:
                sum += ((element % 10)**2)
                element //= 10
            return sum

        while True:
            print("n : ", n)
            print("encountered , ", encountered)
            if n in encountered:
                return False
            n = sum_of_digits_squared(n)
            if n == 1:
                return True
            encountered.add(n)
