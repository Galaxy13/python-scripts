import sys

number_of_words = int(sys.stdin.readline().rstrip('\n'))
word_len_freq = {}
for word in sys.stdin:
    word = word.rstrip('\n')
    if not word:
        break
    if not word_len_freq.get(len(word)):
        word_len_freq[len(word)] = []
    word_len_freq[len(word)].append(word[::-1])
for len_of_word in sorted(word_len_freq):
    for word in sorted(word_len_freq[len_of_word]):
        print(word[::-1])

# 68d5249c011a2047a3c8e92a540399c2