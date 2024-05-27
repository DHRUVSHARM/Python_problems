# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        return -1

    def length(self) -> int:
        return -1


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_index, left, right = -1, 0, mountain_arr.length() - 1
        mid = (left + right) // 2
        print("left , right , mid : ", mountain_arr.get(left), mountain_arr.get(right), mountain_arr.get(mid))

        while (right - left + 1) >= 3:
            print("left , right , mid : ", left, right, mid)
            if mountain_arr.get(mid - 1) > mountain_arr.get(mid):
                right = mid
            else:
                peak_index = mid
                left = mid
            mid = (left + right) // 2

        print("peak index : ", peak_index)

        def find_element(l, r, t) -> int:
            # print("l , r: " , l , r)
            target_index = -1
            while l <= r:
                mid = (l + r) // 2
                mid_element = mountain_arr.get(mid)
                if mid_element == t:
                    target_index = mid
                    break
                elif mid_element < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return target_index

        def find_element2(l, r, t) -> int:
            # print("l , r: " , l , r)
            target_index = -1
            while l <= r:
                mid = (l + r) // 2
                mid_element = mountain_arr.get(mid)
                if mid_element == t:
                    target_index = mid
                    break
                elif mid_element > target:
                    l = mid + 1
                else:
                    r = mid - 1
            return target_index

        result = find_element(0, peak_index, target)
        if result != -1:
            return result
        # print("**************************")
        result = find_element2(peak_index + 1, mountain_arr.length() - 1, target)
        if result != -1:
            return result

        return result
