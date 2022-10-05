from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        ss = set(wordDict)
        for i in range(1, n + 1):
            for j in range(i):
                t = s[j:i]
                if dp[j] and t in ss:
                    dp[i] = True
                    break
        return dp[n]


s = Solution()

print(s.wordBreak('leetcode', ['leet', 'code']))
