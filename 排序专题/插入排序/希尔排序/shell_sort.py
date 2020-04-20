def shell_sort(n: list):
    list_len = len(n)
    gap = list_len // 2
    while gap > 0:
        for i in range(gap, list_len):
            ins = n[i]
            j = i - gap
            while j >= 0 and ins < n[j]:
                n[j + gap] = n[j]
                j -= gap
            n[j + gap] = ins
        gap //= 2


li = [5, 4, 3, 2, 1]
li2 = [5, 4, 3, 2, 1, 7, 9, 8, 6, 0]

shell_sort(li2)
print(li2)
