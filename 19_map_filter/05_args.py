def sum(*args):
    # args will be the tuple of all the values passed to the sum.
    total = 0
    for item in args:
        total += item
    return total
print(sum(343, 5, 7, 5))