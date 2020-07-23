class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


k = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

print(k.removeDuplicates(nums))
print(nums)
