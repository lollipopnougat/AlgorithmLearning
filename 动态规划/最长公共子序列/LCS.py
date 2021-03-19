class value:
    array_b = None
    array_c = None

    def __init__(self, m, n):
        self.array_b = [[0 for i in range(n)] for j in range(m)]
        self.array_c = [[0 for i in range(n)] for j in range(m)]


def lcs_len(list_x, list_y) -> value:
    m = len(list_x)
    n = len(list_y)
    res = value(len(list_x), len(list_y))
    #res.array_c = [[0 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if list_x[i] == list_y[j]:
                res.array_c[i][j] = res.array_c[i - 1][j - 1] + 1
                res.array_b[i][j] = 1
            elif res.array_c[i - 1][j] >= res.array_c[i][j - 1]:
                res.array_c[i][j] = res.array_c[i - 1][j]
                res.array_b[i][j] = 2
            else:
                res.array_c[i][j] = res.array_c[i][j - 1]
                res.array_b[i][j] = 3
    return res

result = []

def lcs_r(i, j, list_x, res: value):
    if i == 0 or j == 0:
        return
    if res.array_b[i][j] == 1:
        lcs_r(i - 1, j - 1, list_x, res)
        #print(list_x[i])
        result.append(list_x[i])
    elif res.array_b[i][j] == 2:
        lcs_r(i - 1, j, list_x, res)
    else:
        lcs_r(i, j - 1, list_x, res)


def get_lcs(list_x, list_y):
    global result
    result = []
    list_x.insert(0, ' ')
    list_y.insert(0, ' ')
    m = len(list_x) - 1
    n = len(list_y) - 1
    tmp = lcs_len(list_x, list_y)
    lcs_r(m, n, list_x, tmp)
    list_x.pop(0)
    list_y.pop(0)
    print(result)


l1 = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
l2 = ['B', 'D', 'C', 'A', 'B', 'A']

get_lcs(l1, l2)
