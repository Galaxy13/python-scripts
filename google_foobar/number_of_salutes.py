def solution(s):
    count_to_right, salutes_count = 0, 0
    for symb in s:
        if symb == '>':
            count_to_right += 1
        elif symb == '<':
            salutes_count += (count_to_right * 2)
    return salutes_count
