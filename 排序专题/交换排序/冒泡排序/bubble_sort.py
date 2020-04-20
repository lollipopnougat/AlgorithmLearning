def bubble_sort(n: list):
    for i in range(len(n) - 1):
        for j in range(len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]


li = [5, 4, 3, 2, 1]
li2 = [5, 4, 3, 2, 1, 7, 9, 8, 6, 0]

bubble_sort(li2)
print(li2)