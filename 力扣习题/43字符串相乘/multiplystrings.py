class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(n1:str, n2:str) -> str:
            (l, s) = (n2, n1) if len(n1) <= len(n2) else (n1, n2)
            i = 0
            l = l[::-1]
            s = s[::-1]
            res = ''
            c = 0
            while i < len(s):
                tmp = int(l[i]) + int(s[i]) + c
                res += str(tmp % 10)
                c = tmp // 10
                i += 1
            while i < len(l):
                tmp = int(l[i]) + c
                res += str(tmp % 10)
                c = tmp // 10
                i += 1
            if c != 0:
                res += str(c)
            return res[::-1]

        def simple_mul(st1: str, ch: str) -> str:
            res = ''
            c = 0
            chi = int(ch)
            st = st1[::-1]
            for i in st:
                tmp = int(i) * chi + c
                c = tmp // 10
                res += str(tmp % 10)
            if c != 0:
                res += str(c)
            return res[::-1]

        res = '0'         
        for i in range(len(num1)):
            res = add(res, simple_mul(num2, num1[i]) + '0' * (len(num1) - 1 - i))
        return res


s = Solution()

print(s.multiply('500','2'))

#rint(simple_mul('100','2'))