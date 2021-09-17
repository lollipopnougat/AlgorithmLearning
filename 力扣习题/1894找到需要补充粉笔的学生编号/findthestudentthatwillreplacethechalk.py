from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        le = len(chalk)
        i = 0
        su = sum(chalk)
        k -= su * (k // su)
        while k >= chalk[i]:
            k -= chalk[i]
            i = (i + 1) % le
        return i
            