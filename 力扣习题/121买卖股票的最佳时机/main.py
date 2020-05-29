class Solution:
    '''
    动态规划
    '''
    def maxProfit(self, prices: List[int]) -> int:
        #length = len(prices)
        res = 0
        min_pri = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - prices[min_pri])
            if prices[i] < prices[min_pri]:
                min_pri = i
        return res
