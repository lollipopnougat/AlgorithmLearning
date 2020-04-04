class Solution:
    num = 0
    chess = None
    res = []

    def cal_row(self, ch: list, row: int):
        if row == self.num:
            tmp = []
            for i in range(self.num):
                str_tmp = ''.join('Q' if ch[i][j] == 1 else '.' for j in range(self.num))
                tmp.append(str_tmp)
            self.res.append(tmp)
            return
        chess_tmp = ch
        for i in range(self.num):
            for j in range(self.num):
                chess_tmp[row][j] = 0
            chess_tmp[row][i] = 1
            if self.is_ok(chess_tmp, row, i):
                self.cal_row(chess_tmp, row + 1)

    def is_ok(self, ch: list, row: int, col: int):
        step = 1
        while row - step >= 0:
            if ch[row - step][col] == 1:
                return False
            if col - step >= 0 and ch[row - step][col - step] == 1:
                return False
            if col + step < self.num and ch[row - step][col + step] == 1:
                return False
            step += 1
        return True

    def solveNQueens(self, n: int):
        self.res = []
        self.chess = [[0] * n for i in range(n)]
        self.num = n
        self.cal_row(self.chess, 0)
        return self.res


s = Solution()

print(s.solveNQueens(8))