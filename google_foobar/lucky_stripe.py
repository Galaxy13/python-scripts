def solution(l):
    count_stipes = 0
    for index1 in range(len(l) - 2):
        for index2 in range(index1 + 1, len(l) - 1):
            if not l[index2] % l[index1]:
                for index3 in range(index2 + 1, len(l)):
                    if not l[index3] % l[index2]:
                        count_stipes += 1
    return count_stipes