class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        we need to count a value made by the subarrays, not the subarrays themselves
        so we would need something like a set to enumerate and count 


        """

        # base case 
        ans , n = set([arr[0]]) , len(arr)
        prev_subarray_sum = set([arr[0]])

        for index in range(1 , n):
            curr_res = set()
            for prev_or in prev_subarray_sum:
                curr_res.add(prev_or | arr[index])
            ans = ans | curr_res
            prev_subarray_sum = curr_res

        return len(ans)