class Solution:
    def countSubstrings(self, s: str) -> int:
        self.n = 0
        def dfs(st):
            length = len(st)
            if length == 0:
                return
            elif length == 1:
                self.n += 1
            else:
                if st == st[::-1]:
                    self.n += 1
                for i in range(1, length):
                    if st[:-i] == st[:-i][::-1]:
                        self.n += 1
                dfs(st[1:])
        dfs(s)
        return self.n

class Solution2:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

class Solution3:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [0] * length
        c = 0
        for i in range(length):
            dp[i] = 1
            c += 1
            for j in range(i):
                if s[j] == s[i] and dp[j + 1] == 1:
                    dp[j] = 1
                    c += 1
                else:
                    dp[j] = 0
        return c
    
s = Solution3()

print(s.countSubstrings('aaa'))