class Solution:
    def removeElement(self, nums:  list, val: int) -> int:
        '''
        正规版
        '''
        l = len(nums) - 1
        i = 0
        while i <= l:
            if nums[i] == val:
                nums[i], nums[l] = nums[l], nums[i]
                l -= 1
            else:
                i += 1
        return l + 1
    
class Solution2:
    '''
    抖机灵版
    '''
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        


