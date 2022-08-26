from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def backtrack(start, comb):
            if len(comb) == k:
                result.append(comb)
                return
            for num in range(start, n + 1):
                backtrack(num + 1, comb + [num])
        backtrack(1, [])
        return result

    def combine_iter(self, n, k):
        return [list(comb) for comb in combinations(range(1, n + 1), k)]


print(Solution().combine(4, 2))
print(Solution().combine_iter(4, 2))