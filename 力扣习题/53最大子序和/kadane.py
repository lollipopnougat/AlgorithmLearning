
'''
Kadane算法扫描一次整个数列的所有数值，
在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。
该子数列由两部分组成：以前一个位置为结束点的最大子数列、该位置的数值。
因为该算法用到了“最佳子结构”（以每个位置为终点的最大子数列都是基于其前一位置的最大子数列计算得出），
该算法可看成动态规划的一个例子。
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)