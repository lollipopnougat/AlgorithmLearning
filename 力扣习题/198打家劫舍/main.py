class Solution:
    # 当前最大价值 = max(上一个最大的价值， 上一个最大的价值 + 现在的这个的价值) 
    def rob(self, nums: list) -> int:
        last, now = 0, 0
        for i in nums:
            #这是一个动态规划问题
            last, now = now, max(last + i, now)
            #注意 max中的last还是之前的last值
        return now
s = Solution()
s.rob([1,2,3,1])