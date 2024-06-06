"""
def solution(numbers):
    # print(numbers)
    n = len(numbers)
    unique_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            str1 = str(numbers[i])
            str2 = str(numbers[j])
            # print("i , j:  ", i, " ", j)

            if len(str1) == len(str2):
                if sorted(str1) == sorted(str2):
                    if len([None for k in range(len(str1)) if str1[k] != str2[k]]) <= 2:
                        unique_pairs += 1
    return unique_pairs
"""

"""
def standard_representation(num):
    # Sorts the digits of the number and returns a string representation
    return ''.join(sorted(str(num)))

def solution(numbers):
    group_dict = {}
    count = 0

    for index, num in enumerate(numbers):
        std_repr = standard_representation(num)
        if std_repr not in group_dict:
            group_dict[std_repr] = []
        group_dict[std_repr].append(index)

    for indices in group_dict.values():
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                # Count pairs within each group that differ by at most 2 characters
                str1 = str(numbers[indices[i]])
                str2 = str(numbers[indices[j]])

                diff_count = sum(1 for a, b in zip(str1, str2) if a != b)
                if diff_count <= 2:
                    count += 1

    return count
"""


def solution(numbers):
    from collections import defaultdict

    # Create a default dictionary to store lists of anagrams
    anagrams = defaultdict(list)

    # Helper function to create a key for the hash table
    def create_key(number):
        key = [0] * 10  # There are 10 possible digits
        for digit in str(number):
            key[int(digit)] += 1
        return tuple(key)

    # Populate the anagram hash table
    for number in numbers:
        key = create_key(number)
        anagrams[key].append(number)

    # Function to check if two numbers differ by at most two digits
    def differ_by_at_most_two(num1, num2):
        count = 0
        for digit1, digit2 in zip(str(num1), str(num2)):
            if digit1 != digit2:
                count += 1
                if count > 2:
                    return False
        return True

    # Count unique pairs that are anagrams and differ by at most two digits
    unique_pairs = 0
    for key, group in anagrams.items():
        # Check each pair in the group
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                if differ_by_at_most_two(group[i], group[j]):
                    unique_pairs += 1

    return unique_pairs


"""
# Example usage:
numbers = [123, 231, 312, 321, 456, 654]
result = solution(numbers)
print("Number of pairs:", result)
"""

if __name__ == "__main__":
    # ans = solution([1, 23, 156, 1650, 451, 165, 32, 10, 10])
    ans = solution([123, 321, 123])

    print(ans)
