if __name__ == '__main__':
    s = "nnNNYY"
    arr = list(s)
    print(arr)
    for i in range(len(arr) - 1, -1, -3):
        print(arr[i])


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customer_array = list(customers)
        open = [0 for _ in range(0, len(customer_array))]
        closed = [0 for _ in range(0, len(customer_array) + 1)]

        open[0] = 0 if customer_array[0] == 'Y' else 1
        for index in range(1, len(customer_array)):
            open[index] = open[index - 1] + (customer_array[index] == 'N')

        for index in range(len(customer_array) - 1, -1, -1):
            closed[index] = closed[index + 1] + (customer_array[index] == 'Y')

        minimal_penalty, closing_index = float("inf"), -1
        for index in range(0, len(customer_array) + 1):
            penalty = closed[index]
            if index - 1 >= 0:
                penalty += open[index - 1]

            if penalty < minimal_penalty:
                minimal_penalty = penalty
                closing_index = index

        return closing_index
