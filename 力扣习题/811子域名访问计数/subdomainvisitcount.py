from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        ret = []
        for i in cpdomains:
            tmp = i.split(' ')
            times = int(tmp[0])
            domains = tmp[1].split('.')
            n = len(domains)
            res[domains[-1]] = res.get(domains[-1], 0) + times
            res[tmp[1]] = res.get(tmp[1], 0) + times
            if n == 3:
                second = f'{domains[-2]}.{domains[-1]}'
                res[second] = res.get(second, 0) + times
        for k in res.keys():
            ret.append(f'{res[k]} {k}')
        return ret

class Solution2:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for n in cpdomains:
            temp = n.split(' ')
            times, name = int(temp[0]), temp[1]
            cnt[name] += times
            for i in range(len(name)):
                if name[i] == '.':
                    cnt[name[i+1:]] += times
        return [str(cnt[key]) + " " + key for key in cnt]

s = Solution()

inp = ["9001 discuss.leetcode.com"]
res = s.subdomainVisits(inp)
print(res)
inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
res = s.subdomainVisits(inp)
print(res)