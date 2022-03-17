class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = numerator / denominator
        if res - int(res) == 0:
            return str(int(res))
        fl = False
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            fl = True
        denominator = abs(denominator)
        numerator = abs(numerator)
        if fl:
            res = -res
        val = str(int(res))
        la = {}
        tmp = [val, '.']
        remains = numerator % denominator
        count = 0
        while not remains in la:
            count += 1
            la[remains] = count
            remains *= 10
            tt = remains // denominator
            tmp.append(str(tt))
            remains %= denominator
        if remains != 0:
            tmp.insert(la[remains] + 1, '(')
            tmp.append(')')
        else:
            tmp.pop()
        if fl:
            tmp.insert(0, '-')
        return ''.join(tmp)



s = Solution()
print(s.fractionToDecimal(-1, 2))
print(s.fractionToDecimal(-2147483648, 1))
print(s.fractionToDecimal(2147483647, 37))
print(s.fractionToDecimal(1, 214748364))
print(s.fractionToDecimal(1, 4))
print(s.fractionToDecimal(1, 8))
print(s.fractionToDecimal(-10, 3))
print(s.fractionToDecimal(-10, 5))
print(s.fractionToDecimal(-22, 7))
print(s.fractionToDecimal(-1, 6))
print(s.fractionToDecimal(1, 9))
print(s.fractionToDecimal(227, 53))
print(s.fractionToDecimal(71821, 99990))
