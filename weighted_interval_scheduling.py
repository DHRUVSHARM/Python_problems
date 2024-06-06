import bisect


def weighted_interval_scheduling(intervals):
    n = len(intervals)
    # first we sort the intervals by finish time
    intervals.sort(key=lambda interval: interval[1])
    print("intervals is : ", intervals)
    # now we create the rho array
    rho = []

    def binary_search_right(arr, left, right, start):
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            if arr[mid][1] <= start:
                left += 1
            else:
                right -= 1
        # invariant method of bs , finally we will get [l , r] and l will have the right answer
        return left + 1

    rho = [
        binary_search_right(intervals, -1, i + 1, intervals[i][0]) for i in range(0, n)
    ]
    print("rho is : ", rho)
    dp = [0 for _ in range(n + 1)]
    for i in range(1, len(dp)):
        dp[i] = max(
            dp[i - 1], intervals[i - 1][1] - intervals[i - 1][0] + dp[rho[i - 1]]
        )
    print("dp is : ", dp)


if __name__ == "__main__":
    arr = [1, 3, 4, 5]
    # bisect and bisect right is the same
    print(bisect.bisect(arr, 2))
    # bisect gives the index of the last occ + 1 or first element greater than given element
    print(bisect.bisect_left(arr, 2))
    # gives the index of the first occ or same as bisect
    # thus , bisect and bisect_left are equal iff the element does not exist in the array

    # now we write the weighted interval scheduling algorithm
    intervals = [(1, 4), (3, 5), (0, 6), (4, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
    weighted_interval_scheduling(intervals)
