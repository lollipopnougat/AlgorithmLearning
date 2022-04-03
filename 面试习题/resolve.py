from typing import List
class Solution:
    def solve(self, s: str, tags: List[int]) -> List[List[int]]:
        i = 0
        l = len(s)
        res = []
        m = {}
        while i < l:
            tag = int(s[i: i + 2], 16)
            tag_len = int(s[i + 2: i + 4], 16)
            tag_offset = i // 2 + 2
            m[tag] = [tag_len, tag_offset]
            i += 4 + tag_len * 2
        for i in tags:
            if i in m:
                res.append(m[i])
        return res

s = Solution()

print(s.solve('0F04ABABABAB', [15]))

        
