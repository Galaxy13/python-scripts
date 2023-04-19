import sys

word_dict = {}
index_counter = 0
for input_line in sys.stdin:
    if input_line == '\n':
        break
    words = input_line.rstrip('\n').split()
    for word in words:
        if (word_index := word_dict.get(word, None)) is None:
            print(-1, end=' ')
        else:
            print(word_index, end=' ')
        word_dict[word] = index_counter
        index_counter += 1

# 05f0753b2f462add65a77d88ca5d89c5

