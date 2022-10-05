class Solution:
    def isFlipedStringb(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2:
            return False
        i = 0
        j = 0
        flag  = False
        fl = False
        while i < l1:
            if j == l2:
                if flag:
                    break
                j = 0
                flag = True
            if s1[i] == s2[j]:
                fl = True
                i += 1
                j += 1
            elif fl:
                i = 0
                j += 1
            else:
                j += 1
        return i == l1
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s3 = s2 + s2
        return s3.find(s1) != -1


s = Solution()

print(s.isFlipedString('abcd','acbd'))
print(s.isFlipedString('wsww','swww'))