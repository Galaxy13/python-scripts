def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if not n % 2:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n +=1
        count += 1
    return count



print(solution("15"))

