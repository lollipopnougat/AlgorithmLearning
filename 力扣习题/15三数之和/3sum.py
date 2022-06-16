from typing import List

class Solutionm:
    # 击败9%(丢人，你给我退出码厂)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)
        if l < 3:
            return res
        for i in range(l - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m = {}
            for j in range(i + 1, l):
                t = -nums[i] - nums[j]
                if t in m:
                    ins = [nums[i], nums[j], t]
                    if not ins in res:
                        res.append(ins)
                m[nums[j]] = j
        return res

class Solutiond:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums.sort()
        for first in range(n - 2):
            if nums[first] > 0:
                return res
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            left = first + 1
            right = n - 1
            tar = -nums[first]
            while left < right:
                total = nums[left] + nums[right]
                if total == tar:
                    res.append([nums[first],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > tar:
                    right -= 1
                else:
                    left += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)
        if l < 3:
            return res
        for i in range(l - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m = {}
            for j in range(i + 1, l):
                t = -(nums[i] + nums[j])
                if t in m:
                    ins = [nums[i], t, nums[j]]
                    if not ins in res:
                        res.append(ins)
                m[nums[j]] = j
        return res

class Solutionrrr:
    '''
    260ms 卡密!
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeros, positives, negatives = 0, {}, {}
        for num in nums:
            if num == 0:
                zeros += 1
            elif num > 0:
                positives.setdefault(num, 0)
                positives[num] += 1
            else:
                negatives.setdefault(num, 0)
                negatives[num] += 1

        # 相加为0的三元组可能的组成形式：
        # 3个0，两个负数一个正数，两个正数一个负数，一正一负加一零
        results = []
        if zeros >= 3:
            results.append([0] * 3)
            
        if len(positives) != 0 and len(negatives) != 0:
            for pi in positives:
                count = positives[pi]
                if count >= 2 and (-2 * pi) in negatives:
                    results.append([pi] * 2 + [-2 * pi])
                if -pi in negatives and zeros > 0:
                    results.append([pi, -pi, 0])
                for pj in positives:
                    if pj <= pi:
                        continue
                    if -1 * (pi + pj) in negatives:
                        results.append([-1 * (pi + pj), pi, pj])
    
            for ni in negatives:
                count = negatives[ni]
                if count >= 2 and (-2 * ni) in positives:
                    results.append([ni] * 2 + [-2 * ni])
                for nj in negatives:
                    if nj <= ni:
                        continue
                    if -1 * (ni + nj) in positives:
                        results.append([-1 * (ni + nj), ni, nj])

        return results


s = Solution()

li = [-1,0,1,2,-1,-4]

print(s.threeSum(li))