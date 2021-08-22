class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        c = 0
        res = ''
        tmp = ''
        le = len(s)
        for i in range(le):
            c += 1
            if c == k:
                if i - c < 0:
                    res += s[i::-1]
                else:
                    res += s[i:i - c:-1]
            if c == 2 * k:
                res += s[i - c:i]
                c = 0
        if c < k:
            if le - c < 0:
                res += s[le - 1::-1]
            else:
                res += s[le - 1:le - c:-1]
        else:
            res += s[le - c:le]
        return res

s = Solution()
print(s.reverseStr("abcdefg",2))