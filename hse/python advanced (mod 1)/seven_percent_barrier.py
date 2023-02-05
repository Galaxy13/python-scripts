import sys

parties_dict = {}
for input_line in sys.stdin:
    input_line = input_line.rstrip(':\n')
    if input_line == 'PARTIES':
        continue
    if input_line == 'VOTES':
        break
    parties_dict.setdefault(input_line, 0)

for input_line in sys.stdin:
    party = input_line.rstrip('\n')
    if not party:
        break
    parties_dict[party] += 1
sum_of_parties = sum(parties_dict.values())
print(*[party + '\n' for party in parties_dict.keys() if parties_dict[party] * 100 / sum_of_parties >= 7], sep='')

# 13800f616c0369cd9d566c4aa85b0426