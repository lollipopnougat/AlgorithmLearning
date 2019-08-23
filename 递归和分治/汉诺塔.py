# -*- coding=utf-8 -*-
# 汉诺塔


def hanoi(a, b, c, n):
    if n == 1:
        print(a, ' --> ', b)
    else:
        hanoi(a, c, b, n - 1)  # n-1个盘子从A移到B
        hanoi(a, b, c, 1)  # 剩下一个盘子从A移到C
        hanoi(b, a, c, n - 1)  #B上n-1个盘子移到C上


if __name__ == "__main__":
    try:
        n = int(input('输入阶数: '))
        hanoi('A', 'B', 'C', n)
    except Exception as er:
        print(str(er))