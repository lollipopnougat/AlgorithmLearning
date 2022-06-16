class Solution:
    '''
    动态规划，LCS
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '^' + text1 
        text2 = '^' + text2 
        m, n = len(text1), len(text2)
        c = [([0] * n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])
        return c[m - 1][n - 1]


s = Solution()

print(s.longestCommonSubsequence("abcde", "ace"))
