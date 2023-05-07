from typing import List
n = 3
dat = [(2, 6), (1, 3), (5, 7)]

def getMergeIntsMax(ints: List[List[int]]) -> List[int]:
    # ints.sort(key=lambda x: x[0])
    qu = []
    ma = 0
    count = 0
    for i in ints:
        qu.append((i[0], 0))
        qu.append((i[1], 1))
    qu.sort(key=lambda x: x[0])
    res = 0
    for i in qu:
        if i[1] == 0:
            res += 1
            if ma < res:
                ma = res
                count = 1
            elif ma == res:
                count += 1
        else:
            res -= 1
    return ma, count
    
m, c = getMergeIntsMax(dat)
print(f'{m} {c}')
