class Solutionde:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        l = len(s)
        if l == 1:
            return 1
        if l == 2:
            if s[0] == '0':
                return 0
            tmp = int(s)
            if  tmp <= 26 and tmp != 10 and tmp != 20:
                return 2
            else:
                return 1
        else:
            af = self.numDecodings(s[1:])
            pr = self.numDecodings(s[:-1]) if s[-1] != '0' else 0
            if af > 0 and pr > 0 and l == 3:
                return af + pr - 1
            else:
                return af + pr


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        l = len(s)
        if l == 1:
            return 1
        dp = [0] * (l + 1)
        dp[0] = 1
        for i in range(l):
            dp[i + 1] = 0 if s[i] == '0' else dp[i]
            if i > 0 and (s[i-1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                dp[i + 1] += dp[i - 1]
        return dp[-1]
        
s = Solution()

print(s.numDecodings('2101'))