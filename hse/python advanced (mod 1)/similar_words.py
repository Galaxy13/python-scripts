import sys

cars = sys.stdin.readline().rstrip().split()
scores = sys.stdin.readline().rstrip().split()
values = filter(lambda x: float(x[0]) > 0.5, sorted(zip(scores, cars), reverse=True))
for x in values:
    print(x[1])

# 3229b7f9444e5492549ee427d670aa63