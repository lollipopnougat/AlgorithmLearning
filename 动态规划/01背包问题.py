# -*- coding=utf-8 -*-
# 01背包问题


def backpack01(goods_bulk: list, goods_value: list, bag_capacity: int):
    if len(goods_bulk) != len(goods_value) or goods_bulk[0] != 0 or goods_value[0] != 0:
        raise Exception('参数不合法')
    dp_list = [[0 for k in range(bag_capacity + 1)] for x in range(len(goods_bulk))]
    for i in range(1, 5):
        for j in range(1, bag_capacity + 1):
            if j < goods_bulk[i]:
                dp_list[i][j] = dp_list[i - 1][j]
            else:
                dp_list[i][j] = max(
                    dp_list[i - 1][j],
                    dp_list[i - 1][j - goods_bulk[i]] + goods_value[i])
    return dp_list



'''dp_list = [[0 for k in range(9)] for x in range(5)]

for i in range(1, 5):
    for j in range(1, bag_capacity + 1):
        if j < goods_bulk[i]:
            dp_list[i][j] = dp_list[i - 1][j]
        else:
            dp_list[i][j] = max(
                dp_list[i - 1][j],
                dp_list[i - 1][j - goods_bulk[i]] + goods_value[i])
'''
if __name__ == "__main__":
    gb = [0, 2, 3, 4, 5]
    gv = [0, 3, 4, 5, 6]
    bc = 8
    maxv = 0
    dp = backpack01(gb, gv, bc)
    for i in dp:
        for j in i:
            if j > maxv:
                maxv = j
            print(j, ' ', end='')
        print(' ')
    print('由此得知最大价值是 ',maxv)
    input()