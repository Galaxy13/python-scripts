import sys


def upper_count(word: str):
    upper_number = 0
    for letter in word:
        if letter.isupper():
            upper_number += 1
    return upper_number


word_set = set()
lower_set = set()
mistakes_count = 0
for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().rstrip('\n')
    word_set.add(word)
    lower_set.add(word.lower())
for word in sys.stdin.readline().rstrip('\n').split():
    if word not in word_set:
        if word.lower() in lower_set:
            mistakes_count += 1
        else:
            if (number_of_uppers := upper_count(word)) > 1 or not number_of_uppers:
                mistakes_count += 1
print(mistakes_count)
