import itertools
class Solution:
    def permute(self, nums: list) -> list:
        return list(itertools.permutations(nums))

class Solution2:
    def permute(self, nums: list) -> list:
        res = []
        def perm(lst:list, p:int, e:int):
            if p == e:
                res.append(lst[:])
            else:
                for i in range(p, e):
                    lst[i], lst[p] = lst[p], lst[i]
                    perm(lst, p + 1, e)
                    lst[i], lst[p] = lst[p], lst[i]
        perm(nums, 0, len(nums))
        return res

s = Solution2()
s2 = Solution()
li = ['a', 'b', 'c']

print(s.permute(li))
print(s2.permute(li))