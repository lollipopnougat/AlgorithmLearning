from typing import List
import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        self.res = []
        cur = math.ceil(math.log(label + 1, 2))
        self.helper(label, cur)
        return self.res

    def helper(self, label:int, cur: int):
        self.res.insert(0, label)
        if cur == 1:
            return
        cur_num = cur_one = 2 ** (cur - 1)
        if cur & 1:
            cur_index = label - cur_one
            last_cur = cur_index // 2
            par_num = 2 ** (cur - 1) - 1 - last_cur
        else:
            cur_index = cur_num - (label - cur_one) - 1
            last_cur = cur_index // 2
            par_num = 2 ** (cur - 2) + last_cur
        self.helper(par_num, cur - 1)

class Solution2:
    def pathInZigZagTree(self, label: int) -> List[int]:
        self.res = []
        cur = math.ceil(math.log(label + 1, 2))
        while cur >= 1:
            self.res.insert(0, label)
            cur_one = 2 ** (cur - 1)
            if cur & 1:
                cur_index = label - cur_one
                last_cur = cur_index // 2
                label = 2 ** (cur - 1) - 1 - last_cur
            else:
                cur_index = cur_one - (label - cur_one) - 1
                last_cur = cur_index // 2
                label = 2 ** (cur - 2) + last_cur
            cur -= 1
        return self.res

    def pathInZigZagTree2(self, label: int) -> List[int]:
        ''' tql 
        位运算即可。具体解释见题解。
        举例14=1110b，
        先将14右移，变为111b，然后对除第一位外所有位取反变为100b，即它的根节点4，
        同理100b，右移变为10b，对除第一位外所有位取反变为11b，即它的根节点3
        一直到1结束。
        '''
        res = []
        while label != 1:
            res.append(label)
            label >>= 1
            # 这里我采用异或实现
            label = label ^(1 << (label.bit_length() - 1)) - 1
        return [1]+res[::-1]



s = Solution2()

print(s.pathInZigZagTree(1))
print(s.pathInZigZagTree(3))
print(s.pathInZigZagTree(6))
print(s.pathInZigZagTree(14))
print(s.pathInZigZagTree(10))
print(s.pathInZigZagTree(26))
print(s.pathInZigZagTree(31))
        


