class Solution:
    @staticmethod
    def scoreOfParentheses(s: str) -> int:
        stack = [0]
        i = 0
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                value = max(2 * stack.pop(), 1)
                stack[-1] += value
        return stack.pop()

print(Solution.scoreOfParentheses('(()(()))'))


