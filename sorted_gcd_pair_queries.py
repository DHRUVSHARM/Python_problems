from typing import List

"""
You are given an integer array 
nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.



[2 , 3 , 4]


# first we need to understand that gcd(i , j) for any i, j is <=  min(nums[i] , nums[j])

so gcd(i , j) <= max(nums)

1 <= nums[i] <= 5 * 104

so we can work from there 

if we count the freq of element 

0 1 2 3 4 
    1 1 1

we can calculate divisible by 
by starting from each element and 
calc till the end , 
add all the elements, 
we can make a pair from any 2 of these elements
say 2 , 4 divisible by 2 

so we can also store something where divisible[i] = number of pairs in problem space divisble by i 

basically this means if we have 2 numbere a , b 
a = im
b = iq

let gcd of a, b be g

then divisible[i] = shoulbe atleast gcd[i]
the rem will be 2i, 3i, or so on 
since common divisor


2,3,3,3,4,5,6,6     2,7,21,46


ki <= M
exact_div [i] = gcd(i) , gdc(2i) ... gcd(ki)


gcd[i] = exact_div[i] - (2i ... ki)

gcd[i] = exact_dic[i] - (2i , 3i , 4i .... , ki )


ie;
gcd[i] = exact_div[i] - (sum from 2i , M + 1 , i)
gcd[i - 1] = exact_div[i - 1] - (sum from 2(i - 1) , M + 1 , i - 1)


so we start from M and back say form 
    gcd[M] = exact_div[M] - (2M , M + 1 , M)


    

0   | 1 2 3 ....            M
      count + prefix


      
      [1, 1, 1, 2, 2, 4].

      0  1  2  3  4
      0  3  2  0  1
      0  3  5  5  6

      <=  >
         T
         bisect right will give the one greater, we have index, in the query so > index, ie; where we have seen index elements 
         index means we have seen index elements before current position so this will work 

         1 <= queries.length <= 105
"""
from bisect import bisect_right
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        # 1 ... M
        freq = [0] * (M + 1)
        divsible = [0] * (M + 1) # divisible[i] : number of pairs that are divisible by i 
        gcd = [0] * (M + 1) # gcd(i) : number of pairs that have gcd exactly i 

        for element in nums:
            freq[element] += 1
        
        for i in range(1 , len(divsible)):
            elements = 0
            for multiple in range(i , len(divsible) , i):
                elements += freq[multiple]

            divsible[i] = (elements * (elements - 1)) // 2

        # divisible[i] = gcd(i) + gcd(2i) ....
        # print(divsible)

        for i in range(M , 0 , -1):
            # gcd[i] = exact_div[i] - (sum from 2i , M + 1 , i)
            gcd[i] = divsible[i] # inclusion
            for multiple in range(2*i , M + 1 , i):
                gcd[i] -= gcd[multiple] # exclude multiples of i 
        

        # make prefix sum
        for index in range(1 , len(gcd)):
            gcd[index] += gcd[index - 1]
        
        # use bisect right to answer queries,
        # query[i] = index, => seen index elements before this element appears 

        ans = []
        for q in queries:
            ans.append(bisect_right(gcd , q))
        
        return ans

