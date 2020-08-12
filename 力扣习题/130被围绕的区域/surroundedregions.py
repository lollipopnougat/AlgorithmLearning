class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        if h == 0:
            return
        w = len(board[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= h or j >= w or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            

        for i in range(h):
            dfs(i, 0)
            dfs(i, w - 1)
        for i in range(w):
            dfs(0, i)
            dfs(h - 1, i)
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'

s = Solution()
li = [
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"],
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"]]
s.solve(li)
print(li)            



