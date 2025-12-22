# demonstrate the principle of color compression
def compression(color : int , m: int):
    prev , valid , colors = -1 , True , []

    for _ in range(0 , m):
        current_color = color % 3
        colors.append(current_color)
        if current_color == prev:
            valid = False
            break
        prev = current_color
        color //= 3

    print(colors)
    print("is valid : " , valid)   



if __name__ == '__main__':
    # let us say base 3
    # digits can be 0 , 1 , 2
    # the size can be represented by the rows 

    m = 4

    # 0120
    encoded_color = 0 * (3**0) + 1 * (3**1) + 2 * (3**2) + 0 * (3**3)
    compression(encoded_color , 4)

    # this extracts the colors sequentially and checks repeating 
    # 0122
    encoded_color_duplicate = 0 * (3**0) + 1 * (3**1) + 2 * (3**2) + 2 * (3**3)
    compression(encoded_color_duplicate , 4)


