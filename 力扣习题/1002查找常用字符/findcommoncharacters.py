from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        s = [set(i) for i in A]
        l = len(A)
        m = [{} for _ in range(l)]
        aset = s[0]
        for i in range(1, l):
            aset &= s[i]
        for i in range(l):
            for j in A[i]:
                m[i][j] = m[i].get(j, 0) + 1
        res = []
        for i in aset:
            t = float('inf')
            for j in m:
                if j[i] < t:
                    t = j[i]
            while t > 0:
                res.append(i)
                t -= 1
        return res


class Solutionm:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += minnum * k
        return res


s = Solution()
li = ["bella", "label", "roller"]
print(s.commonChars(li))