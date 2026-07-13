from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # can we solve with digit dp ?
        # 10 <= low <= high <= 10^9
        """
        enumeration 

        1  8   7   6   5    4  3   2    1
        _   _   _   _   _   _   _   _   _

        8! + 7! + 6! + ... constant complexity since limited number of cases 
        
        """

        ans = []

        # outer loop is number of digit places 
        for digit_places in range(1 , 11):
            # 9 digits max
            for start_d in range(1 , 10):
                number = 0 # start from digit 1 since we would need that and 
                d = start_d # start from digit 1 
                # seq has to increase 
                if 10 - start_d >= digit_places:
                    for _ in range(0 , digit_places):
                        number = (10 * number) + d                 
                        d += 1
    

                    if low <= number <= high:
                        ans.append(number)
                    elif number > high:
                        break
        
        return ans

