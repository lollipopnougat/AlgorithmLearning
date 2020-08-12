def backpack01(goods_value: list, goods_volume: list,
               bag_capacity: int) -> int:
    length = len(goods_value)
    dp = [([0] * bag_capacity) for _ in range(length)]
    for i in range(length):
        for j in range(bag_capacity):
            if j + 1 < goods_volume[i]:
                dp[i][j] = dp[i - 1][j] #python -1 索引表示最后一个数组元素，因为本来就是0所以可以不用判断
            else:
                tmp = dp[i - 1][j - goods_volume[i]] + goods_value[i]
                dp[i][j] = max(dp[i - 1][j], tmp)
    return dp[length - 1][bag_capacity - 1]


gva = [1, 2, 3, 4, 5]
gvo = [1, 3, 4, 5, 6]
bc = 8

print(backpack01(gva, gvo, bc))



