class Solution:
    def sumNums(self, n: int) -> int:
        '''
        and 短路
        '''
        return n and (n + self.sumNums(n - 1))

s = Solution()

print(s.sumNums(9))