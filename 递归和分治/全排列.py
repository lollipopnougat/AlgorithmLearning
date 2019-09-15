# -*- coding=utf-8 -*-
# 全排列递归算法 时间复杂度O(n!) 如果数据量较大就无能为力了
'''
算法:
比如求{a,b,c,d}的全排列
1. 固定a,求{b,c,d}的全排列(递归)
    (1). 固定b,求{c,d}的全排列(递归)
        a. 固定c,求{d}的全排列(递归)
            * d的排列只有一种,输出此轮结果
        b. 固定d,求{c}的全排列(递归)
            * c的全排列只有一种,输出此轮结果
    (2). 固定c,求{b,d}全排列(递归)
        ...
        ...
完成 `1.` 以后我们得到了第一个元素为a时{b,c,d}的全排列,
此时我们只要把第一个元素分别换成b,c,d
再调用递归函数递归计算即可获得最终结果

递归函数
参数: lst:传入的数组对象, p: 求全排列的开始位置(数组下标), e: 全排列的结束位置

如果 p==e 一次排列完成，输出
如果不相等, 将此次递归开始位置元素按顺序与后面元素一个一个交换,调用递归函数计算下一轮
'''

list = []


def perm(lst, p, e):
    if p == e:
        #global list
        #list.append(lst)
        print(lst)
    else:
        for i in range(p, e):
            lst[i], lst[p] = lst[p], lst[i]
            perm(lst, p + 1, e)
            lst[i], lst[p] = lst[p], lst[i]


class perm:
    list = []
    reslist = []

    def __init__(self, lst):
        self.list = lst

    def go(self, p, e):
        if p == e:
            self.reslist.append(list[:])
        else:
            for i in range(p, e):
                self.list[i], self.list[p] = self.list[p], self.list[i]
                self.go(p + 1, e)
                self.list[i], self.list[p] = self.list[p], self.list[i]

    def show(self):
        for i in self.reslist:
            for j in i:
                print(j, ' ', end='')
            print(' ')


list = ['A', 'B', 'C']
#perm(list, 0, len(list))

Per = perm(list)

Per.go(0,len(list))
Per.show()

'''
for i in list:
    for j in i:
        print(j, ' ', end='')
    print(' ')
'''
input()
