class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        return_string = ''
        for word in word_list:
            index1, index2 = 0, len(word) - 1
            word_list = list(word)
            while index1 < index2:
                word_list[index1], word_list[index2] = word_list[index2], word_list[index1]
                index1, index2 = index1 + 1, index2 - 1
            return_string = return_string + ''.join(letter for letter in word_list) + ' '
        return return_string[:-1]

    def reverseWords2(self, s: str) -> str:
        word_list = s.split(' ')
        rev_str = ''
        for word in word_list:
            rev_str += ' ' + word[::-1]
        return rev_str.lstrip()

    def reverseWords3(self, s: str) -> str:
        return ''.join(' ' + word[::-1] for word in s.split(' '))[1:]

print(Solution().reverseWords3("Let's take LeetCode contest"))
