class Matrix(list):
    def __init__(self, m: int, n: int) -> None:
        self.rows = m
        self.cols = n
        self.mat = [0] * m * n
        self.format = [self.mat[key * self.cols : (key + 1) * self.cols] for key in range(self.rows)]

    def __getitem__(self, key: int):
        if key >= self.rows:
            raise IndexError
        tmp = self.mat[key * self.cols : (key + 1) * self.cols]
        return tmp
    
    def __setitem__(self, key: int, val):
        for i in range(len(val)):
            self.mat[key * self.cols + i] = val[i]

    def __str__(self):
        return str(self.format)

m = Matrix(4, 3)

m[0][1] = 5

print(m)

