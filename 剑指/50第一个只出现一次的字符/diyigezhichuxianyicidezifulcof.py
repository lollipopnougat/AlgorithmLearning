class Solution:
    def firstUniqChar(self, s: str) -> str:
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in m:
            if m[i] == 1:
                return i
        return ' '