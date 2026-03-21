# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""

length is atleast 3

structure 

x , y  , peak , smaller elements

There exists some i with 0 < i < arr.length - 1 such that:

all elements are distinct 
                                            peak
arr[0] < arr[1] < ... < arr[i - 1] <  (    arr[i]   ) > arr[i + 1] > ... > arr[arr.length - 1]

fundamentally:

left < mid > right  peak

left < mid < right - left side 
left > mid > right - right side

we know peak lies in the middle so we move there 

       l      
[1,2,3,4,5,3,1]

"""


class Solution:

    def find(self, target , arr , l , r , increasing=True)->int:
        """
        bs based find function that finds the element in the array 
        -1 if not found 
        """
        # [l , r]
        if r - l + 1 < 1:
            return - 1

        # 1000
        # f  f    t     t
        # >= target , find the first if equal then return index
        # 1 , 2 , 10 , 100    

        left , right = l-1 , r+1
        while left + 1 < right:
            mid = (left + right) // 2
            
            if arr.get(mid) < target:
                if increasing:
                    left = mid
                else:
                    right = mid
            else:
                if increasing:
                    right = mid
                else:
                    left = mid
        

        if increasing:
            if right < (r + 1) and arr.get(right) == target:
                return right
            else:
                return -1
        else:
            if left > (l - 1) and arr.get(left) == target:
                return left
            else:
                return -1
 
    

    def find_peak(self , arr) ->int:
        """
        peak is guaranteed and the arr input is of size 3 minimum
        returns the peak index
        """
        left, right , peak_index = 0 , arr.length() - 1 , -1

        while (right - left + 1) >= 3 :
            mid = (left + right) // 2
            if arr.get(mid - 1) < arr.get(mid) > arr.get(mid + 1):
                peak_index = mid
                break
            elif arr.get(mid - 1) < arr.get(mid) < arr.get(mid + 1):
                left = mid
            else:
                right = mid
            
        return peak_index

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int: # type: ignore
        # find the peak index
        #class MountainArray:
        # def get(self, index: int) -> int:
        # def length(self) -> int:
        peak_index = self.find_peak(mountainArr)
        l_index = self.find(target , mountainArr , 0 , peak_index)
        if l_index != -1:
            return l_index
        return self.find(target , mountainArr , peak_index + 1 , mountainArr.length() - 1 , increasing=False)