if __name__ == "__main__":
    x = 10
    print("binary bit string repr : ", bin(x))
    print("value at the 32nd bit 0 based : ", (1 << 32) & x)
    # 0 for a positive integer else 2 power 32

    print(
        "the value of 2 power 32 that is the number "
        "represented by 1 on the 32nd (0 based)  bit is is : ",
        2**32,
    )
