from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
      res = [0] * (n + 1)
      for i in range(n + 1):
        if i % 2 == 0:
          res[i] = res[i // 2]
        else:
          res[i] = res[i - 1] + 1
      return res
