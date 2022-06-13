def solution(l):
    count_of_divisors = {index:0 for index in range(len(l))}
    count_of_lucky_triples = 0
    for index_r in range(len(l)):
        for index_l in range(0, index_r):
            if not l[index_r] % l[index_l]:
                count_of_divisors[index_r] += 1
                count_of_lucky_triples += count_of_divisors[index_l]
    return count_of_lucky_triples



