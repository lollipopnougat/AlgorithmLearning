class Solution:
    def isPalindrome(self, s: str) -> bool:

        tmp = ''.join(e for e in s if e.isalnum())
        if tmp == '':
            return True
        tmp = tmp.lower()
        print(tmp)
        le = len(tmp)
        i = 0
        flag = False
        while tmp[i] == tmp[le - i - 1]:
            if i == le // 2:
                flag = True
                break
            i += 1
        return flag


# 大佬的代码
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(s.split(' '))
        a = a.lower()
        b = [i for i in a if i.isalnum()]
        # print(b)
        return b == b[::-1]


# 启发
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        b = ''.join(e for e in s.lower() if e.isalnum())
        return b == b[::-1]


# 越发变态...
class Solution4:
    def isPalindrome(self, s: str) -> bool:
        # s = list(filter(str.isalnum, s.lower()))
        # return True if s == s[::-1] else False
        s = [*filter(str.isalnum, s.lower())]
        return True if s == s[::-1] else False


s = Solution3()

print(s.isPalindrome("A man, a plan, a canal: Panama"))

print(s.isPalindrome(" "))
