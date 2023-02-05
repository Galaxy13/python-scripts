import sys

word_dict = {}
for input_line in sys.stdin:
    input_line = input_line.rstrip('\n').split()
    if not input_line:
        break
    for word in input_line:
        if not word_dict.get(word, 0):
            word_dict[word] = 0
        word_dict[word] += 1
freq_dict = {}
for word in word_dict:
    if not freq_dict.get(word_dict[word], 0):
        freq_dict[word_dict[word]] = []
    freq_dict[word_dict[word]].append(word)
for frequency in sorted(freq_dict, reverse=True):
    for word in sorted(freq_dict[frequency]):
        print(word)