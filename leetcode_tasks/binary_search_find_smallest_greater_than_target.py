class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if len(letters) == 1 or letters[-1] <= target:
            return letters[0]
        len_list_idx = len(letters) // 2
        if letters[len_list_idx] > target:
            if letters[len_list_idx - 1] > target:
                return self.nextGreatestLetter(letters[:len_list_idx], target)
            return letters[len_list_idx]
        elif letters[len_list_idx] <= target:
            return self.nextGreatestLetter(letters[len_list_idx:], target)



sol = Solution()
print(sol.nextGreatestLetter(['c', 'f', 'j'], 'a'))
