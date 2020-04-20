def insert_sort_short(n: list):
    for i in range(1, len(n)):
        j = i
        while j >= 1 and n[j - 1] > n[j]:
            n[j], n[j - 1] = n[j - 1], n[j]
            j -= 1

def insert_sort(n: list):
    for i in range(1, len(n)):
        j = i
        tmp = n[i]
        while j >= 1 and n[j - 1] > tmp:
            n[j] = n[j - 1]
            j -= 1
        n[j] = tmp

li = [5, 4, 3, 2, 1]
li2 = [5, 4, 3, 2, 1, 7, 9, 8, 6, 0]

insert_sort(li2)
print(li2)
