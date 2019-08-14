# -*- coding: utf-8 -*-
"""
维护一维数组，递归求解
"""
import time


def QueenAtRow2(chess, row):
    num = len(chess)
    if row == num:
        print("---" * num)
        print(chess, ' ')
        return
    chessTmp = chess
    # 向这一行的每一个位置尝试排放皇后
    # 然后检测状态，如果安全则继续执行递归函数摆放下一行皇后
    for i in range(num):
        # 摆放这一行的皇后，之前要清掉所有这一行摆放的记录
        chessTmp[row] = i
        if is_conflict(chessTmp, row, i):
            QueenAtRow2(chessTmp, row + 1)


def is_conflict(chess, row, col):
    step = 1
    # 判断中上、左上、右上是否冲突
    for i in range(row - 1, -1, -1):
        if chess[i] == col:
            return False
        if chess[i] == col - step:
            return False
        if chess[i] == col + step:
            return False
        step += 1
    return True


if __name__ == '__main__':
    for queenNum in range(8, 10):
        # queenNum = 8  # 修改不同的皇后数
        chess = [0 for j in range(queenNum)]  # 初始化棋盘，全部置0
        time1 = time.time()
        QueenAtRow2(chess, 0)
        print('消耗时间为：', time.time() - time1)
        input()