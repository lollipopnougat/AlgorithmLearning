# -*- coding: utf-8 -*-
"""
维护8×8格的矩阵，递归求解
"""
import time


def QueenAtRow(chess, row):
    num = len(chess[0])
    if row == num:
        print("---" * num)
        for i in range(num):
            print(chess[i], ' ')
        return
    chessTmp = chess
    # 向这一行的每一个位置尝试排放皇后
    # 然后检测状态，如果安全则继续执行递归函数摆放下一行皇后
    for i in range(num):
        for j in range(num):
            # 摆放这一行的皇后，之前要清掉所有这一行摆放的记录
            chessTmp[row][j] = 0
        chessTmp[row][i] = 1
        if is_conflict(chessTmp, row, i):
            QueenAtRow(chessTmp, row + 1)


def is_conflict(chess, row, col):
    step = 1
    while row - step >= 0:
        if chess[row - step][col] == 1:
            return False
        if col - step >= 0 and chess[row - step][col - step] == 1:
            return False
        if col + step < len(chess[0]) and chess[row - step][col + step] == 1:
            return False
        step += 1
    return True


if __name__ == '__main__':
    queenNum = 8  #修改不同的皇后数
    chess = [[0 for i in range(queenNum)]
             for j in range(queenNum)]  #初始化棋盘，全部置0
    time1 = time.time()
    QueenAtRow(chess, 0)
    print('消耗时间为：', time.time() - time1)
    input()
