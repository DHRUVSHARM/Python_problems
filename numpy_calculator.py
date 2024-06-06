import numpy as np


def process_and_stack(matrix):
    # Ignore the last column and normalize
    normalized_matrix = np.array(matrix)[:, :-1] / 255.0
    # Add a column of ones to the end of the matrix for bias
    ones_column = np.ones((normalized_matrix.shape[0], 1))
    biased_matrix = np.hstack((normalized_matrix, ones_column))
    return biased_matrix


def calculate_accuracy(vector1, vector2):
    """
    Calculate the accuracy percentage based on the number of matches
    between two numpy column vectors of the same length.

    Parameters:
    - vector1: First numpy column vector.
    - vector2: Second numpy column vector.

    Returns:
    - Accuracy as a percentage of matches.
    """
    if (
        vector1.shape != vector2.shape
        or len(vector1.shape) != 2
        or vector1.shape[1] != 1
    ):
        raise ValueError("Both inputs must be column vectors of the same size.")

    # Calculate matches as a boolean array
    matches = vector1 == vector2

    # Calculate accuracy
    accuracy = (
        np.mean(matches) * 100
    )  # np.mean computes the fraction of matches, multiplying by 100 gives the percentage

    return accuracy


if __name__ == "__main__":
    D = [
        [255, 128, 128, 0, 0],
        [55, 128, 128, 128, 2],
        [192, 128, 128, 0, 0],
        [100, 128, 128, 100, 2],
        [30, 64, 128, 30, 4],
        [20, 64, 128, 0, 4],
    ]

    # Process the matrix
    processed_matrix = process_and_stack(D)

    print("images")
    print(processed_matrix)

    # Update the weight and bias size to match the processed_matrix (including bias)
    # weight_and_bias = np.array([0, 0, 0, 0, 0])
    # 2nd iteration
    """
    [[0.29215686]
    [0.16732026]
    [0.16732026]
    [0.        ]
    [0.33333333]]
    """
    weight_and_bias = np.array([0.29215686, 0.16732026, 0.16732026, 0.0, 0.33333333])
    weight_and_bias = weight_and_bias.reshape(-1, 1)

    print("weight and bias : ")
    print(weight_and_bias)

    # multiply and get f(x)
    classification_output = np.dot(processed_matrix, weight_and_bias)
    print("class op ")
    print(classification_output)

    # Assign 1 if op > 0 else 0
    classification_result = (classification_output > 0).astype(int)
    classification_result = classification_result.reshape(-1, 1)
    print("Final Classification:")
    print(classification_result)

    # Encoded ground truth
    encoded_gt = np.array([1, 0, 1, 0, 0, 0])
    encoded_gt = encoded_gt.reshape(-1, 1)

    print("encode gt : ")
    print(encoded_gt)

    # alpha (ak - fk)
    alpha = encoded_gt - classification_result
    print("alpha")
    print(alpha)

    # Scale each row of the processed_matrix by the corresponding alpha value
    scaled_matrix = processed_matrix * alpha
    print("scaled matrix : ")
    print(scaled_matrix)
    # Calculate the average of each column in the scaled matrix
    column_averages = np.mean(scaled_matrix, axis=0)
    print("Column Averages (Updates):")
    print(column_averages)

    print("\n")
    new_weights = column_averages.reshape(-1, 1) + weight_and_bias
    print("new weights ..")
    print(new_weights)
    print("new weights : ", new_weights)

    print("getting accuracy : ")
    score = np.dot(processed_matrix, new_weights)
    print(score)
    score = (score > 0).astype(int)
    print("final classifications")
    print(score)

    print("Accuaracy : ")
    print(calculate_accuracy(encoded_gt, score))
