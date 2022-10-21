class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        index1, index2 = 0, 0
        max_count = 1
        while index2 < len(s):
            if len(set(s[index1:index2 + 1])) != len(s[index1:index2 + 1]):
                if index2 - index1 > max_count:
                    max_count = index2 - index1
                index1 += 1
            index2 += 1
        return max(max_count, index2 - index1)


# print(Solution().lengthOfLongestSubstring(""))

print(id('abc'))
print(id('bac'))
print(id('cvr'))
