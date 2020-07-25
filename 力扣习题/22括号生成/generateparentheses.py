class Solution:
    def generateParenthesis(self, n: int) -> list:
        res = []
        def gen(l: int, r: int, s: str):
            if l == 0 and r == 0:
                res.append(s)
                return;
            if l > 0:
                gen(l - 1, r, s + "(")
            if r > l:
                gen(l, r - 1, s + ")")
        gen(n, n, '')
        return res

s = Solution()

print(s.generateParenthesis(3))