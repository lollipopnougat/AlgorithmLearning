from typing import List


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        que = []
        m = {}
        s = set()
        res = set([i for i in range(numCourses)])
        for i in prerequisites:
            if i[0] not in m:
                m[i[0]] = []
            m[i[0]].append(i[1])
        for i in range(numCourses):
            if i in res:
                if i not in m:
                    res.remove(i)
                else:
                    que.insert(0, i)
                    s.add(i)
                    while que:
                        if que[0] not in m:
                            k = que.pop(0)
                            s.remove(k)
                            if k in res:
                                res.remove(k)
                        elif m[que[0]] not in res:
                            k = que.pop(0)
                            s.remove(k)
                            if k in res:
                                res.remove(k)
                        elif m[que[0]] in s:
                            return False
                        else:
                            t = m[que[0]]
                            que.insert(0, t)
                            s.add(t)
        return len(res) == 0


s = Solution()
print(s.canFinish(2, [[0, 1]]))
print(s.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
