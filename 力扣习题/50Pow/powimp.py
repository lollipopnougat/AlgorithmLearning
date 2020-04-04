

class Solution0:
    def myPow(self, x: float, n: int) -> float:
        '''
        挺好的，就是会超时
        '''
        if n < 0:
            return 1 / self.myPow(x,-n)
        else:
            tmp = x
            x = 1
            for i in range(n):
                x *= tmp
            return x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        考虑快速幂算法
        '''
        if n < 0:
            return 1 / self.myPow(x,-n)
        else:
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                return self.myPow(x * x, n / 2)
            else:
                return self.myPow(x, n - 1) * x


s = Solution()
print(s.myPow(0.0001,2147483647))