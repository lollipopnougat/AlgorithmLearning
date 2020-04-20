class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        if str_len <= 1:
            return s
        str_map = {}
        def palindrome_len(n1:int, n2:int) -> int:
            length = 0
            while n1 >= 0 and n2 < str_len:
                if s[n1] == s[n2]:
                    length += 2
                    n1 -= 1
                    n2 += 1
                else:
                    break
            return length
        max_len = 1
        max_ind = 0
        max_type = 1

        for i in range(1, str_len):
            if s[i] == s[i - 1]:
                if i + 1 < str_len and s[i - 1] == s[i + 1]:
                    res_len = palindrome_len(i - 1, i + 1) + 1
                    if res_len > max_len:
                        max_len = res_len
                        max_ind = i
                        max_type = 1
                res_len = palindrome_len(i - 2, i + 1) + 2
                if res_len > max_len:
                    max_len = res_len
                    max_ind = i
                    max_type = 0
            else:
                res_len = palindrome_len(i - 1, i + 1) + 1
                if res_len > max_len:
                    max_len = res_len
                    max_ind = i
                    max_type = 1
        
        offest = max_len // 2
        res_str = ''
        if max_type:
            res_str = s[max_ind - offest:max_ind + offest + 1]
        else:
            res_str = s[max_ind - offest:max_ind + offest]
        return res_str



class Solution2:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        if str_len <= 1:
            return s
        str_map = {}
        def palindrome_len(n1:int, n2:int) -> int:
            length = 0
            while n1 >= 0 and n2 < str_len:
                if s[n1] == s[n2]:
                    length += 2
                    n1 -= 1
                    n2 += 1
                else:
                    break
            return length
        max_info = [1, 0, 1]
        for i in range(1, str_len):
            if s[i] == s[i - 1]:
                if i + 1 < str_len and s[i - 1] == s[i + 1]:
                    res_len = palindrome_len(i - 1, i + 1) + 1
                    if res_len > max_info[0]:
                        max_info = [res_len, i, 1]
                res_len = palindrome_len(i - 2, i + 1) + 2
                if res_len > max_info[0]:
                    max_info = [res_len, i, 0]
            else:
                res_len = palindrome_len(i - 1, i + 1) + 1
                if res_len > max_info[0]:
                    max_info = [res_len, i, 1]
        
        offest = max_info[0] // 2
        return s[max_info[1] - offest:max_info[1] + offest + 1] if max_info[2] else s[max_info[1] - offest:max_info[1] + offest]
s = Solution()
print(s.longestPalindrome("bppbsooos"))