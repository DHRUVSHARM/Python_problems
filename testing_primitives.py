def is_primitive_root(candidate, modulus):
    seen = set()
    for x in range(1, modulus):  # We check the powers from 1 up to modulus-1 (4972)
        result = pow(candidate, x, modulus)
        if result in seen:
            return False  # Found a duplicate result before reaching modulus-1, not a primitive root
        seen.add(result)
    return len(seen) == modulus - 1  # Check if we've seen all possible non-zero elements

# Modulus value
modulus = 4973

# List of candidate primitive elements to test
candidates = [1006, 1007, 1008, 1011]

# Test each candidate
if __name__ == '__main__':

    test_results = {candidate: is_primitive_root(candidate, modulus) for candidate in candidates}
    print(test_results)
