# -*- coding=utf-8 -*-
# Prim算法求最小生成树
# 来源 https://blog.csdn.net/yht201293018/article/details/81321743
import sys
if __name__ == '__main__':
    MAX = sys.maxsize
    primgraph = [[MAX, 10, MAX, MAX, MAX, 11, MAX, MAX, MAX],
                 [10, MAX, 18, MAX, MAX, MAX, 16, MAX, 12],
                 [MAX, 18, MAX, 22, MAX, MAX, MAX, MAX, 8],
                 [MAX, MAX, 22, MAX, 20, MAX, MAX, 16, 21],
                 [MAX, MAX, MAX, 20, MAX, 26, 7, 19, MAX],
                 [11, MAX, MAX, MAX, 26, MAX, 17, MAX, MAX],
                 [MAX, 16, MAX, MAX, 7, 17, MAX, 19, MAX],
                 [MAX, MAX, MAX, 16, 19, MAX, 19, MAX, MAX],
                 [MAX, 12, 8, 21, MAX, MAX, MAX, MAX, MAX]]
    chararray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    charlist = []
    charlist.append(chararray[0])
    mid = []  #mid[i]表示生成树集合中与点i最近的点的编号
    lowcost = []  #lowcost[i]表示生成树集合中与点i最近的点构成的边最小权值 ，-1表示i已经在生成树集合中
    lowcost.append(-1)
    mid.append(0)
    n = len(chararray)
    for i in range(1, n):  #初始化mid数组和lowcost数组
        lowcost.append(primgraph[0][i])
        mid.append(0)
    sum = 0
    for _ in range(1, n):  #插入n-1个结点
        minid = 0
        min = MAX
        for j in range(1, n):  #寻找每次插入生成树的权值最小的结点
            if (lowcost[j] != -1 and lowcost[j] < min):
                minid = j
                min = lowcost[j]
        charlist.append(chararray[minid])
        print(chararray[mid[minid]] + '——' + chararray[minid] + '权值：' +
              str(lowcost[minid]))
        sum += min
        lowcost[minid] = -1
        for j in range(1, n):  #更新插入结点后lowcost数组和mid数组值
            if (lowcost[j] != -1 and lowcost[j] > primgraph[minid][j]):
                lowcost[j] = primgraph[minid][j]
                mid[j] = minid
    print("sum=" + str(sum))
    print("插入结点顺序：" + str(charlist))
