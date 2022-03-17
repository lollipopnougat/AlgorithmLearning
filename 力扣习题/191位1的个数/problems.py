class Solution1:
    '''
    除2取余
    '''
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res

class Solution2:
    '''
    最低位
    '''
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

class Solution3:
    '''
    每轮去掉二进制中位置最靠后的1
    '''
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res


class Solution4:
    '''
    字符串法
    '''
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')

s = Solution4()

print(s.hammingWeight(5))
print(s.hammingWeight(16))
print(s.hammingWeight(15))