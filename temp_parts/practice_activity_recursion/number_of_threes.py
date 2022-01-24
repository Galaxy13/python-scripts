def number_of_threes(x):
    if x < 10 and x != 3:
        return 0
    else:
        if x % 10 == 3:
            return 1 + number_of_threes(x // 10)
        else:
            return number_of_threes(x // 10)

print(number_of_threes(23343))
