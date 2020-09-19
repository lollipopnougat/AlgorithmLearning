class matrix:
    def __init__(self, m: int, n: int) -> None:
        self.mat = [([0] * n) for _ in range(m)]
        self.rows = m
        self.cols = n

    @staticmethod
    def bylist(array: list):
        row = len(array)
        col = len(array[0]) if array else 0
        t = matrix(m=row, n=col)
        t.mat = [i[:] for i in array]
        return t

    def __getitem__(self, key: int):
        return self.mat[key]

    @staticmethod
    def get_transpose(ma) -> list:
        tmp = matrix(m=ma.cols, n=ma.rows)
        for i in range(ma.cols):
            for j in range(ma.rows):
                tmp[i][j] = ma[j][i]
        return tmp

    def show(self):
        print(self.mat)
    



li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m = matrix.bylist(li)

m.show()

matrix.get_transpose(m).show()
