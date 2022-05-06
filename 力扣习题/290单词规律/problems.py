class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(' ')
        l = len(strs)
        if len(pattern) != l:
            return False
        s = {}
        ss = set()
        for i in range(l):
            if pattern[i] not in s:
                if strs[i] in ss:
                    return False
                ss.add(strs[i])
                s[pattern[i]] = strs[i]
            elif s[pattern[i]] != strs[i]:
                return False
        return True