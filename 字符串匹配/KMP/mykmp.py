def get_next(text:str) -> list:
    length = len(text)
    next_arr = [0] * length
    i, j = 1, 0
    while i < length:
        if text[i] == text[j]:
            j += 1
            next_arr[i] = j
            i += 1
        elif j == 0:
            next_arr[i] = 0
            i += 1
        else:
            j = next_arr[j - 1]
    return next_arr

def mykmp_search(text:str, pat:str) -> int:
    next_arr = get_next(pat)
    tlen = len(text)
    plen = len(pat)
    i, j = 0, 0
    while i < tlen:
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == plen:
                return i - j
        elif j == 0:
                i += 1
        else:
            j = next_arr[j - 1]
    return -1


def quick_kmp(t, p):
    tlen = len(t)
    plen = len(p)
    next_arr = [0] * plen
    i, j = 1, 0
    if tlen < plen:
        return -1
    if plen == 0:
        return 0
    while i < plen:
        if t[i] == t[j]:
            next_arr[i] = j
            i, j = i + 1, j + 1
        elif j == 0:
            next_arr[i] = 0
            i += 1
        else:
            j = next_arr[j - 1]
    i = j = 0
    while i < tlen:
        if t[i] == p[j]:
            i, j = i + 1, j + 1
            if j == plen:
                return i - j
        elif j == 0:
                i += 1
        else:
            j = next_arr[j - 1]
    return -1


print(get_next('ababcabc'))
print(get_next('uefhiuefbeuifgbrygfecfge78fgABCDEdfbfbdddb'))
print(mykmp_search('ababcababcabc', 'ababcabc'))
print(quick_kmp('uefhiuefbeuifgbrygfecfge78fgABCDEdfbfbdddb', 'CDE'))
print(mykmp_search('mississippi','issip'))
