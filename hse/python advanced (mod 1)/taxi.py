import sys

distances = sorted(list(map(int, sys.stdin.readline().rstrip('\n').split())))
fares = sorted(list(map(int, sys.stdin.readline().rstrip('\n').split())), reverse=True)
taxi_payment = 0
for index in range(len(distances)):
    taxi_payment += distances[index] * fares[index]
print(taxi_payment)