class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        res = 0
        val = None
        for i in s:
            if c == 0:
                val = i
                c += 1
            elif val == i:
                c += 1
            else:
                c -= 1
                if c == 0:
                    res += 1
        return res

s1 = 'RLRRLLRLRL'
s2 = 'RLLLLRRRLR'
s3 = 'LLLLRRRR'
s4 = ''
s = Solution()

print(s.balancedStringSplit(s2))
print(s.balancedStringSplit(s3))
print(s.balancedStringSplit(s4))