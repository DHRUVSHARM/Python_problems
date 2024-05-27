# Python3 Program to implement
# the above approach

# Function to find maximum
# distance between every
# two element
def max_distance(a, temp, n):
    # Stores index of last
    # occurrence of each
    # array element
    mp = {}

    # Initialize temp[]
    # with -1
    for i in range(1, n + 1):
        temp[i] = -1

    # Traverse the array
    for i in range(n):

        # If array element has
        # not occurred previously
        if (a[i] not in mp):

            # Update index in temp
            temp[a[i]] = i + 1

        # Otherwise
        else:

            # Compare temp[a[i]] with
            # distance from its previous
            # occurrence and store the maximum
            temp[a[i]] = max(temp[a[i]],
                             i - mp[a[i]])

        mp[a[i]] = i

    for i in range(1, n + 1):

        # Compare temp[i] with
        # distance of its last
        # occurrence from the end
        # of the array and store
        # the maximum
        if (temp[i] != -1):
            temp[i] = max(temp[i],
                          n - mp[i])


# Function to find the minimum
# common element in subarrays
# of all possible lengths
def min_comm_ele(a, ans, temp, n):
    # Function call to find
    # a the maximum distance
    # between every pair of
    # repetition
    max_distance(a, temp, n)

    # Initialize ans[] to -1
    for i in range(1, n + 1):
        ans[i] = -1

    for i in range(1, n + 1):

        # Check if subarray of length
        # temp[i] contains i as one
        # of the common elements
        if (ans[temp[i]] == -1):
            ans[temp[i]] = i

    for i in range(1, n + 1):

        # Find the minimum of all
        # common elements
        if (i > 1 and
                ans[i - 1] != -1):

            if (ans[i] == -1):
                ans[i] = ans[i - 1]
            else:
                ans[i] = min(ans[i],
                             ans[i - 1])

        print(ans[i], end=" ")


# Driver Code
if __name__ == "__main__":
    N = 6
    a = [1, 3, 4, 5, 6, 7]
    temp = [0] * 100
    ans = [0] * 100
    min_comm_ele(a, ans, temp, N)
