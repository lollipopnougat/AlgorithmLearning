class Solution:
    def fib(self, n: int) -> int:
        a = 0
        x = 1
        if n == 0:
            return a
        for i in range(n - 1):
            x, a = x + a, x
        return x % 1000000007

s = Solution()

print(s.fib(10))