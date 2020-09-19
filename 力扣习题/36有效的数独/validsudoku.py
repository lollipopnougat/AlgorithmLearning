class Solution:
    def isValidSudoku(self, board: list) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    st = board[i][j]
                    for k in range(j + 1, 9):
                        if st == board[i][k]:
                            return False
                    for k in range(i + 1, 9):
                        if st == board[k][j]:
                            return False
                    c = 0
                    for p in range(3):
                        for q in range(3):
                            tmp = board[p + 3 * (i // 3)][q + 3 * (j // 3)]
                            if st == tmp:
                                c += 1
                    if c != 1 and c != 0:
                        return False
        return True


class Solution2:
    def isValidSudoku(self, board: list) -> bool:
        matrix_line = [set() for i in range(9)]
        matrix_column = [set() for i in range(9)]
        matrix_area = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                pos = (i // 3) * 3 + j // 3
                if item != '.':
                    if item not in matrix_line[i] and item not in matrix_column[
                            j] and item not in matrix_area[pos]:
                        matrix_line[i].add(item)
                        matrix_column[j].add(item)
                        matrix_area[pos].add(item)
                    else:
                        return False
        return True


li = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()

print(s.isValidSudoku(li))
