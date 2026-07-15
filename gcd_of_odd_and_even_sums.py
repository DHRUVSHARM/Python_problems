# 1 <= n <= 10​​​​​​​00
"""
lues:

sumOdd: the sum of the smallest n positive odd numbers.

sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.


if n is odd:
    # (n - 1) // 2 evem. n // 2 odd
    5 we have 2 even 3 odd
else:
    # n // 2 even , n // 2 is odd 
    4 we have 2 even 2 odd 

    
1 + 3 + 5 + ...
x = 3

2(0) + 1 + 2(1) + 1 + ... 2(x - 1) + 1
    
x + ( x - 1)(x)

x ** 2 # sum of odd numbers put x = how many odd


2 + 4 + 6

2(1) + 2(2) + .. 2(x)


//////////////////////////////////
(x)(x + 1) (even)  ,   x**2 (odd) 

if even 
    same for both , so we can take x = n // 2 as gcd
if odd
    (x - 1)(x) even , x ** 2 odd so again , x = n // 2 as gcd
"""


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n # (actuall 2 * n // 2)