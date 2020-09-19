import copy
class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        h = len(image)
        w = len(image[0])
        vmap = {}
        tmp = image[sr][sc]
        res = copy.deepcopy(image)
        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= h or j >= w or res[i][j] != tmp or (i, j) in vmap.keys():
                return
            vmap[(i, j)] = True
            res[i][j] = newColor
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        dfs(sr, sc)
        return res


class Solution2:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        self.nc = newColor
        self.h, self.w = len(image), len(image[0])
        self.vmap = {}
        self.tmp = image[sr][sc]
        self.res = [i[:] for i in image]
        self.dfs(sr, sc)
        return self.res

    def dfs(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.h or j >= self.w or self.res[i][j] != self.tmp or (i, j) in self.vmap.keys():
            return
        self.vmap[(i, j)] = True
        self.res[i][j] = self.nc
        self.dfs(i, j + 1)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i - 1, j)
s = Solution()
li = [[0,0,0],[0,1,1]]
print(s.floodFill(li, 1, 1, 1))

