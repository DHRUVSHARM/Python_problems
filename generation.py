# Adjusting the approach to find at least one generator for each subgroup by checking the orders of elements from 1
# to 4972.


def divisors(n):
    """Helper function to find divisors of a number."""
    return [i for i in range(1, n + 1) if n % i == 0]


def find_generator_and_subgroups(modulus):
    order = modulus - 1  # Full group order
    subgroup_generators = {
        d: None for d in divisors(order)
    }  # Prepare a dictionary for subgroup generators

    for a in range(1008, modulus):  # Start checking from 1001 up to modulus-1
        # Find the smallest k such that a^k % modulus = 1
        for k in range(1, order + 1):
            if pow(a, k, modulus) == 1:
                if k in subgroup_generators and subgroup_generators[k] is None:
                    subgroup_generators[k] = (
                        a  # Assign a as a generator for the subgroup of size k
                    )
                break  # Stop as soon as the order of a is found

        # Early exit if all subgroup sizes have their generators
        if None not in subgroup_generators.values():
            break

    return subgroup_generators


# Find generators for each subgroup size in Z/4973Z

if __name__ == "__main__":
    subgroup_generators = find_generator_and_subgroups(4973)
    print(subgroup_generators)
    # Display the mapping of subgroup sizes to their generators
