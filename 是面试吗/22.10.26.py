#1024 马尔科夫链
class A:
    '''
    不使用闭包能提高速度
    '''
    def permute(self, nums: list) -> list:
        self.res = []
        self.perm(nums, 0, len(nums))
        return self.res

    def perm(self, lst, p: int, e: int):
        if p == e:
            self.res.append(lst[:])
        else:
            for i in range(p, e):
                lst[i], lst[p] = lst[p], lst[i]
                self.perm(lst, p + 1, e)
                lst[i], lst[p] = lst[p], lst[i]

def cal(x: int, op: str, y: int) -> int:
    if op == '|':
        return x | y
    elif op == '+':
        return x + y
    elif op == '^':
        return x ^ y
    elif op == '*':
        return x * y
    elif op == '%' and y != 0:
        return x % y
    elif op == '-':
        return x - y
    elif op == '<<':
        return x << y
    elif op == '>>':
        return x >> y
    elif op == '**':
        return x ** y
    elif op == '//' and y != 0:
        return x // y
    else:
        return -1

# nums = [2, 7, 1, 30, 31, 29, 2, 15, 6, 2, 15, 5, 8, 1024, 14]
# 8 6 0
# 3 4 9 10
nums = [1, 2, 2, 2, 6, 7, 14, 15, 26, 29, 30, 965]
ops = ['>>', '<<', '*']
a = A()
ops_c = a.permute(ops)
nums.sort()
n = len(nums)

for i in range(n):
    for j in range(n):
        if j == i:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            for m in range(n):
                if m == i or m == j or m == k:
                    continue
                for o in ops_c:
                    res1 = cal(nums[i], o[0], nums[j])
                    res2 = cal(res1, o[1], nums[k])
                    res = cal(res2, o[2], nums[m])
                    if res == 1024:
                        print(f'{nums[i]} {o[0]} {nums[j]} {o[1]} {nums[k]} {o[2]} {nums[m]} = {res}')

