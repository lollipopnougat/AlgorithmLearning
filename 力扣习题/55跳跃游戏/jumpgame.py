'''
贪心，
每个位置都计算自己能达到的最远距离，
同时每个位置要判断自己是否可达，
也就是本位置需要在当前最远能到达的距离中。
最终计算出来能到达的最远距离，与数组长度比较即可
'''

class Solution:
    def canJump(self, nums: list) -> bool:
        can_reach = 0
        for i in range(len(nums)):
            if i > can_reach:
                return False
            can_reach = max(can_reach, i + nums[i])
        return True

class Solutionn:
    def canJump(self, nums: list, k: int) -> int:
        l = len(nums)
        dp = [float('inf')] * l
        dp[0] = 0
        for i in range(l - 1):
            v = i + nums[i]
            lm = min(v + 1, l)
            for j in range(1, lm):
                dp[j] = min(dp[j], dp[i] + 1)
        if dp[-1] <= k:
            return dp[-1]
        else:
            return -1

            
            
s = Solutionn()

print(s.canJump([2,3,1,1,4], 2))
print(s.canJump([2,1,5,6,2,3], 6))
print(s.canJump([2,0,1,0,3], 5))