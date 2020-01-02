# 我的思路： 设计一个寻找两个字符串的最长公共前缀的函数，然后遍历字符串列表调用此函数找出最长，
# 采用了分治法的思想 每次只需要比较前一次的结果和当前的字符串，把结果暂存准备下次使用
class Solution:
    # 非递归版
    def longestCommonPrefix(self, strs: list) -> str:
        l = len(strs)
        if l < 2:
            return '' if l == 0 else strs[0]
        elif l == 2:
            return self.findCommonPrefix(strs[0], strs[1])
        else:
            tmp = self.findCommonPrefix(strs[0], strs[1])
            for i in range(2, l):
                tmp = self.findCommonPrefix(tmp, strs[i])
            return tmp

    def findCommonPrefix(self, strl: str, strr: str) -> str:
        limit = min(len(strl), len(strr))
        flag = True
        for i in range(limit):
            if strl[i] != strr[i]:
                return strl[0:i]
        return strl[0:limit]

    # 递归版
    def reLongestCommonPrefix(self, strs: list, num: int) -> str:
        l = len(strs)
        if l < 2:
            return '' if l == 0 else strs[0]
        elif num == len(strs) - 2:
            return self.findCommonPrefix(strs[num], strs[num + 1])
        else:
            return self.findCommonPrefix(
                strs[num], self.reLongestCommonPrefix(strs, num + 1))


# 啊我又好了（指看到大佬的代码）
class Solution2:
    def longestCommonPrefix(self, strs: list) -> str:
        result = ""
        for temp in zip(*strs):
            if len(set(temp)) == 1:
                result += temp[0]
            else:
                break
        return result


s = Solution()

strs = ['apple', 'application', 'apex']

print(s.longestCommonPrefix(strs))
print(s.reLongestCommonPrefix(strs, 0))
