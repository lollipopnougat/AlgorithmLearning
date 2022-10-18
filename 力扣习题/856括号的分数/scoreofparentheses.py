class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        res = 0
        for i in s:
            if i == '(':
                stk.append(['(', 0])
            elif i == ')' and stk and stk[-1][0] == '(':
                t = stk.pop()
                if t[1] > 0:
                    if len(stk) == 0:
                        res += (t[1] * 2)
                    else:
                        stk[-1][1] += t[1] * 2
                else:
                    if len(stk) == 0:
                        res += 1
                    else:
                        stk[-1][1] += 1
        return res




s = Solution()

print(s.scoreOfParentheses('()'))
print(s.scoreOfParentheses('(())'))
print(s.scoreOfParentheses('()()'))
print(s.scoreOfParentheses('()()()'))
print(s.scoreOfParentheses('(()(()))'))
print(s.scoreOfParentheses('((())((()())))'))
print(s.scoreOfParentheses('(((((()(((())((()))))))(()))()))'))