class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left , right , ans = 0 , 0 , []

        while left < len(firstList) and right < len(secondList):
            sl , el = firstList[left]
            sr , er = secondList[right]

            if sl <= sr:
                # reference point is the left interval
                if el < sr:
                    # skip 
                    left += 1
                elif sr <= el <= er:
                    # overlap
                    ans.append([max(sl , sr) , min(el , er)])
                    left += 1
                else:
                    # left interval complete cover
                    ans.append([max(sl , sr) , min(el , er)])
                    right += 1
            else:
                # reference point is the right interval
                if er < sl:
                    # skip 
                    right += 1
                elif sl <= er <= el:
                    # overlap
                    ans.append([max(sl , sr) , min(el , er)])
                    right += 1
                else:
                    # right interval complete cover
                    ans.append([max(sl , sr) , min(el , er)])
                    left += 1
        
        return ans