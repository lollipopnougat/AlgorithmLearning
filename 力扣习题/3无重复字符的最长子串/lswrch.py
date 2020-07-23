'''
动态规划 还挺好做的
 状态转移：
1. 第i个字符从未出现过，则dp[i] = dp[i-1] + 1；
2. 第i个字符出现过， 这时我们找出第i个字符最近一次出现的位置index,记两个的距离为d = i - index：
  1） d<=dp[i-1],即这个字符出现在以第i-1个字符结尾的不包含重复数组的子字符串中，则dp[i] = d；
  2） d>dp[i-1], 即这个字符没有出现在以第i-1个字符结尾的不包含重复数组的子字符串中，则dp[i] = dp[i-1] + 1 。

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        store_index = {}
        dp = [0] * len(s)
        res = 1
        for i in range(len(s)):
            if s[i] in store_index:
                d = i - store_index[s[i]]
                dp[i] = d if d <= dp[i - 1] else dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1
            store_index[s[i]] = i
            res = max(res, dp[i])
        return res


'''
大佬优化的动态规划
ans : 上一个位置的最长字串长度
i : 重复元素下一个元素的位置，
想象成一个队列，一边添加，遇到重复的另一边就删除，
删除后记录长度的起始位置为删除元素（重复元素）的下一个元素，所以为st[s[j]] + 1
'''


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]] + 1, i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))

