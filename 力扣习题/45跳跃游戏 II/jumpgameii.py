from typing import List

class Solution:
    # 贪心
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        far = st = end = 0
        for i in range(n - 1):
            if far > i:
                far = max(far, i + nums[i])
                if st == end:
                    end = far
                    st += 1
        return st


class Solutionm:
    def jump(self, nums: List[int]) -> int:
        m = {0:set()}
        for i, v in enumerate(nums):
            for j in range(1, v + 1):
                if j + v in m:
                    m[j + v].add(i)
                else:
                    m[j + v] = set()
        count = 0
        k = -1
        while True:
            if k == 0:
                break
            k = min(m[k])
            count += 1
        return count