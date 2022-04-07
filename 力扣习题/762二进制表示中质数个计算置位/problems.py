class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        temp = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0
        for i in range(left, right + 1):
            if bin(i).count('1') in temp:
                res += 1
        return res