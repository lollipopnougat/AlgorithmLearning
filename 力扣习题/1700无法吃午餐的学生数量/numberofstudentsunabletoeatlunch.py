from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = [0, 0]
        for i in students:
            if i == 0:
                st[0] += 1
            else:
                st[1] += 1
        for i in sandwiches:
            if i == 0 and st[0] > 0:
                st[0] -= 1
            elif i == 1 and st[1] > 0:
                st[1] -= 1
            else:
                break
        return st[0] + st[1]
        
        


s = Solution()

print(s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
print(s.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
