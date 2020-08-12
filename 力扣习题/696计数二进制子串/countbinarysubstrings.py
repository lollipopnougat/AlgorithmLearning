class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        it = iter(s)
        last = next(it)
        count = 1
        res = []
        for i in it:
            if i == last:
                count += 1
            else:
                res.append(count)
                count = 1
                last = i
        res.append(count)
        length = len(res)
        result = 0
        for i in range(length - 1):
            result += min(res[i], res[i + 1])
        return result


s = Solution()
print(s.countBinarySubstrings("000111000"))