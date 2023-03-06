class Solution:
    def printBin(self, num: float) -> str:
        res = ['0', '.']
        k = 0.5
        while len(res) < 32:
            if num - k > 0:
                num -= k
                k *= 0.5
                res.append('1')
            elif num - k == 0:
                num -= k
                res.append('1')
                break
            else:
                res.append('0')
                k *= 0.5
        return 'ERROR' if num != 0 else ''.join(res)