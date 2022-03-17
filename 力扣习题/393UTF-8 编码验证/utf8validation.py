from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        flag = 0
        l = len(data)
        for i in range(l):
            if flag == 0:
                if data[i] >> 7 == 0:
                    flag = 0
                elif data[i] >> 5 == 6:
                    flag = 1
                elif data[i] >> 4 == 14:
                    flag = 2
                elif data[i] >> 3 == 30:
                    flag = 3
                else:
                    return False
            else:
                if data[i] >> 6 != 2:
                    return False
                flag -= 1
        return flag == 0




s = Solution()

print(s.validUtf8([255]))
print(s.validUtf8([192, 130, 1]))
print(s.validUtf8([235, 140, 4]))
