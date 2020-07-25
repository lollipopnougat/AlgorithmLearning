class Solution:
    '''
    双指针(滑动窗口) 有动态规划思想
    '''
    def maxArea(self, height: List[int]) -> int:
        res, i = 0, 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                minH = height[i]
                i += 1
            else:
                minH = height[j]
                j -= 1
            res = max(res, (j - i + 1) * minH)
        return res