from typing import List


class Solution:
    def findNumberIn2DArrayn(self, matrix: List[List[int]],
                            target: int) -> bool:
        '''
        每行预处理 再二分
        '''
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        for ar in matrix:
            if ar[0] > target or ar[-1] < target:
                continue
            else:
                l = 0
                r = n - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target == ar[mid]:
                        return True
                    elif target > ar[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
        return False

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
        站在右上角看。这个矩阵其实就像是一个Binary Search Tree
        从右上角开始走，利用这个顺序关系可以在O(m+n)的复杂度下解决这个题：

        如果当前位置元素比target小，则row++
        如果当前位置元素比target大，则col--
        如果相等，返回true
        如果越界了还没找到，说明不存在，返回false
        '''
        if not matrix or not matrix[0]:
            return False
        w, h = len(matrix[0]), len(matrix)
        i, j = 0, w - 1
        while  i < h and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


s = Solution()

li = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
li2 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
       [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
print(s.findNumberIn2DArray(li, 5))
print(s.findNumberIn2DArray(li, 2))
print(s.findNumberIn2DArray(li, 0))
print(s.findNumberIn2DArray(li, 60))
print(s.findNumberIn2DArray(li2, 20))
