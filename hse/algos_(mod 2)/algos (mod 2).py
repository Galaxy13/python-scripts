def lines(line: list) -> int:
    pointer1, pointer2 = 0, 1
    count = 0
    while pointer2 < len(line):
        while pointer2 < len(line) and line[pointer1] == line[pointer2]:
            pointer2 += 1
        else:
            if (num_of_erased := pointer2 - pointer1) > 2:
                line = line[:pointer1] + line[pointer2:]
                count += num_of_erased
                pointer1, pointer2 = 0, 1
                continue
        pointer1 = pointer2
        pointer2 = pointer1 + 1
    return count


print(lines([int(x) for x in input().split()]))

