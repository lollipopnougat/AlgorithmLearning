class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[:1:-1]
        s += '0' * (32 - len(s))
        return int(s, 2)

class Solution2:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while n:
            res += (n % 2) * 2 ** (31 - count)
            count += 1
            n >>= 1
        return res

class Solution3:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 32
        while count:
            res <<= 1
            res += n & 1
            n >>= 1
            count -= 1
        return res

class Solution4:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n&1) << (31-i)
            n =  n >> 1
        return ans

s = Solution3()
i = 0b00000010100101000001111010011100
print(s.reverseBits(i))
print(s.reverseBits(0b1011))