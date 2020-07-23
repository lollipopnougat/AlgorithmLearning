# 朴素的搜索(暴力)实现
def bf_find(string, pattern):
    pat_len = len(pattern)
    str_len = len(string)
    j = 0
    for i in range(str_len):
        while j > 0 and string[i] != pattern[j]:
            j = 0
        if string[i] == pattern[j]:
            j += 1
        if j == pat_len:
            return i - pat_len + 1
    return -1


print(bf_find('uefhiuefbeuifgbrygfecfge78fgABCDEvsfsdvs', 'CDE'))