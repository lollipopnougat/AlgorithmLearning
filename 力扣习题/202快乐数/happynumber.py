class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        st = str(n)
        res = 0
        while res != 1:
            res = 0
            for i in st:
                res += int(i) ** 2
            if(res in s):
                return False
            s.add(res)
            st = str(res)
        return True

class Solutionn:
    def isHappy(self, n: int) -> bool:
        s = set()
        st = n
        res = 0
        while res != 1:
            res = 0
            while st > 9:
                res += (st % 10) ** 2
                st //= 10
            res += st ** 2
            if(res in s):
                return False
            s.add(res)
            st = res
        return True

s1 = Solutionn()
s2 = Solution()

print(s1.isHappy(13))
print(s2.isHappy(13))
print(s1.isHappy(19))
print(s2.isHappy(19))
print(s1.isHappy(2))
print(s2.isHappy(2))