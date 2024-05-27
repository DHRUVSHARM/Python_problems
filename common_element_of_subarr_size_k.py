def minCommonElementInSubarrays(arr, k):
    """
    find the minimal common element of subarr size k else return -1
    :param arr: ip
    :param k: subarr size
    :return: None
    """

    print("the input arr is : ", arr)
    n = len(arr)

    center = (n // 2) - 1

    if k - 1 <= center:
        # never possible to have an overlapping subarr , hence no answer
        return - 1

    min_common_element = float("inf")
    for index in range(n - k, k):
        min_common_element = min(min_common_element, arr[index])
        print("element considered : ", arr[index])

    return min_common_element


if __name__ == '__main__':
    # arr has distinct elements
    arr = [1, 2, 3, 4]
    # subarray size k
    k = 4
    minCommonElementInSubarrays(arr, k)
