class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        p = {}
        n = len(s)
        for i in range(n):
            if s[i] in m:
                if t[i] != m[s[i]]:
                    return False
            else:
                if t[i] in p:
                    if p[t[i]] != s[i]:
                        return False
                else:
                    m[s[i]] = t[i]
                    p[t[i]] = s[i]
        return True

s = Solution()
print(s.isIsomorphic('egg','add'))
print(s.isIsomorphic('badc','baba'))