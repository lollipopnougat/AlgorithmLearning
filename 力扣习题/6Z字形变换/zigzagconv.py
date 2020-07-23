class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = [''] * len(s)
        if len(s) == 0 or numRows < 1:
            return '';
        if numRows == 1:
            return s;
        for i,j in enumerate(s):
            ans = i // (numRows - 1)
            cur = i % (numRows - 1)
            if ans % 2:
                temp[numRows - cur - 1] += j;
            else:
                temp[cur] += j
        return ''.join(temp)