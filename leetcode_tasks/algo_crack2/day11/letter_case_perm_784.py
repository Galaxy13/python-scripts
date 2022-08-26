class Solution:
    def letterCasePermutation_depricated(self, s: str) -> list[str]:
        perms = []
        len_of_string = len(s)

        def dfs(sliced_string, perm):
            for symbol_index in range(len(sliced_string)):
                if sliced_string[symbol_index].isalpha():
                    dfs(sliced_string[symbol_index + 1:], perm + sliced_string[symbol_index].lower())
                    dfs(sliced_string[symbol_index + 1:], perm + sliced_string[symbol_index].upper())
                else:
                    perm += sliced_string[symbol_index]
            if len(perm) == len_of_string:
                perms.append(perm)

        dfs(s, '')
        return perms if perms else [s]

    def letterCasePermutation(self, s):
        perms = []
        len_of_string = len(s)

        def dfs(idx, perm):
            if idx == len_of_string:
                perms.append(perm)
                return
            if s[idx].isalpha():
                dfs(idx + 1, perm + s[idx].lower())
                dfs(idx + 1, perm + s[idx].upper())
            else:
                dfs(idx + 1, perm + s[idx])
        dfs(0, '')
        return perms

print(Solution().letterCasePermutation("D14f00"))
