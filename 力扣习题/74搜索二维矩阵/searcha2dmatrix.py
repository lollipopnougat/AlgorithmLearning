from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        h, w = len(matrix), len(matrix[0])
        i, j = 0, w - 1
        while i < h and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target == matrix[i][j]:
                return True
            else:
                j -= 1
        return False

class Solutionnn:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix[m - 1][n - 1] < target or matrix[0][0] > target:
            return False
        l = 0
        h = m - 1
        while l < h:
            m = (l + h) // 2
            if target == matrix[m][n - 1]:
                return True
            elif target > matrix[m][n - 1]:
                l = m + 1
            else:
                h = m - 1
        if matrix[h][n - 1] < target:
            h += 1
        if h < 0:
            h += 1
        rl = 0
        rh = n - 1
        while rl <= rh:
            m = (rl + rh) // 2
            if target == matrix[h][m]:
                return True
            elif target > matrix[h][m]:
                rl = m + 1
            else:
                rh = m - 1
        return False


s = Solutionnn()

print(s.searchMatrix([[1], [3]], 1))
print(
    s.searchMatrix(
        [[-8, -7, -5, -3, -3, -1, 1], [2, 2, 2, 3, 3, 5, 7],
         [8, 9, 11, 11, 13, 15, 17], [18, 18, 18, 20, 20, 20, 21],
         [23, 24, 26, 26, 26, 27, 27], [28, 29, 29, 30, 32, 32, 34]], -5))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 10))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(
    s.searchMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                    [17, 18, 19, 21, 27]], 18))
