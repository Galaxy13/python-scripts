def largest_palindrome(letter_s: str) -> int:
    # pointer1, pointer2 = 0, 1
    max_palindrome = letter_s[0]
    for index in range(len(letter_s)):
        pointer1 = pointer2 = index
        while pointer1 >= 0 and pointer2 < len(letter_s) and letter_s[pointer1] == letter_s[pointer2]:
            pointer1 -= 1
            pointer2 += 1
        if len(palindrome := letter_s[pointer1 + 1: pointer2]) > len(max_palindrome):
            max_palindrome = palindrome

    for index in range(len(letter_s) - 1):
        pointer1, pointer2 = index, index + 1
        while pointer1 >= 0 and pointer2 < len(letter_s) and letter_s[pointer1] == letter_s[pointer2]:
            pointer1 -= 1
            pointer2 += 1
        if len(palindrome := letter_s[pointer1 + 1: pointer2]) > len(max_palindrome):
            max_palindrome = palindrome

    return max_palindrome