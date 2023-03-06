from typing import List
#        右移     下移     左移     上移
dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def draw(n: int) -> List[str]:
    # 填充n*n为.
    res = [(['.'] * n) for _ in range(n)]
    i = j = 0
    v = n - 1
    k = 0
    while k < n:
        d = dire[k % 4]
        for _ in range(v):#循环v次
            res[i][j] = '0'
            i += d[0]
            j += d[1]
        k += 1
        v = n - (k if k % 2 == 1 else k - 1) # 如果k是奇数就 v = n - k 如果是偶数 v = n - k + 1
    res[i][j] = '0'
    return res


res = draw(5)
print(res)