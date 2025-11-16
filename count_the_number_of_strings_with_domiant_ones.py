import unittest
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # idea can be that we can stop if we have more than sqrt(n) zeroes and then work with that  
        zeroes, ans, left, right , max_zeroes = 0 , 0 , 0 , 0 , int(math.sqrt(len(s)))
        prev_0 = {}
        zero_indices = [-1]
        prefix_sums = {-1 : 0}

        for index, element in enumerate(s):
            if element == '0':
                prefix_sums[index] = prefix_sums[index - 1] + 1
                zero_indices.append(index)
            else:
                prefix_sums[index] = prefix_sums[index - 1]

        print("zero indices : " , zero_indices)
        print("prefix_sums : "  , prefix_sums)

        prev_zero_index = len(zero_indices) - 1
        for index in range(len(s) - 1 , -1 , -1):
            if s[index] == '1':
                # prev zero is documented 
                pass
            else:
                # need to move_index
                prev_zero_index = (max(prev_zero_index - 1 , 0))
            prev_0[index] = zero_indices[prev_zero_index]

        
        print("prev zeroes : " , prev_0)

        #print("max zeroes : " , max_zeroes)

        def helper(st , end):
            print("st , end : " , st , " , " , end , " : " , s[left : right + 1])
            return 0

        while right < len(s):
            if s[right] == '0':
                zeroes += 1

            # make sure that the window has zeroes in limit 
            while left <= right and zeroes > max_zeroes:
                if s[left] == '0':
                    zeroes -= 1
                left += 1

            # call the helper to count 
            ans += helper(left , right)

            right += 1


        # return the final answer 
        return ans




class TestProblem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = Solution()

    @classmethod
    def tearDownClass(cls):
        print("complete")

    def test_1(self):
        self.assertEquals(TestProblem.test_obj.numberOfSubstrings("00011") , 0)


    def test_2(self):
        self.assertEquals(TestProblem.test_obj.numberOfSubstrings("101101") , 0)



if __name__ == "__main__":
    unittest.main()