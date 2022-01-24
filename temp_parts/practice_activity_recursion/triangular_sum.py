def recursive_sum(x):
    if x == 0:
        return x
    return x + recursive_sum(x-1)

print(recursive_sum(3))