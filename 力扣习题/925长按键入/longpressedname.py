class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        '''
        双指针
        '''
        i = j = 0
        ln, lt = len(name), len(typed)
        while i < ln and j < lt:
            if name[i] == typed[j]:
                while (i >= ln - 1 or name[i] != name[i + 1]) and j < lt - 1 and typed[j] == typed[j + 1]:
                    j += 1
                j += 1
                i += 1
            else:
                return False
        if i == ln and j == lt:
            return True
        else:
            return False

from itertools import *
class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1, g2 = groupby(name), groupby(typed)
        for (c1, groups1), (c2, groups2) in zip_longest(g1, g2, fillvalue=(repeat(''), None)):
            if c1 != c2 or len(list(groups1)) > len(list(groups2)):
                return False
        return True

s = Solution2()

print(s.isLongPressedName('leet','lleeetr'))