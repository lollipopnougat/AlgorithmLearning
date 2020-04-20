class Solution:
    '''
    思路：通过一个检查函数把一个岛全部标记成其他值 算法：深搜
    '''
    def numIslands(self, grid: list) -> int:
        h_l = len(grid)
        if h_l == 0:
            return 0
        l_l = len(grid[0])
        def check(i:int, j:int):
            if i < 0 or i >= h_l or j < 0 or j >= l_l or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            check(i + 1, j)
            check(i - 1, j)
            check(i, j + 1)
            check(i, j - 1)
        num = 0
        for i in range(h_l):
            
            for j in range(l_l):
                if grid[i][j] == '1':
                    check(i, j)
                    num+=1
        return num

s = Solution()

li = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
print(s.numIslands(li))