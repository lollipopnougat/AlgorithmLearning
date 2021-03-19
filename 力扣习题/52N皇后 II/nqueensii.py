class Solution:
    '''
    真大佬
    '''
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.count = 0
        self.dfs(0, 0, 0, 0)
        return self.count

    def dfs(self, row, cols, pie, na):
        if row >= self.n:
            self.count += 1  # 解法加1
            return
        # cols | pie | na，列、撇、捺 方向 所有已经被占的位置 标为1
        # 取反后 所有可用的位置标为 1,但cols、pie、na 都是 32位，取反后 高位的 0 都变成了 1
        # 而我们只想保留 低8位，想把高位都置为0, ((1<<n) - 1) 表示先把1左移8位——> 100000000
        # 再减1，则变成了 011111111，再做与运算，即可保留低八位，去除高位
        bits = (~(cols | pie | na)) & ((1 << self.n) - 1)  # 得到当前行 可放置皇后的格子

        while bits:  # bits中还包含1
            p = bits & -bits  # 取到最低位的1，即从当前行可用的格子中取出最右边 为1 的格子
            bits = bits & (bits - 1)  # 将当前行最右边的 1置为0，表示在P位置上放上皇后
            # (pie | p) << 1 ，左斜线往下一行的格子延展时，相当于左移一位
            self.dfs(row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)

    
# 抖机灵算法

class Solutiont:
    def totalNQueens(self, n: int) -> int:
        return [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712][n]


class Solutiono:
    '''
    八皇后1
    '''
    num = 0
    chess = None
    res = []
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.chess = [[0] * n for i in range(n)]
        self.num = n
        self.cal_row(self.chess, 0)
        return self.res


        
    def cal_row(self, ch: list, row: int):
        if row == self.num:
            tmp = []
            for i in range(self.num):
                str_tmp = ''
                for j in range(self.num):
                    if ch[i][j] == 1:
                       str_tmp += 'Q'
                    else:
                        str_tmp += '.'
                tmp.append(str_tmp)
            self.res += 1
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
    
s = Solution()

print(s.totalNQueens(8))