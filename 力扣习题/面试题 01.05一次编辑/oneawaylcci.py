class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lf = len(first)
        ls = len(second)
        if abs(lf - ls) > 1:
            return False
        elif lf - ls == 1:
            i = j = 0
            fl = True
            while i < lf and j < ls:
                if first[i] == second[j]:
                    i += 1
                    j += 1
                elif fl:
                    i += 1
                    fl = False
                else:
                    return False
            return True
        elif ls - lf == 1:
            i = 0
            j = 0
            fl = True
            while i < lf and j < ls:
                if first[i] == second[j]:
                    i += 1
                    j += 1
                elif fl:
                    j += 1
                    fl = False
                else:
                    return False
            return True
        elif lf == ls:
            i = j = 0
            fl = True
            while i < lf and j < ls:
                if first[i] == second[j]:
                    i += 1
                    j += 1
                elif fl:
                    j += 1
                    i += 1
                    fl = False
                else:
                    return False
            return True


fi = ['aaab', 'aaa', 'abc', 'aca', 'app', 'pdd', 'aaabca', 'pale', 'pales']
se = ['aaab', 'aaab', 'acb', 'acb', 'pp', 'ddd', 'aabc', 'ple', 'pal']

s = Solution()
# print(s.oneEditAway('abc','acb'))
res = []
for i in range(len(fi)):
    res.append(s.oneEditAway(fi[i], se[i]))
print(res)
