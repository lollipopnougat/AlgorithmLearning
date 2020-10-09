class Solution:
    def combinationSum2(self, candidates:list, target: int) -> list:
        self.res = set()
        self.flag = False
        self.helper(candidates,target, [])
        return list(self.res)
        

    def helper(self, can, tar, tmp):
        l = len(can)
        for i in range(l):
            if can[i] == tar:
                tmp.append(can[i])
                self.res.add(tuple(sorted(tmp)))
                tmp.pop()
            if can[i] < tar:
                t = can[i]
                tmp.append(t)
                can.pop(i)
                self.helper(can, tar - t, tmp)
                tmp.pop()
                can.insert(i, t)


class Solution2:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        self.candidates = candidates
        self.res = []
        self.target = target
        self.dfs(0, [])
        return (self.res)

    def dfs(self, level, res_current):
        for i in range(level, len(self.candidates)):
            if i > level:
                if self.candidates[i] == self.candidates[i - 1]: continue
            if sum(res_current) + self.candidates[i] == self.target:
                    self.res.append(res_current[:] + [self.candidates[i]])
                    return
            elif sum(res_current) + self.candidates[i] < self.target:
                self.dfs(i + 1, res_current[:] + [self.candidates[i]])
            else: 
                return

s = Solution2()
sr = [4,2,2,2]
t = 6

print(s.combinationSum2(sr,t))


