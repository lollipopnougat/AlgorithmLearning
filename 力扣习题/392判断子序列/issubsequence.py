class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        if length == 0:
            return True
        i = 0
        for j in t:
            if s[i] == j:
                i += 1
                if i == length:
                    return True
        return False

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(i in t for i in s) 

class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        tm = iter(t)
        res = []
        for i in s:
            if i in tm:
                res.append(i)
            else:
                res.append(None)

        res = iter(res)
        return all(res)


s = Solution3()
print(s.isSubsequence('321','123abc'))