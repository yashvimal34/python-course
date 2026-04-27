from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]  # let us know how it works.
        # [3, 3, 4, 5, 6]
        # [6, 4, 5, 6]
        # [10, 5, 6]
        # [15, 6]
        # [21]
        # This is how reduce works.

def sum(a, b):
    return a + b

new = reduce(sum, numbers)
print(new)