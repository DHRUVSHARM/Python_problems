"""
Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3

# from 0 .. i with last finger as 1 

   i - 1                         i
                    choose the last finger as l
                           l [c]

     
prev: 
left finger is at i - 1 # simple use the same finger, + dist(mov) , right stays the same 
or right finher is at i - 1 , left can be at any pistion - > curr posit, keep thje right one the same

curr = word[i] , prev = word[i - 1]


# means that the current thing is valid (one finger either left or right is on the curr , and the other is coming in can be left or right ) 
dp[i][other] = min (
    dp[i - 1][k] + dis(prev , curr) for all k  # other can be any k but we still move prev to curr 
)
but this already covered under looping for other 

so can we just for all i, for all other, 
dp[i][other] : # till i, some finger has curr, prev is covered by other finger ? 
    = min (
        dp[i - 1][other] + dist(prev , curr) # one finger on prev, move that finger from prev to current , keep other as is 
        
    )

    dp[i][prev] =  # one finger on i, other one on prev
                    dp[i - 1][other] + dist(other , curr) # one finger on prev, dont move that move the other to the curr


                    base case dp[0][other] = 0 for all other since one finger is on curr

                    

    for i in range(1 , ..):
        prev, curr = arr[i - 1] , arr[i]
        for other in range(0   , 26):
            

 //////////////////////////////////////////////////////////////////////////////////////////////////////////////                                  

dp[i][0] = min (
    dp[i - 1][0] + abs(one(i - 1) - curr(i)) # use same finger ,
        one[i] = curr[i]
        second[i] = second[i - 1]
    
    dp[i - 1][1] + (second(i - 1) - curr(i))
        second[i] = curr[i]
        first[i] = first[i - 1]
)



if none then choose as equal to current 


            C                   A       K       E      
dp[0]      (0 , C , None)       
dp[1]      (0 , None , C)


////////////////////////////////////////////////////////////////

dp[i][l][r] # from 0 .. i , and pos l is in l and r is at r minimal

# only valid state at i  

dp[i][curr][r]
dp[i][l][curr]
# exacltly one of l, r is curr



dp[i][curr][r] = min(
    dp[i - 1][prev][r] + dist(prev , curr) # move left ,
    dp[i - 1][l = k][prev] + dist(k , curr) # left free to move comes to curr for all k 
    
)

dp[i][l][curr] = min(
    dp[i - 1][l][prev] + dist(prev , curr) # move right 
    dp[i - 1][prev][r = k] + dist(k , curr) # right free to move and comes to curr , for all k 
)


dp[i][all l][all r] , n * 26 * 26 complexity 

base case only curr
dp[0][curr][for all r] = 0
dp[0][for all l][curr] = 0


"""
class Solution:
    def dist(self, x, y):
        # absolute diff from computed indices 
        x1 , y1 , x2 , y2 = x // 6 , x % 6 , y // 6 , y % 6
        return abs(x1 - x2) + abs(y1 - y2)

    def minimumDistance(self, word: str) -> int:
        
        word_ord = [ord(c) - ord('A') for c in word]
        # dp[i][l][r] : min dist to type till ...i with left finger on l and right finger on r 
        # r , l , i
        # indexed as i , l , r 
        dp = [[[float("inf") for _ in range(0 , 26)] for _ in range(0 , 26)] for _ in range(0 , len(word_ord))]

        # base cases, will also cover naive cases like both fingers on the same curr, but will not affect final 
        # answer 
        # print(word_ord)
        curr = word_ord[0] 
        for l in range(0 , 26):
            for r in range(0 , 26):
                dp[0][curr][r] = 0
                dp[0][l][curr] = 0

        for i in range(1  , len(word_ord)):
            prev, curr = word_ord[i - 1] , word_ord[i]

            # first we check if the curr is covered by the left finger 
            for r in range(0 , 26):
                dp[i][curr][r] = min(dp[i][curr][r] , dp[i - 1][prev][r] + self.dist(prev , curr)) # move the left to curr from prev 
                # right finger is on prev and move left from the remaining k to the curr
                for k in range(0 , 26):
                    dp[i][curr][prev] = min(dp[i][curr][prev] , dp[i - 1][k][prev] + self.dist(k , curr))


            for l in range(0 , 26):
                dp[i][l][curr] = min(dp[i][l][curr] , dp[i - 1][l][prev] + self.dist(prev , curr))
                for k in range(0 , 26):
                    dp[i][prev][curr] = min(dp[i][prev][curr] , dp[i - 1][prev][k] + self.dist(k , curr))

        # final result can be across, l, r combinations 
        result = float("inf")
        for l in range(0 , 26):
            for r in range(0 , 26):
                result = min(result , dp[-1][l][r])
        
        return result