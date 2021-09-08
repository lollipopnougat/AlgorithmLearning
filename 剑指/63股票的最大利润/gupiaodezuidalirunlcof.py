from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        在遍历数组的过程中，维护一个最小值，最小值初试为prices[0]
        如果prices[i]大于min，则去更新一下利润res
        否则说明当前的prices[i]比min还小，则更新min
        '''
        le = len(prices)
        if le <= 1:
            return 0
        dp, m = 0, prices[0]
        for i in range(le):
            if prices[i] < m:
                m = prices[i]
            else:
                dp = max(dp, prices[i] - m)
        return dp