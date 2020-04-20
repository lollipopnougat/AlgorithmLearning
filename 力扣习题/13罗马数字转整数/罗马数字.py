class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, j in enumerate(s):
            if i < len(s) - 1 and dic[j] < dic[s[i + 1]]:
                ans -= dic[j]
            else:
                ans += dic[j]
        return ans


s = Solution()

print(s.romanToInt('IV'))