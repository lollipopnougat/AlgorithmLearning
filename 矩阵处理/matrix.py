# matrix.py
''' 
Auth: lollipopnougat
Date: 2020.10.05
Encoding: UTF-8
'''
class matrix:
    # 构造矩阵对象 m: 行数 n: 列数
    def __init__(self, m: int, n: int) -> None:
        self.mat = [([0] * n) for _ in range(m)]
        self.rows = m
        self.cols = n

    # 从二维列表构建矩阵
    @staticmethod
    def from_list(array: list):
        row = len(array)
        col = len(array[0]) if array and isinstance(array[0], list) else 0
        if col == 0:
            col = row
            row = 1
            array = [array]
        t = matrix(m=row, n=col)
        t.mat = [i[:] for i in array]
        return t

    # 静态方法: 获取矩阵的转置
    @staticmethod
    def get_transpose(ma) -> list:
        tmp = matrix(m=ma.cols, n=ma.rows)
        for i in range(ma.cols):
            for j in range(ma.rows):
                tmp[i][j] = ma[j][i]
        return tmp

    # 静态方法: 判断是否是单位阵
    @staticmethod
    def is_identity(ma) -> bool:
        if ma.rows == ma.cols:
            for i in range(ma.rows):
                if ma.mat[i][i] != 1:
                    return False
            return True
        return False

    # 静态方法: 按行展开求行列式(递归)
    @staticmethod
    def __det_helper(li: list, n: int) -> int or float:
        if n == 1:
            return li[0][0]
        ans = 0
        tmp = [([0] * n) for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                for k in range(n - 1):
                    tmp[j][k] = li[j + 1][k + 1 if k >= i else k]
            t = matrix.__det_helper(tmp, n - 1)
            if i & 1:
                ans -= li[0][i] * t
            else:
                ans += li[0][i] * t
        return ans

    # 静态方法: 求矩阵对应行列式值
    @staticmethod
    def det_val(ma):
        if ma.rows != ma.cols:
            raise TypeError('matrix is not square')
        return matrix.__det_helper(ma.mat, ma.rows)

    # 静态方法: 求矩阵的伴随阵
    @staticmethod
    def get_adjugate(ma):
        if ma.rows != ma.cols:
            raise TypeError('matrix is not square')
        res = [([0] * ma.rows) for _ in range(ma.rows)]
        if ma.rows == 1:
            res[0][0] = 1
            return matrix.from_list(res)
        tmp = [([0] * ma.rows) for _ in range(ma.rows)]
        for i in range(ma.rows):
            for j in range(ma.rows):
                for k in range(ma.rows - 1):
                    for m in range(ma.rows - 1):
                        tmp[k][m] = ma.mat[k + 1 if k >= i else k][
                            m + 1 if m >= j else m]
                res[j][i] = matrix.__det_helper(tmp, ma.rows - 1)
                if (i + j) % 2 == 1:
                    res[j][i] = -res[j][i]
        return matrix.from_list(res)

    # 静态方法: 求矩阵的逆
    @staticmethod
    def get_inverse(ma):
        if ma.rows != ma.cols:
            raise TypeError('matrix is not square')
        flag = matrix.__det_helper(ma.mat, ma.rows)
        if flag == 0:
            raise TypeError("matrix's det result is zero")
        flag = 1 / flag
        tmp = matrix.get_adjugate(ma)
        return tmp * flag

    # 静态方法: 获取 n 阶单位阵
    @staticmethod
    def eye(n: int):
        tmp = matrix(n, n)
        for i in range(n):
            tmp.mat[i][i] = 1
        return tmp

    # 静态方法: 获取 n 阶0阵
    @staticmethod
    def zeros(n:int):
        tmp = matrix(n, n)
        return tmp
    
    # 静态方法: 获取 n 阶1阵
    @staticmethod
    def ones(n:int):
        tmp = matrix(n, n)
        for i in range(n):
            for j in range(n):
                tmp.mat[i][j] = 1
        return tmp

    # 静态方法: 获取矩阵的秩
    @staticmethod
    def get_rank(ma):
        t = ma.copy()
        i = j = 0
        m, n = t.rows - 1, t.cols - 1
        while i < m and j < n:
            r = i
            for k in range(i, m):
                if t[k][j]:
                    r = k
                    break
            if t[r][j]:
                if r != i:
                    t[r], t[i] = t[i], t[r]
                for u in range(i + 1, m):
                    if t[u][j]:
                        for k in range(i, n + 1):
                            t[u][k] ^= t[i][k]
                i += 1
            j += 1
        return i

    # 获取元素
    def __getitem__(self, key: int) -> list:
        return self.mat[key]

    # 设置元素
    def __setitem__(self, key: int, val: list):
        self.mat[key] = val

    # 直接对矩阵对象进行转置 需要是方阵
    def transposed(self):
        if self.rows != self.cols:
            raise TypeError('matrix is not square')
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                self.mat[i][j], self.mat[j][i] = self.mat[j][i], self.mat[i][j]

    # 矩阵转列表(深拷贝)
    def to_list(self):
        return [i[:] for i in self.mat]

    # 实现 print()
    def __str__(self) -> str:
        st = '['
        for i, v in enumerate(self.mat):
            st += str(v) + (',\n' if i != self.rows - 1 else ']')
        return st

    # 深拷贝矩阵对象
    def copy(self):
        return matrix.from_list(self.mat)

    # 重载 + 运算符
    def __add__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise TypeError("matrix's size is not fit")
        tmp = self.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                tmp[i][j] += other[i][j]
        return tmp

    # 实现 len()
    def __len__(self):
        return self.rows * self.cols

    # 重载 * 运算符(右乘)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return matrix.from_list([[i * other for i in j] for j in self.mat])
        else:
            if self.cols != other.rows:
                raise TypeError("matrix's size is not fit")
            tmp = matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        tmp[i][j] += self.mat[i][k] * other[k][j]
            return tmp

    # 重载 * 运算符(左乘)
    def __rmul__(self, other: int or float):
        return matrix.from_list([[i * other for i in j] for j in self.mat])

    # 重载 - 运算符
    def __sub__(self, other):
        return self.__add__(other * -1)

    # 重载 / 运算符
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return matrix.from_list([[i / other for i in j] for j in self.mat])
        else:
            return self.__mul__(matrix.get_inverse(other))

    # 重载 / 运算符(左除？)
    def __rtruediv__(self, other: int or float):
        return matrix.from_list([[i / other for i in j] for j in self.mat])

    # 重载 == 运算符
    def __eq__(self, other) -> bool:
        return self.to_list() == other.to_list()

    # 重载 != 运算符
    def __ne__(self, other) -> bool:
        return self.to_list() != other.to_list()

    # 重载 ~ 运算符(逆矩阵)
    def __invert__(self):
        return matrix.get_inverse(self)

    # 重载 in 成员操作符
    def __contains__(self, key) -> bool:
        for i in self.mat:
            if key in i:
                return True
        return False


if __name__ == "__main__":
    li1 = [[1, 2, 3], [4, 0, 6], [1, 1, 2]]
    li2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    li4 = [1, 2, 3, 4]
    li5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m1 = matrix.from_list(li1)
    m2 = matrix.from_list(li2)
    m3 = matrix.eye(3)
    m4 = matrix.from_list(li4)
    m5 = matrix.get_inverse(m1)
    m6 = matrix.from_list(li5)
    #print(m1 * m2)
    #print(len(m1))
    # print('')
    # print(m4)
    # print('')
    #print(matrix.get_transpose(m4))
    #print('')
    # m2.transposed()
    # print(m1 * m5)
    # print('')
    print(matrix.get_rank(m6))
    print(m2 == m3)
    print(~m1)
    #print(matrix.is_identity(m2))
    print('')
    s = m1.copy()
    print(matrix.det_val(m2))

    input('press anykey to exit...')
