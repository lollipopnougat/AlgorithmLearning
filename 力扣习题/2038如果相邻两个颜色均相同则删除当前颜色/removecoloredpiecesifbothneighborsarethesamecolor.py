class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        '''
        本题本质就是寻找 'AAA' 和 'BBB' 的个数，并进行比较 a > b ， 两人删除的过程中，互不干扰
        '''
        a = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    a -= 1
        return a > 0

class Solution2:
    def winnerOfGame(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = 'C', 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[ord(cur) - ord('A')] += 1
        return freq[0] > freq[1]

class Solution3:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        l = len(colors)
        for i in range(l - 2):
            if colors[i:i + 3] == 'AAA':
                count += 1
            if colors[i:i + 3] == 'BBB':
                count -= 1
        return count > 0

s = Solution()

print(s.winnerOfGame('AAABABB'))
print(s.winnerOfGame('AABABB'))