'''
给两个正整数a，b，其中 a > b，求最小的 x 使 a % (b + x) == 0 或 a % (b - x) == 0 成立
'''
import math
def q1_b(a: int, b: int) -> int:
    if a % b == 0:
        return 0
    x = 1
    while a % (b + x) != 0 and a % (b - x) != 0:
        x += 1
    return x

def q1(a: int, b: int) -> int:
    if a % b == 0:
        return 0
    res = float('inf')
    d = math.floor(math.sqrt(a)) + 1
    for i in range(1, d):
        if a % i == 0:
            res = min(abs(b - i), res)
            res = min(abs(b - a / i), res)
    return int(res)


print(q1(100, 23))
print(q1_b(100, 23))
print(q1(102, 23))
print(q1_b(102, 23))

'''
求最小操作次数使得字符串中连续0的个数为a的倍数，连续1的个数为b的倍数，每个操作只能将一个1变为0或将一个0变为1
'''
def q2(text: str, a: int, b: int) -> int:
    n = len(text)
    if n < a and n < b:
        return -1
    inf = float('inf')
    dp = [inf] * n
    zeros = [0] * n
    ones = [0] * n
    if text[0] == '0':
        zeros[0] = 1
    else:
        ones[0] = 1
    for i in range(1, n):
        if text[i] == '0':
            zeros[i] = zeros[i - 1] + 1
            ones[i] = ones[i - 1]
        else:
            zeros[i] = zeros[i - 1]
            ones[i] = ones[i - 1] + 1
    dp[a - 1] = min(ones[a - 1], dp[a - 1])
    dp[b - 1] = min(zeros[b - 1], dp[b - 1])
    for i in range(max(a, b), n):
        if dp[i - a] == inf and dp[i - b] == inf:
            dp[i] = inf
            continue
        if dp[i - a] != inf:
            dp[i] = min(dp[i - a] + ones[i] - ones[i - a], dp[i])
        if dp[i - b] != inf:
            dp[i] = min(dp[i - b] + zeros[i] - zeros[i - b], dp[i])
    return dp[n - 1] if (dp[n - 1] != inf) else -1

print(q2('0111110000', 5, 5))
print(q2('0000011111', 5, 5))
print(q2('0001111000', 4, 3))
print(q2('0001111000', 4, 2))
print(q2('0001111000', 4, 7))
print(q2('0111110000', 5, 5))