from math import floor
percent = int(input())
dollars = int(input())
cents = int(input())
years = int(input())
result = (dollars * 100 + cents)
while years:
    result += floor(result / 100 * percent)
    years -= 1
print(result // 100, result % 100)