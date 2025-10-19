class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total , ans , left , right , cur_sum = sum(cardPoints) , float("-inf") , 0 , len(cardPoints) - k  - 1 , 0

        for index in range(left , right + 1):
            cur_sum += cardPoints[index]
        
        # print(cur_sum)

        ans = max(ans , total - cur_sum)

        while right >= left and right + 1 < len(cardPoints):
            cur_sum -= cardPoints[left]
            cur_sum += cardPoints[right + 1]
            # print(cur_sum)
            ans = max(ans , total - cur_sum)
            right += 1
            left += 1
        

        return ans
