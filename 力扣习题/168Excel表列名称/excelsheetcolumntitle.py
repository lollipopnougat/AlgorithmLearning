class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        tmp = []
        while columnNumber:
            columnNumber -= 1
            tmp.insert(0, columnNumber % 26)
            columnNumber //= 26
        return ''.join(map(lambda x: chr(x + 65), tmp))


class Solution2:
    def convertToTitle(self, columnNumber: int) -> str:
        s = []
        while columnNumber > 0:
            columnNumber -= 1
            s.append(chr((columnNumber % 26) + 65))
            columnNumber = columnNumber // 26
        s.reverse()
        str1 = "".join(s)
        return str1


s = Solution()

for i in range(1, 120):
    print(s.convertToTitle(i))
print(s.convertToTitle(701))
print(s.convertToTitle(2147483647))