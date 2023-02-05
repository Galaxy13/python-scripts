import sys

word_dict = dict()
for input_line in sys.stdin:
    words = input_line.rstrip('\n').split()
    if not words:
        break
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
word_dict = dict(sorted(word_dict.items()))
print(list(word_dict.keys())[list(word_dict.values()).index(max(word_dict.values()))])

# 4809f12de8e700315e2378bd26073f22