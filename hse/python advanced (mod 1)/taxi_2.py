import sys

distances = enumerate(sys.stdin.readline().rstrip().split())
fares = enumerate(sys.stdin.readline().rstrip().split())

new_values = sorted(zip(sorted(distances, key=lambda x: int(x[1])), sorted(fares, key=lambda x: int(x[1]), reverse=True)), key=lambda x: x[0][0])
for x in new_values:
    print(x[1][0], end=' ')