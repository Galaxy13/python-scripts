import sys

numbers_q = int(sys.stdin.readline().rstrip('\n'))
comparison_value_dict = {}


def new_value(number: str):
    pointer1, pointer2 = 0, len(number) - 1
    new_number = 0
    while pointer1 < pointer2:
        new_number += (int(number[pointer1]) - int(number[pointer2]))
        pointer1 += 1
        pointer2 -= 1
    return new_number


for _ in range(numbers_q):
    number = sys.stdin.readline().rstrip('\n')
    if not number:
        break
    if not comparison_value_dict.get(new_num := new_value(number), 0):
        comparison_value_dict[new_num] = []
    comparison_value_dict[new_num].append(int(number))
for value in sorted(comparison_value_dict):
    for old_value in sorted(comparison_value_dict[value]):
        print(old_value)