class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        贪心
        '''
        mnc = mxc = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                mnc += 1
                mxc += 1
            elif s[i] == ')':
                mnc = max(mnc - 1, 0)
                mxc -= 1
                if mxc < 0:
                    return False
            else:
                mnc = max(mnc - 1, 0)
                mxc += 1
        return mnc == 0

    def checkValidStringdp(self, s: str) -> bool:
        n = len(s)
        dp = [([False] * n) for _ in range(n)]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
        for i in range(1, n):
            dp[i - 1][i] = (s[i - 1] == '(' or s[i - 1] == '*') and (s[i] == ')' or s[i] == '*')