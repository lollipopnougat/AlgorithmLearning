class Solution:
    '''
    双指针
    '''
    def fourSum(self, nums: list, target: int) -> list:
        d = {}
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                d.setdefault(nums[i] + nums[j], []).append((i, j))
        result = set()
        for i in range(l):
            for j in range(i + 1, l):
                for a, b in d.get(target - nums[i] - nums[j], []):
                    temp = {i, j, a, b}
                    if len(temp) == 4:
                        result.add(tuple(sorted(nums[t] for t in temp)))
        return list(result)

class Solution2:
    '''
    官方题解
    '''
    def fourSum(self, nums: list, target: int) -> list:
        quadruplets = []
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

