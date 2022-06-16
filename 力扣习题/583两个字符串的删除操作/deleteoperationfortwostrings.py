class Solution:
    '''
    与 1143 题一样
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        t1 = '^' + word1 
        t2 = '^' + word2
        m, n = len(t1), len(t2)
        c = [([0] * n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if t1[i] == t2[j]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])
        return n + m - 2 - 2 * c[m - 1][n - 1]
        