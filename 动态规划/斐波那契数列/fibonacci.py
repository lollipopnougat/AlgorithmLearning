# 动态规划

def fib(n):
    if n <= 0:
        return None
    i1, i2 = 1, 1
    if n <= 2:
        return 1
    for i in range(n - 2):
        tmp = i1 + i2
        i1 = i2
        i2 = tmp
    return i2

# 使用帮助理解的DP
def fib_info(n):
    if n <= 0:
        return None
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]


# yield 实现
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print(fib(8))

# for n in fab(8):
#     print(n)