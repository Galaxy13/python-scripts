def largest_palindrome(letter_s: str) -> int:
    pointer1, pointer2 = 0, 1
    max_palindrome = letter_s[0]
    while pointer2 < len(letter_s):
        if letter_s[pointer1] == letter_s[pointer2]:
            if pointer1 > 0 and pointer2 < len(letter_s) - 1 and letter_s[pointer1 - 1] == letter_s[pointer2] and\
                    letter_s[pointer1 - 1] != letter_s[pointer2 + 1]:
                pointer1 -= 1
            while pointer2 < len(letter_s) - 1 and pointer1 > 0 and letter_s[pointer1 - 1] == letter_s[pointer2 + 1]:
                pointer1 -= 1
                pointer2 += 1
            else:
                if len(palindrome := letter_s[pointer1: pointer2 + 1]) > len(max_palindrome):
                    max_palindrome = palindrome
            pointer1 = pointer2
            pointer2 = pointer1 + 1
        elif pointer2 < len(letter_s) - 1 and letter_s[pointer1] == letter_s[pointer2 + 1]:
            pointer2 += 1
        else:
            pointer1 = pointer2
            pointer2 = pointer1 + 1
    return max_palindrome

# print(largest_palindrome(input()))

