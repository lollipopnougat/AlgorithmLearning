# 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        v = x ^ y
        return bin(v).count('1')

class Solutionn:
    def hammingDistance(self, x: int, y: int) -> int:
        v = x ^ y
        res = 0
        while v:
            res += v & 1
            v >>= 1
        return res