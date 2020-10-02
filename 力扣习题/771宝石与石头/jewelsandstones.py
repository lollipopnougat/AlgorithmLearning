class Solution:
    '''
    普通解法
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for i in S:
            if i in J:
                c += 1
        return c


class Solutionn:
    '''
    普通解法(???)
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)
        c = 0
        for i in S:
            if i in s:
                c += 1
        return c



class Solution2:
    '''
    起飞！！！
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)
        return sum([(1 if i in J else 0) for i in S]) 

class Solution3:
    '''
    pythonic
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)

