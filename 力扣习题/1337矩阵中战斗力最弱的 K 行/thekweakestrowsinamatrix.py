from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        res = [(0,sum(mat[0]))]
        for i in range(1, n):
            tmp = sum(mat[i])
            j = 0
            while j < (le := len(res)) and tmp >= res[j][1]:
                j += 1
            res.insert(j,(i,tmp))
        return [res[i][0] for i in range(k)]
