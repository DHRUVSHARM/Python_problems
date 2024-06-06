def lcs(x, y):
    """
    longest common subsequence b/w x and y
    :param x: x
    :param y: y
    :return: None
    """

    X = list(x)
    Y = list(y)
    print(X, Y)

    dp = [[0 for _ in range(len(X) + 1)] for _ in range(len(Y) + 1)]

    for i in range(1, len(Y) + 1):
        for j in range(1, len(X) + 1):
            if Y[i - 1] == X[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                # always better to add equal elements
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for row in dp:
        print(row)

    print("the lcs is : ", dp[len(Y)][len(X)])


if __name__ == "__main__":
    x = "hearty"
    y = "hyena"
    lcs(x, y)
