# 回溯
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(x, y, s):
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True

        def bt(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            if board[x][y] != '.':
                return bt(cur + 1)
            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):
                    board[x][y] = s
                    if bt(cur + 1):
                        return True
                    board[x][y] = '.'
            return False

        bt(0)


li = [["4", ".", ".", ".", "3", ".", "7", ".", "8"],
      [".", ".", ".", ".", "6", "4", "9", ".", "."],
      ["2", "1", ".", ".", "9", ".", ".", ".", "."],
      [".", "7", ".", "4", "5", "6", ".", ".", "."],
      ["6", "2", "9", "3", "7", "1", "8", "5", "4"],
      [".", ".", ".", "9", "2", "8", ".", "6", "."],
      [".", ".", ".", ".", "1", ".", ".", "8", "5"],
      [".", ".", "2", "6", "4", ".", ".", ".", "."],
      ["1", ".", "7", ".", "8", ".", ".", ".", "3"]]

s = Solution()

s.solveSudoku(li)

print(li)