class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()
        def dfs(li):
            t = sum(li)
            for i in candidates:
                if li and i < li[-1]:
                    continue
                if t + i == target:
                    li.append(i)
                    res.append(li[:])
                    li.pop()
                    return
                elif t + i < target:
                    li.append(i)
                    dfs(li[:])
                    li.pop()
                else:
                    continue
        dfs([])
        return res

class Solution2:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()
        le = len(candidates)
        stack = [-1]
        li = []
        while stack:
            i = stack.pop() + 1
            if i == le and stack:
                li.pop()
            while i < le:
                t = sum(li)
                if li and candidates[i] < li[-1]:
                    i += 1
                if t + candidates[i] == target:
                    li.append(candidates[i])
                    res.append(li[:])
                    if li[-1] < target:
                        li.pop()
                    li.pop()
                    break
                elif t + candidates[i] < target:
                    li.append(candidates[i])
                    stack.append(i)
                else:
                    if li:
                        li.pop()
                    break
        return res
                    




s = Solution2()

li = [2]

print(s.combinationSum(li, 1))