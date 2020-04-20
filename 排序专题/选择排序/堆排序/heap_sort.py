def adjustHeap(arr: list, i: int, length: int):
    #先取出当前元素i
    temp = arr[i]
    #从i结点的左子结点开始，也就是2i+1处开始
    k = 2 * i + 1
    while k < length:
        #如果左子结点小于右子结点，k指向右子结点
        if k + 1 < length and arr[k] < arr[k + 1]:
            k += 1
        #如果子节点大于父节点，将子节点值赋给父节点（不用进行交换）
        if arr[k] > temp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = k * 2 + 1
    #将temp值放到最终的位置
    arr[i] = temp


def heap_sort(arr: list):
    #1.构建大顶堆
    for i in range(len(arr) // 2 - 1, -1, -1):
        #从第一个非叶子结点从下至上，从右至左调整结构
        adjustHeap(arr, i, len(arr))
        #2.调整堆结构+交换堆顶元素与末尾元素
    for j in range(len(arr) - 1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]  #将堆顶元素与末尾元素进行交换
        adjustHeap(arr, 0, j)  #重新对堆进行调整


li = [5, 4, 3, 2, 1]
heap_sort(li)
print(li)
