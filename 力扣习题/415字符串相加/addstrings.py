class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        le1, le2 = len(num1), len(num2)
        if le1 > le2:
            res = list(num1[::-1])
            p = list(num2[::-1])
        else:
            res = list(num2[::-1])
            p = list(num1[::-1])
            le2, le1 = le1, le2
        i, c = 0, 0
        while(i < le1):
            if i < le2:
                tmp = int(res[i]) + int(p[i]) + c
            else:
                tmp = int(res[i]) + c
            res[i] = str(tmp % 10)
            c = tmp // 10
            i += 1
        if c!= 0:
            res += '1'
        res.reverse()
        return ''.join(res)

class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        res = ''
        while i >= 0 or j >= 0 or c:
            tmp = int(num1[i] if i >= 0 else 0) + int(num2[j] if j >= 0 else 0) + c
            res = str(tmp % 10) + res
            c = tmp // 10
            j -= 1
            i -= 1
        return res


                