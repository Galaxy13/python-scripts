import sys

customer_size = int(sys.stdin.readline().rstrip('\n'))
sizes = [int(size) for size in sys.stdin.readline().rstrip('\n').split() if int(size) >= customer_size]
sizes.sort()
num_of_pairs = 1 if len(sizes) else 0
if len(sizes):
    current_pair = sizes[0]
for pair in sizes[1:]:
    if pair - current_pair >= 3:
        num_of_pairs += 1
        current_pair = pair
print(num_of_pairs)

# 49e53f94f0eeafc3c54caeb565872373

