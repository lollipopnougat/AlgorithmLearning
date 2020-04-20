def select_sort(array:list):
    max_index = 0
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i):
            if array[j] > array[max_index]:
                max_index = j
        array[length - i - 1], array[max_index] = array[max_index], array[length - i - 1]
        max_index = 0
    
li = [5, 4, 3, 2, 1]
select_sort(li)
print(li)
input()

    

