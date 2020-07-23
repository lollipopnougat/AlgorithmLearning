
# https://baijiahao.baidu.com/s?id=1659735837100760934&wfr=spider&for=pc

def get_next(pattern):
    length = len(pattern)
    next = [0] * length
    j = 0
    for i in range(2, length):
        while j != 0 and pattern[j] != pattern[i - 1]:
            j = next[j]
        if pattern[j] == pattern[i - 1]:
            j += 1
        next[i] = j
    return next


def kmp_find(string, pattern):
    next = get_next(pattern)
    length = len(pattern)
    str_len = len(string)
    j = 0
    for i in range(str_len):
        while j > 0 and string[i] != pattern[j]:
            j = next[j]
        if string[i] == pattern[j]:
            j += 1
        if j == length:
            return i - length + 1
    return -1


def simple_kmp(st, pa):
    pat_len = len(pa)
    str_len = len(st)
    next = [0] * pat_len
    j = 0
    # 生成next数组 记录了下次模式串要比较的位置
    for i in range(2, pat_len):
        while j > 0 and pa[j] != pa[i - 1]:
            j = next[j]
        if pa[j] == pa[i - 1]:
            j += 1
        next[i] = j
    j = 0
    # 比较
    for i in range(str_len):
        while j > 0 and st[i] != pa[j]:
            j = next[j]
        if st[i] == pa[j]:
            j += 1
        if j == pat_len:
            return i - pat_len + 1
    return -1
    
# 时间复杂度O(m + n)

print(get_next('gtgtgcf'))

print(kmp_find('uefhiuefbeuifgbrygfecfge78fgABCDEdfbfbdddb', 'CDE'))
