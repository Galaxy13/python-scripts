import sys

for a, b in zip(sys.stdin.readline().rstrip().split(), sys.stdin.readline().rstrip().split()):
    print(1, end=' ') if a != b else print(0, end=' ')

# 66b5471eb3d119fa52f004280c33f833