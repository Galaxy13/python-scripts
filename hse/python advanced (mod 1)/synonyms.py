import sys

synonyms_dict = dict()
for _ in range(int(sys.stdin.readline())):
    words = sys.stdin.readline().rstrip('\n').split()
    synonyms_dict[words[0]] = words[1]
    synonyms_dict[words[1]] = words[0]
print(synonyms_dict[sys.stdin.readline().rstrip('\n')])