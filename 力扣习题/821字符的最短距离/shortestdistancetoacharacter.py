from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = len(s)
        res = [float('inf')] * l
        last = float('inf')
        for i in range(l):
            if s[i] == c:
                res[i] = 0
                last = i
                j = i - 1
                while j >= 0 and s[j] != c:
                    res[j] = min(res[j], i - j)
                    j -= 1
            else:
                res[i] = abs(last - i)
        return res

    def shortestToChar2(self, s: str, c: str) -> List[int]:
        l = len(s)
        res = [float('inf')] * l
        last = float('inf')
        for i in range(l):
            if s[i] == c:
                res[i] = 0
                last = i
                j = i - 1
                while j >= 0 and i - j < res[j]:
                    res[j] = i - j
                    j -= 1
            else:
                res[i] = abs(last - i)
        return res
        
s = Solution()

print(s.shortestToChar('loveleetcode', 'e'))