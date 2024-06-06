def getMaxLengthSubarray(arr, K):
    N = len(arr)
    l = N
    i = 0
    maxlen = 0
    max_len_start, max_len_end = 0, 0
    while i < l:
        j = i
        while i + 1 < l and (abs(arr[i] - arr[i + 1]) <= K):
            i += 1

        # Length of the valid sub-array
        # currently under consideration
        currLen = i - j + 1

        # Update the maximum length subarray
        if maxlen < currLen:
            maxlen = currLen
            max_len_start = j
            max_len_end = i

        if j == i:
            i += 1

    return [max_len_start, max_len_end]


if __name__ == "__main__":
    # Driver code
    arr = [
        33,
        13,
        15,
    ]
    K = 2
    N = len(arr)
    l, r = getMaxLengthSubarray(arr, K)
    print(l, " , ", r)
