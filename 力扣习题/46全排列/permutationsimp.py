import itertools


class Solution:
    def permute(self, nums: list) -> list:
        return list(itertools.permutations(nums))


class Solution2:
    def permute(self, nums: list) -> list:
        res = []

        def perm(lst: list, p: int, e: int):
            if p == e:
                res.append(lst[:])
            else:
                for i in range(p, e):
                    lst[i], lst[p] = lst[p], lst[i]
                    perm(lst, p + 1, e)
                    lst[i], lst[p] = lst[p], lst[i]

        perm(nums, 0, len(nums))
        return res


class Solution3:
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


s = Solution2()
s2 = Solution()
li = ['a', 'b', 'c']

#print(s.permute(li))
print(s2.permute(li))