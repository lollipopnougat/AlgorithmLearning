from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(board[0])
        h = len(board)
        le = len(word)
        vis = [([False] * w) for _ in range(h)]
        def dfs(i, j, ind):
            if ind == le - 1:
                return board[i][j] == word[le - 1]
            vis[i][j] = True
            for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= k < h and 0 <= l < w and not vis[k][l] and board[k][l] == word[ind + 1]:
                    if dfs(k, l, ind + 1):
                        return True
            vis[i][j] = False
            return False
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False

class Solutiontql:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dps(x, y, pos):
            global find
            if visited[x][y] or find or board[x][y] != word[pos]:
                return 
            visited[x][y] = True
            if pos == len(word)-1:
                find = True
                return 
            for k in range(4):
                nx = x + direction[k]
                ny = y + direction[k+1]
                if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                    dps(nx, ny, pos+1)
            visited[x][y] = False
        direction = [-1, 0, 1, 0, -1]
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        global find
        find = False
        dic_board, dic_word = {}, {}
        start = []
        for i in range(m):
            for j in range(n):
                dic_board[board[i][j]] = dic_board.get(board[i][j], 0) + 1
                if board[i][j] == word[0]:
                    start.append([i,j])
        for i in range(len(word)):
            dic_word[word[i]] = dic_word.get(word[i], 0) + 1
        for i in dic_word:
            if dic_word[i] > dic_board.get(i, 0):
                return False
        for loc in start:
            dps(loc[0], loc[1], 0)
            if find:
                return True
        return False

class Solutionnr:
    # 非递归
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        dic_board = {}
        dic_word = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                dic_board[board[i][j]] = dic_board.get(board[i][j], 0) + 1
                if word[0] == board[i][j]:
                    start.append([i, j])
        for i in word:
            dic_word[i] = dic_word.get(i, 0) + 1
        for i in dic_word:
            if dic_board.get(i, 0) < dic_word[i]:
                return False
        for loc in start:
            passed = [[] for i in range(len(word))]
            current = loc
            path = []
            letter = 0
            while letter < len(word):
                i = current[0]
                j = current[1]
                if board[i][j] == word[letter]:
                    if current not in path:
                        path.append(current)
                        #passed[letter] = []
                        if letter >= len(word) - 1:
                            return True
                    letter += 1
                    #print(letter)
                    if (i > 0) & ([i - 1, j] not in passed[letter]) & ([i - 1, j] not in path):
                        current = [i - 1, j]
                    elif (i < len(board) - 1) & ([i + 1, j] not in passed[letter]) & ([i + 1, j] not in path):
                        current = [i + 1, j]
                    elif (j > 0) & ([i, j - 1] not in passed[letter]) & ([i, j - 1] not in path):
                        current = [i, j - 1]
                    elif (j < len(board[i]) - 1) & ([i, j + 1] not in passed[letter]) & ([i, j + 1] not in path):
                        current = [i, j + 1]
                    else:
                        path.pop()
                        passed[letter] = []
                        letter -= 1   
                        if  letter <= 0:
                            break
                        passed[letter].append(current)
                        letter -= 1
                        current = path[-1]
                else:
                    passed[letter].append(current)
                    current = path[-1]
                    letter -= 1
        return False



