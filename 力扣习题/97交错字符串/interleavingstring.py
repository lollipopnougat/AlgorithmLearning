from functools import lru_cache


class Solution:
    '''
    超时
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        t1 = False
        if (s1 == s3 and s2 == '') or (s2 == s3 and s1 == ''):
            return True
        if s1 and s3 and s1[0] == s3[0]:
            t1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2 and s3 and s2[0] == s3[0]:
            t1 = t1 or self.isInterleave(s1, s2[1:], s3[1:])
        return t1


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dp(i, j, k):  #dp(i,j,k)返回s1[0...i]与s2[0...j]是否能交叉组成s3[0...k]
            if k == j == i == -1: return True  #baselie,匹配成功
            if i == -2 or j == -2 or k == -2: return False  #边界条件
            flag = False
            if s1[i] == s3[k] and s2[j] == s3[k]:  #s1、s2尾部都与s3相同，选择s1或者s2
                flag = dp(i - 1, j, k - 1) or dp(i, j - 1, k - 1) or flag
            elif s1[i] == s3[k]:  #s1、s3尾部相同
                flag = dp(i - 1, j, k - 1) or flag
            elif s2[j] == s3[k]:  #s2、s3尾部相同
                flag = dp(i, j - 1, k - 1) or flag
            else:
                return False  #s3与s1、s2尾部都不相同
            return flag

        if len(s1) + len(s2) != len(s3): return False  #s3的长度必须等于s1+s2
        if not s1 or not s2:  #s1、s2其中一个为空，那么s3必须与s1与s2的其中一个相等
            if s1 == s3 or s2 == s3: return True
            return False
        return dp(len(s1) - 1, len(s2) - 1, len(s3) - 1)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s = Solution()

print(s.isInterleave(s1, s2, s3))

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

print(s.isInterleave(s1, s2, s3))

s1 = ""
s2 = ""
s3 = ""

print(s.isInterleave(s1, s2, s3))

s1 = "abbcc"
s2 = "xyz"
s3 = "xabbzyz"

print(s.isInterleave(s1, s2, s3))

s1 = "a"
s2 = "b"
s3 = "a"

print(s.isInterleave(s1, s2, s3))