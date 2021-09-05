from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 差分数组
        tmp = [0] * (n + 1)
        res = [0] * n
        for st,ed,count in bookings:
            tmp[st - 1] += count
            tmp[ed] -= count
        l = 0
        for i in range(n):
            l += tmp[i]
            res[i] = l 
        return res

s = Solution()

li = [[1,2,10],[2,3,20],[2,5,25],[3,5,7]]

print(s.corpFlightBookings(li, 5))
