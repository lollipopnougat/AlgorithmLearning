class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        h = len(board)
        w = len(board[0])

        def isMine(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or board[i][j] != 'M':
                return False
            return True

        def findMine(i, j):
            num = 0
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if isMine(i + k, j + l):
                        num += 1
            return num

        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or board[i][j] == 'B':
                return
            if board[i][j] == 'E':
                n = findMine(i, j)
                if n == 0:
                    board[i][j] = 'B'
                    dfs(i - 1, j - 1)
                    dfs(i - 1, j)
                    dfs(i - 1, j + 1)
                    dfs(i, j - 1)
                    dfs(i, j + 1)
                    dfs(i + 1, j - 1)
                    dfs(i + 1, j)
                    dfs(i + 1, j + 1)
                else:
                    board[i][j] = str(n)

        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        dfs(i, j)
        return board


s = Solution()
m = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
     ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
c = [3, 0]
m2 = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]

c2 = [0,0]

print(s.updateBoard(m2, c2))
