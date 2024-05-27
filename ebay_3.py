def partition_matrix(matrix, row, col):
    # Determine the dimensions of the original matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Ensure that the specified row and column are within the matrix bounds
    if row >= num_rows or col >= num_cols:
        raise ValueError("Invalid row or column indices")

    # Initialize submatrices
    top_left = [matrix[i][:col + 1] for i in range(row + 1)]
    top_right = [matrix[i][col + 1:] for i in range(row + 1)]
    bottom_left = [matrix[i][:col + 1] for i in range(row + 1, num_rows)]
    bottom_right = [matrix[i][col + 1:] for i in range(row + 1, num_rows)]

    return top_left, top_right, bottom_left, bottom_right


def foo(matrix):
    row = 0
    col = 0
    m, n = len(matrix), len(matrix[0])
    averages = []

    def calculate_non_negative_average(submatrix):
        non_negative_values = [value for row in submatrix for value in row if value >= 0]
        if non_negative_values:
            return sum(non_negative_values) // len(non_negative_values)
        return None

    for row in range(0, m - 1):
        for col in range(0, n - 1):
            submatrices = partition_matrix(matrix, row, col)
            for submatrix in submatrices:
                """
                for row in submatrix:
                    print(row)
                print()
                """
                average = calculate_non_negative_average(submatrix)
                if average is not None:
                    averages.append(average)
    if averages:
        sorted_averages = sorted(averages)
        return sorted_averages
    else:
        return None


# Example usage:
if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    foo(matrix)
