from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        位运算
        '''
        res = 0
        n = len(words)
        tmp = [0] * n
        for i in range(n):
            for j in words[i]:
                val = 1
                tmp[i] |= (val << (ord(j) - 97))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if tmp[i] & tmp[j] == 0:
                    res = max(len(words[i]) * len(words[j]), res)
        return res


s = Solution()

print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
