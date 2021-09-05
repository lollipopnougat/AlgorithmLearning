# The rand7() API is already defined for you.
import random


def rand7():
    random.randint(1, 7)


# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b = rand7(), rand7()
        while a > 6:
            a = rand7()
        while b > 5:
            b = rand7()
        return (0 + b) if a & 1 else (5 + b)

    def rand10n(self):
        '''
        拒绝采样，
        主要公式为 (rand(X)-1)*Y + randY() -----生成 [1,X*Y]区间，并且等概。 记住就完事了，xdm
        '''
        while True:
            res = (rand7() - 1) * 7 + rand7()  #构造1~49的均匀分布
            if res <= 40:  #剔除大于40的值，1-40等概率出现。
                break
        return res % 10 + 1  #构造1-10的均匀分布
