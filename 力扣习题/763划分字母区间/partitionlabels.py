class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        m = {}
        s = e = 0
        l = len(S)
        for i in range(l):
            m[S[i]] = i
        for i in range(l):
            e = max(e, m[S[i]])
            if i == e:
                res.append(e - s + 1)
                s = i + 1
        return res