def knapsack(items, total_weight_limit):
    """
    function that will solve the 0/1 knapsack problem
    :param items: elements
    :param total_weight_limit: total weight allowed
    :return: None
    """

    dp = [[0 for _ in range(total_weight_limit + 1)] for _ in range(len(items) + 1)]
    for j in range(1, len(items) + 1):
        for w in range(1, total_weight_limit + 1):
            weight, cost = items[j - 1][0], items[j - 1][1]
            dp[j][w] = dp[j - 1][w]
            if w - weight >= 0:
                dp[j][w] = max(dp[j][w], cost + dp[j - 1][w - weight])

    print("the dp is : ")
    for row in dp:
        print(row)

    print("the maximal reward possible is : ", dp[len(items)][total_weight_limit])


if __name__ == "__main__":
    total_weight_limit = 6
    # items are pairs of weight , cost (reward)
    items = [(2, 7), (6, 14), (1, 3), (4, 11), (2, 6)]
    # we want to maximize the reward
    knapsack(items, total_weight_limit)
