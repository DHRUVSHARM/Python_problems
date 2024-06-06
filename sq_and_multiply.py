def square_and_multiply(x, H, n):
    """
    Perform the Square-and-Multiply algorithm for Modular Exponentiation, starting from the MSB.

    Parameters:
    x (int): Base element.
    H (int): Exponent, expressed as a sum of 2^i, with coefficients 0 or 1, starting from the most significant bit.
    n (int): Modulus.

    Returns:
    int: The result of x^H mod n.
    """
    # Convert H to its binary representation, removing the '0b' prefix
    H_bin = bin(H)[2:]

    # Initialize r. The initial step is based on the MSB, so we start with r = 1.
    r = 1
    print("base r , initially : ", r)
    print("exponent created , initially : ", 0)
    print("to create exponent binary : ", H_bin)

    for index, hi in enumerate(
        H_bin
    ):  # Iterate over each bit in H's binary representation
        print(
            "----------------------------------------------------------------------------"
        )
        print("bit seen : ", hi, " , ", "msb -> lsb index : ", len(H_bin) - 1 - index)
        if index != 0:
            print("squaring ....")
            r = pow(r, 2, n)
            # Square r and reduce modulo n , only if not msb
            print("r : ", r)
        if hi == "1":
            print("multiplying ...")
            r = (r * x) % n
            print("r : ", r)
            # Multiply by x and reduce modulo n if the current bit is 1
            print("sq and mul : ", H_bin[: index + 1])
        else:
            print("sq only : ", H_bin[: index + 1])
        print(
            "----------------------------------------------------------------------------"
        )

    return r


if __name__ == "__main__":
    # Example usage
    x = 1234567
    H = 23456789  # Exponent
    n = 3333337  # Modulus
    result = square_and_multiply(x, H, n)
    print(result)

    x = 39
    H = 39  # Exponent
    n = 773  # Modulus
    result = square_and_multiply(x, H, n)
    print(result)
