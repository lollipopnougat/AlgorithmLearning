class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.h = len(board)
        if self.h == 0:
            return
        self.w = len(board[0])

        for i in range(self.h):
            self.dfs(board, i, 0)
            self.dfs(board, i, self.w - 1)
        for i in range(self.w):
            self.dfs(board, 0, i)
            self.dfs(board, self.h - 1, i)
        
        for i in range(self.h):
            for j in range(self.w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= self.h or j >= self.w or board[i][j] != 'O':
            return
        board[i][j] = 'S'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)

s = Solution()
li = [
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"],
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"]]
s.solve(li)
print(li)            



