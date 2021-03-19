from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])
        vis = [([True] * w) for _ in range(h)]
        flag = 0
        i = j = 0
        res = []
        while flag <= min(w, h) / 2:
            while j < w - 1 - flag and vis[i][j]:
                res.append(matrix[i][j])
                vis[i][j] = False
                j += 1
            while i < h - 1 - flag and vis[i][j]:
                res.append(matrix[i][j])
                vis[i][j] = False
                i += 1
            while j > 0 + flag and vis[i][j]:
                res.append(matrix[i][j])
                vis[i][j] = False
                j -= 1
            flag += 1
            while i > 0 + flag and vis[i][j]:
                res.append(matrix[i][j])
                vis[i][j] = False
                i -= 1
        if vis[i][j]:
            res.append(matrix[i][j])
        return res

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        # 取首行，去除首行后，对矩阵翻转来创建新的矩阵，
        # 再递归直到新矩阵为[],退出并将取到的数据返回
        ret = []
        if matrix == []:
            return ret
        ret.extend(matrix[0]) # 上侧
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return ret
        r = self.spiralOrder2([i for i in zip(*new)])
        ret.extend(r)
        return ret

s = Solution()

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
m4 = [[1]]
m5 = [[1,2],[3,4]]
m6 = [[1,2,3]]
print(s.spiralOrder(m3))
print(s.spiralOrder(m6))