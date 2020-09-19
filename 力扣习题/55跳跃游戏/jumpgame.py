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