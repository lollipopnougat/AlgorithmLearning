def find_min_dis(a: list, b: list, c: list) -> tuple:
    la = len(a)
    lb = len(b)
    lc = len(c)
    i, j, k = 0, 0, 0
    stk = []
    dis = None
    while not (i == la or j == lb or k == lc):
        t = abs(a[i] - b[j]) + abs(b[j] - c[k]) + abs(a[i] - c[k])
        if dis:
            if t < dis:
                dis = t
                stk.append((a[i], b[j], c[k]))
        else:
            dis = t
        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] < a[i] and b[j] < c[k]:
            j += 1
        else:
            k += 1
    return (dis, stk[-1])


a = [-1, 0, 9]
b = [-25, -10, 10, 11]
c = [2, 9, 17, 30, 41]

print(find_min_dis(a, b, c))

