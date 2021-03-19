def lcsl(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    length = [([0] * n) for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                length[i][j] = length[i - 1][j - 1] + 1
            else:
                length[i][j] = max(length[i][j - 1], length[i - 1][j])
    return length[m][n]


def lcslr(s1: str, s2: str, i: int, j: int) -> int:
    if i < 0 or j < 0:
        return 0
    elif s1[i] == s2[j]:
        return 
    else:
        return lcslr()
