class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        index1, index2 = 0, len(s) - 1
        while index1 < index2:
            s[index1], s[index2] = s[index2], s[index1]
            index1, index2 = index1 + 1, index2 - 1


print(Solution().reverseString([2,4,5,6]))