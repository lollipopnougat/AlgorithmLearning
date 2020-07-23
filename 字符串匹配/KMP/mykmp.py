def get_next(text:str) -> list:
    length = len(text)
    next_arr = [0] * length
    i, j, count = 1, 0, 0
    while i < length:
        if text[i] == text[j]:
            count += 1
            next_arr[i] = count
            i += 1
            j += 1
        elif j == 0:
            next_arr[i] = count
            j = 0;
            i += 1
        else:
            count = 0
            j = 0
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

print(get_next('ababcabc'))
print(mykmp_search('ababcababcabc', 'ababcabc'))
