'''
6021. 字符串中最多数目的子字符串 显示英文描述 
题目难度Medium
给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。

你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。注意，这个字符可以插入在 text 开头或者结尾的位置。

请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。

子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。

 

示例 1：

输入：text = "abdcdbc", pattern = "ac"
输出：4
解释：
如果我们在 text[1] 和 text[2] 之间添加 pattern[0] = 'a' ，那么我们得到 "abadcdbc" 。那么 "ac" 作为子序列出现 4 次。
其他得到 4 个 "ac" 子序列的方案还有 "aabdcdbc" 和 "abdacdbc" 。
但是，"abdcadbc" ，"abdccdbc" 和 "abdcdbcc" 这些字符串虽然是可行的插入方案，但是只出现了 3 次 "ac" 子序列，所以不是最优解。
可以证明插入一个字符后，无法得到超过 4 个 "ac" 子序列。
示例 2：

输入：text = "aabb", pattern = "ab"
输出：6
解释：
可以得到 6 个 "ab" 子序列的部分方案为 "aaabb" ，"aaabb" 和 "aabbb" 。
 

提示：

1 <= text.length <= 105
pattern.length == 2
text 和 pattern 都只包含小写英文字母。
'''


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        l = len(text)
        res = []
        ans = 0
        cx = cy = 0
        for i in range(l):
            if text[i] == pattern[0]:
                cx += 1
                res.append(text[i])
            elif text[i] == pattern[1]:
                cy += 1
                res.append(text[i])
        if cx > cy:
            res.append(pattern[1])
            l = len(res)
            ans += cx
            for i in range(l - 1):
                if res[i] == pattern[0]:
                    for j in range(i + 1, l - 1):
                        if res[j] == pattern[1]:
                            ans += 1
        else:
            res.insert(0, pattern[0])
            l = len(res)
            ans += cy
            for i in range(1, l - 1):
                if res[i] == pattern[0]:
                    for j in range(i + 1, l):
                        if res[j] == pattern[1]:
                            ans += 1
        return ans


class Solutionn:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        l = len(text)
        cx = cy = 0
        ans = 0
        dp = [0] * l
        for i in text:
            if i == pattern[0]:
                cx += 1
            elif i == pattern[1]:
                cy += 1
        if pattern[0] == pattern[1]:
            cx += 1
            return cx * (cx - 1) // 2
        if cy > cx:
            dp[-1] += 1
        for i in range(l):
            if text[i] == pattern[0]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
                if text[i] == pattern[1]:
                    ans += dp[i]
        if cx >= cy:
            ans += dp[-1]
        return ans


s = Solution()

print(
    s.maximumSubsequenceCount(
        'vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign',
        'rr'))
print(s.maximumSubsequenceCount('cca', 'ac'))
print(s.maximumSubsequenceCount('acac', 'ac'))
print(s.maximumSubsequenceCount('iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik',
                                'mp'))
print(s.maximumSubsequenceCount('rozsjqzottomeiytlvkenctevztfjlgszlv', 'tc'))
print(s.maximumSubsequenceCount('a', 'ac'))
print(s.maximumSubsequenceCount('ac', 'ac'))
print(s.maximumSubsequenceCount('abdcdbc', 'ac'))
print(s.maximumSubsequenceCount('aabb', 'ab'))
print(s.maximumSubsequenceCount('aabb', 'ac'))
print(' ')
s = Solutionn()

print(
    s.maximumSubsequenceCount(
        'vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign',
        'rr'))
print(s.maximumSubsequenceCount('cca', 'ac'))
print(s.maximumSubsequenceCount('acac', 'ac'))
print(s.maximumSubsequenceCount('iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik',
                                'mp'))
print(s.maximumSubsequenceCount('rozsjqzottomeiytlvkenctevztfjlgszlv', 'tc'))
print(s.maximumSubsequenceCount('a', 'ac'))
print(s.maximumSubsequenceCount('ac', 'ac'))
print(s.maximumSubsequenceCount('abdcdbc', 'ac'))
print(s.maximumSubsequenceCount('aabb', 'ab'))
print(s.maximumSubsequenceCount('aabb', 'ac'))
