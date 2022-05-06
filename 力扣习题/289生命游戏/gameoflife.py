from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.view = [i[:] for i in board]
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                live = self.view[i][j]
                lives = 0
                for p in [-1, 0, 1]:
                    for q in [-1, 0, 1]:
                        if p == 0 and q == 0:
                            continue
                        lives += self.helper(i + p, j + q)
                if live == 1 and (lives < 2 or lives > 3):
                    board[i][j] = 0
                elif live == 0 and (lives == 3):
                    board[i][j] = 1
    def helper(self, i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return 0
        else:
            return self.view[i][j]
                
s = Solution()
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(b)
b2 = [[1,1],[1,0]]
s.gameOfLife(b2)
print(b)
print(b2)