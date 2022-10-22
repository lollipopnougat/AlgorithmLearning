class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        n = len(s)
        res = [s[0]]
        for i in range(1, n):
            if res and abs(ord(res[-1]) - ord(s[i])) == 32:
                res.pop()
            else:
                res.append(s[i])
        return ''.join(res)

s = Solution()

print(s.makeGood('abBAcC'))