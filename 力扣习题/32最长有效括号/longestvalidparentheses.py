class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        m = 0
        for i in s:
            if i == ')' and stack:
                res += 2
                stack.pop()
            elif i == '(':
                stack.append('(')
            elif i == ')':
                m = max(res, m)
                res = 0
        m = max(res, m)
        return m

s = Solution()

print(s.longestValidParentheses('()(()'))