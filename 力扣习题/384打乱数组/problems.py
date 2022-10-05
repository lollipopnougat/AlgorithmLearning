import random
from typing import List

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.len = len(nums)


    def reset(self) -> List[int]:
        return self.ori


    def shuffle(self) -> List[int]:
        tmp = self.ori[:]
        for i in range(self.len):
            t = random.randint(0, i)
            tmp[t], tmp[i] = tmp[i], tmp[t]
        return tmp

        



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()