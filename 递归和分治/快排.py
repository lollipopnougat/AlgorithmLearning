# -*- coding=utf-8 -*-
# 快速排序

''' 
import sys
sys.setrecursionlimit(10000) # 修改递归次数限制
'''


def get_index(num: list, low: int, high: int):
    tmp = num[low]
    while low < high:  # 当队尾的元素大于等于基准数据时,向前挪动high指针
        while low < high and num[high] >= tmp:
            high -= 1
        num[low] = num[high]  # 如果队尾元素小于tmp了,需要将其赋值给low
        while low < high and num[low] <= tmp:
            low += 1
        num[high] = num[low]
    num[low] = tmp
    return low


def quick_sort(num: list, low: int, high: int):
    if low < high:
        index = get_index(num, low, high)
        quick_sort(num, low, index - 1)
        quick_sort(num, index + 1, high)


if __name__ == "__main__":
    nums = [9, 6, 3, 2, 5, 8, 7, 4, 1, 0]
    try:
        quick_sort(nums, 0, 9)
    except Exception as er:
        print(str(er))
    for i in nums:
        print(i, ' ', end='')
    print(' ')