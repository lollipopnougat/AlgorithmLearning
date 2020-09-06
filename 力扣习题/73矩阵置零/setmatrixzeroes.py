class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix[0])
        h = len(matrix)
        lw = set()
        lh = set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    lw.add(j)
                    lh.add(i)
        for i in lw:
            for j in range(h):
                matrix[j][i] = 0
        for i in lh:
            for j in range(w):
                matrix[i][j] = 0


l = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

s = Solution()

s.setZeroes(l)

print(l)