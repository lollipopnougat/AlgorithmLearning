# -*- coding=utf-8 -*-
import os
import copy

class Node:
    x = 0
    y = 0

    def __init__(self, px: int, py: int):
        self.x = px
        self.y = py

    def printn(self):
        return "(%d, %d)" % (self.x, self.y)


class Queen:
    chess = []
    res = []
    num = 0
    sol_num = 0

    def __init__(self, n: int):
        self.chess = [[0] * n for i in range(n)]
        self.num = n

    def __cal_row(self, ch: list, row: int):
        if row == self.num:
            tmp = []
            print("---" * self.num)
            for i in range(self.num):
                print(ch[i], ' ')
                tmp.append(''.join('■' if ch[i][j] == 1 else '□' for j in range(self.num))) 
            self.sol_num += 1
            self.res.append(copy.deepcopy(ch)) # 注意列表里存储的是对象的引用，所以还是会变，需要深度拷贝(二维列表的元素本身就是一个一维列表的引用)
            return
        chess_tmp = ch
        for i in range(self.num):
            for j in range(self.num):
                chess_tmp[row][j] = 0
            chess_tmp[row][i] = 1
            if self.__is_ok(chess_tmp, row, i):
                self.__cal_row(chess_tmp, row + 1)

    def __is_ok(self, ch: list, row: int, col: int):
        step = 1
        while row - step >= 0:
            if ch[row - step][col] == 1:
                return False
            if col - step >= 0 and ch[row - step][col - step] == 1:
                return False
            if col + step < self.num and ch[row - step][col + step] == 1:
                return False
            step += 1
        return True

    def invoke(self):
        self.res = []
        self.__cal_row(self.chess, 0)

    def print_all(self):
        print('一共 %d 种'%(self.sol_num))
        for i in self.res:
            for j in i:
                print(j)
            print(' ')


if __name__ == "__main__":
    q = Queen(4)
    q.invoke()
    q.print_all()