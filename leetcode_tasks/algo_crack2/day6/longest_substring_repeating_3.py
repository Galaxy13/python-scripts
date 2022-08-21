class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window, start_i = 0, 0
        max_count = 0
        while window < len(s):
            if len(s[start_i:window + 1]) != len(set(s[start_i:window + 1])):
                if window - start_i > max_count:
                    max_count = window - start_i
                start_i += 1
            window += 1
        return max(max_count, window - start_i)
