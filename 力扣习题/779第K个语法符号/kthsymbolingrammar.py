from functools import lru_cache

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.helper(k)
        
    @lru_cache()
    def helper(self, n: int):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n % 2 == 0:
            return 1 - self.helper(n - 1)
        else:
            return self.helper(n // 2 + 1)


s = Solution()

print(s.kthGrammar(4, 6))
