# -*- coding: utf-8 -*-
"""
八皇后——盲目迭代法
"""
def check_1(a, n):
    for i in range(1, n):
        for j in range(0, i):
            if a[i] == a[j] or abs(a[i]-a[j]) == i - j:
                return False
    return True # 不冲突
 
def queens_1():
    a= [0 for i in range(8)]
    count = 0
    for a[0] in range(8):
        for a[1] in range(8):
            for a[2] in range(8):
                for a[3] in range(8):
                    for a[4] in range(8):
                        for a[5] in range(8):
                            for a[6] in range(8):
                                for a[7] in range(8):
                                    if check_1(a,8) == False:
                                        continue
                                    else:
                                        print(a)
                                        count += 1
    print('八皇后问题的全部解法：',count)
 
if __name__ == '__main__':
    queens_1()
    input()