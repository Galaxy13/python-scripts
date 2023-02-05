import sys

words_count = dict()
for input_line in sys.stdin:
    input_line = input_line.rstrip('\n').split()
    if not input_line:
        break
    for word in input_line:
        if word not in words_count:
            words_count[word] = 0
        else:
            words_count[word] += 1
        print(words_count[word], end=' ')

# 8b012bd91cb8687c9b807e82bee25200