# 标准快排
def get_index(numlist:list, low: int, high: int) -> int:
    tmp = numlist[low]
    while low < high:
        while low < high and numlist[high] >= tmp:
            high -= 1
        numlist[low] = numlist[high]
        while low < high and tmp >= numlist[low]:
            low += 1
        numlist[high] = numlist[low]
    numlist[low] = tmp
    return low


def quick_sort_o(numlist: list, low: int, high: int):
    if low < high:
        index = get_index(numlist, low, high)
        quick_sort_o(numlist, low, index - 1)
        quick_sort_o(numlist, index + 1, high)

# 一分钟写快排
def quick_sort(n: list, l: int, h: int):
    ol = l
    oh = h
    if l < h:
        t = n[l]
        while l < h:
            while l < h and n[h] >= t:
                h -= 1
            n[l] = n[h]
            while l < h and n[l] <= t:
                l += 1
            n[l] = t
        quick_sort(n, ol, l - 1)
        quick_sort(n, l + 1, oh)


li = [1, 5, 2, 9, 3, 7]
quick_sort(li, 0, len(li) - 1)
print(li)
