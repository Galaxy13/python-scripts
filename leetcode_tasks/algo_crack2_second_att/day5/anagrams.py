from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def three_ordSum(substring: str):
            return sum(ord(char) ** 3 for char in substring)

        substring_length = len(p)
        req_sum = three_ordSum(p)
        init_sum = three_ordSum(s[:substring_length])
        output = []
        for ch_index in range(substring_length - 1, len(s)):
            left = ch_index - substring_length + 1
            if init_sum == req_sum:
                output.append(left)
            if ch_index < len(s) - 1:
                init_sum -= ord(s[left]) ** 3
                init_sum += ord(s[ch_index + 1]) ** 3
        return output
