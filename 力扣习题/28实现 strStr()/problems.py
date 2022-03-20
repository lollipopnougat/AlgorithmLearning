class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solutionkmp:
    def strStr(self, haystack: str, needle: str) -> int:
        next_arr = self.get_next(needle)
        tlen = len(haystack)
        plen = len(needle)
        if plen == 0:
            return 0
        i, j = 0, 0
        while i < tlen:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == plen:
                    return i - j
            elif j == 0:
                    i += 1
            else:
                j = next_arr[j - 1]
        return -1

    def get_next(self, text:str) -> list:
        length = len(text)
        next_arr = [0] * length
        i, j = 1, 0
        while i < length:
            if text[i] == text[j]:
                j += 1
                next_arr[i] = j
                i += 1
            elif j == 0:
                next_arr[i] = 0
                i += 1
            else:
                j = next_arr[j - 1]
        return next_arr

hay = "hello"
ne = "ll"

s = Solution()
sk = Solutionkmp()

print(s.strStr(hay, ne))
print(sk.strStr(hay, ne))